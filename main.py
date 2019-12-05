#!/usr/bin/env python
import sys
import copy
import os 
import os 
import logging

from IMAGE import image 
from PROJECT import project
from CONVEX import convex_hull
from COMPUTE import compute_x_or_y

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def _write(fname, **data):
    try:
        logging.debug(f"Writing to {fname}: \n {data}")
        
        with open(fname, 'w') as f:
            for key, matrix in data.items():
                f.write(key)
                f.write('\n')
                if key == 'b':
                    logging.debug("b")
                    line =  ' '.join(list(map(str, matrix)))
                    logging.debug(line)
                    f.write(line)
                    f.write('\n')
                if key == 'A':
                    logging.debug(f"{key}")
                    for row in matrix:
                        line = ' '.join(list(map(str, row)))
                        logging.debug(line)
                        f.write(line)
                        f.write('\n')
        return True

    except Exception as e:
        print(e)

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

        logging.debug(f"Parsed {identifier}: \n {A}")
    return A

argv = sys.argv
arg = sys.argv[1]
if arg == 'project':
    input_file = argv[2]
    k = int(argv[3])
    
    A =  _parser(input_file, identifier = 'A')
    b =  _parser(input_file, identifier = 'b')
    
    logging.debug(f"A : {A}")
    logging.debug(f"b : {b}")
    n = len(A[0])
    A, b = project(A,b, k, n)
    output_file = argv[4]

    _write(output_file, **{
            'A' : A,
            'b' : b
            })

elif arg == 'image':
    input_file_1 = argv[2]
    input_file_2 = argv[3]
    output_file  = argv[4]
    
    A =  _parser(input_file_1, identifier = 'A')
    b =  _parser(input_file_1, identifier = 'b')
    
    M =  _parser(input_file_2, identifier = 'M')
    logging.debug(f"M : {M}")
    logging.debug(f"A : {A}")
    logging.debug(f"b : {b}")

    A, b = image(M, A, b)
    _write(output_file, **{
            'A' : A,
            'b' : b
            })

elif arg == 'H_representation':
    print("H Representation")
    input_file = argv[2]
    output_file  = argv[3]
    
    X =  _parser(input_file, identifier = 'X')

    A, b = convex_hull(X)

    _write(output_file, **{
            'A' : A,
            'b' : b
            })

elif arg == 'compute_x_or_y':
    input_file = argv[2]
    output_file  = argv[3]

    A = _parser(input_file, identifier = 'A')
    b = _parser(input_file, identifier = 'b')

    BOOL, x = compute_x_or_y(A, b)

    logging.debug(f"{BOOL} : {x}")
