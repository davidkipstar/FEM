from testscript import *

def test_compute_x_or_y(instancefile):
    
  with open(instancefile,'r') as instances:
    inputline = instances.readline()
    while inputline !="":
      assert inputline=="A\n"
      with open("tempinput.in",'w') as tempinput:
        tempinput.write(inputline)
        A = []
        inputline = instances.readline()
        while inputline != "" and inputline != "b\n":
          tempinput.write(inputline)
          A.append(list(map(float,inputline.split(" "))))
          inputline = instances.readline()
        tempinput.write(inputline)
        inputline = instances.readline()
        tempinput.write(inputline)
      b = list(map(float,inputline.split(" ")))
      inputline = instances.readline()

      run(["truncate", "-s", "-1", "tempinput.in"])
      
      result = run(["./fourier-motzkin.sh", 
                    "compute_x_or_y", 
                    "tempinput.in"], stdout=PIPE, stderr=PIPE, encoding='utf-8')

      print("output test compute_x_or_y: "+result.stderr)
      output = literal_eval(result.stdout)
      print(output)
      if not test_x_or_y(output,A,b):
        return False
  return True

if __name__ == '__main__':
    test_compute_x_or_y("project_solutions.dat")
