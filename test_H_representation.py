from testscript import *

def test_H_representation(instancefile,solutionfile,testpointfile):
  with open(instancefile,'r') as instances:
    with open(solutionfile,'r') as solutions:
      inputline = instances.readline()
      while inputline !="":
        assert inputline[0]=='X'
        inputline = instances.readline()
        with open("tempinput.in",'w') as tempinput:
          while inputline != "" and inputline != "X\n":
            tempinput.write(inputline)
            inputline = instances.readline()
        run(["truncate", "-s", "-1", "tempinput.in"])
        result = run(["./fourier-motzkin.sh", "H_representation", "tempinput.in", "outfile.ot"], stdout=PIPE, stderr=STDOUT)
        print("output test H_representation: "+result.stdout.decode('utf-8'))
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
          if outline == "":
            raise Exception("No correct output file")
          outline = nextline(outfile)
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
    test_H_representation("H_representation_instances.dat",
                            "H_representation_solutions.dat",
                            "testpoints.dat")
