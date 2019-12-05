import sys
from FME import FME
from IMAGE import IMAGE
with open(sys.argv[1], "rt") as f:
    lines = f.read().splitlines()
del lines[0], lines[0], lines[-2]

b_1 = lines[-1]
b_spl = b_1.split(" ")
b_test = []
for i in range(len(b_spl)):
    b_test.append(float(b_spl[i]))
del lines[-1]

lines2 = []
for i in range(len(lines)):
    lines2.append(lines[i].split(" "))

A_test = [[0 for i in range(len(lines2[0]))] for j in range(len(lines2))]

for i in range(len(lines2)):
    for j in range(len(lines2[0])):
        A_test[i][j] = float(lines2[i][j])
i = 0
n_test = len(A_test[0])
k_test = int(sys.argv[2])
print(A_test)
P_res, b_res = FME(A_test, b_test, k_test, n_test)

#P2_res, b2_res = FME(P_res, b_res, 1, 2)
print(P_res)
print(b_res)
