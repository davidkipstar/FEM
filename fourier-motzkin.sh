#!/bin/bash
#
#python3 main.py project './instances/project_test_1.dat' 2 './result_project.txt'
#python3 main.py image './instances/image_test_poly_1.dat' './instances/image_test_M_1.dat' './result_image.txt'
#python3 main.py H_representation './instances/H_representation_test_1.dat' './result_H_representation.txt'
#python3 main.py compute_x_or_y './instances/compute_x_or_y_test.dat'
#
python3 main.py  "$1" "$2" "$3" "$4" 
