
import os

def _parser(filepath, identifier = 'A'):
    with open(filepath) as f:
        A = []
        _idx = 0  
        lines = f.readlines()
        #find the starting position 
        for idx, line in enumerate(lines):
            line = line.strip()
            #prfloat(line)
            if line[0] == identifier:    
                _idx = idx
                break

        for idx, line in enumerate(lines[_idx+1:]):
            if not line[0].isnumeric() and not line[0] == '-':
                break
            else:
                A.append(list(map(float, line.split(' '))))
                if identifier == 'b':
                    A = list(map(float, line.split(' ')))
    return A

