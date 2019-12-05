
  
def test_project(instancefile,solutionfile,testpointfile):
  with open(instancefile,'r') as instances:
    with open(solutionfile,'r') as solutions:
      inputline = instances.readline()
      while inputline !="":
        assert inputline[0]=='k'
        k = inputline.split()[1]
        inputline = instances.readline()
        with open("tempinput.in",'w') as tempinput:
          while inputline != "" and inputline[0] != 'k':
            tempinput.write(inputline)
            inputline = instances.readline()
        run(["truncate", "-s", "-1", "tempinput.in"])
        result = run(["./fourier-motzkin.sh", "project", "tempinput.in", k, "outfile.ot"], stdout=PIPE, stderr=STDOUT)
        print("output test project: "+result.stdout.decode('utf-8'))
        solA = []
        solutionline = solutions.readline()
        assert solutionline=="A\n"
        solutionline = solutions.readline()
        while solutionline != "b\n":
          solA.append(list(map(float,solutionline.split(" "))))
          solutionline = solutions.readline()
        solutionline = solutions.readline()
        solb = list(map(float,solutionline.split(" ")))
        with open("outfile.ot",'r') as outfile:
          A = []
          outline = nextline(outfile)
          assert outline=="A"
          outline = nextline(outfile)
          while outline != "" and outline != "b":
            A.append(list(map(float,outline.split(" "))))
            outline = nextline(outfile)
          if outline == "" or outline == "\n":
            raise Exception("No correct output file")
          outline = nextline(outfile)
          if outline == "" or outline == "\n":
            print("Empty b vector")
            b = []
          else:
            b = list(map(float,outline.split(" ")))
        n = len(solA[0])
        with open(testpointfile,'r') as testpoints:
          points = []
          testline = testpoints.readline()
          assert testline[0] == "n"
          while testline != "n {}\n".format(n):
            testline = testpoints.readline()
          testline = testpoints.readline()
          while testline != "" and testline != "\n" and testline[0] != 'n':
            points.append(list(map(float,testline.split(" "))))
            testline = testpoints.readline()
        if not testequalpolyhedra((A,b),(solA,solb),points):
          return False
  return True

if __name__ == '__main__':
    print("Test project: {}".format(test_project("project_instances.dat","project_solutions.dat","testpoints.dat")))
