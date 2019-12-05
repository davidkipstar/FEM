import copy 
import logging
from FME import FME

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def image(M, A, b):
    #rows, column
    M_m, M_n = len(M), len(M[0])
    A_m, A_n = len(A), len(A[0])

    m = 2*M_m + A_m
    n = M_n   + M_m

    I_pos = [[0 if i != j else 1 for i in range(M_m)] for j in range(M_m)]
    I_neg = [[0 if i != j else -1 for i in range(M_m)] for j in range(M_m)]

    #First Block
    M_pos = copy.deepcopy(M)
    for i in range(M_m):
        M_pos[i].extend(I_neg[i])
    logging.debug(f"M_pos: {M_pos}")

    #Second Block
    M_neg = copy.deepcopy(M)
    for i in range(M_m):
        for j in range(M_n):
            M_neg[i][j] = -1*M_neg[i][j]
        M_neg[i].extend(I_pos[i])
    logging.debug(f"M_neg: {M_neg}")

    #Third Block
    A_in = copy.deepcopy(A)
    for i in range(A_m):
        A_in[i].extend([0 for j in range(M_m)])

    logging.debug(f"A_in: {A_in}")

    #Combine Matrix
    A_new = M_pos + M_neg + A_in
    
    b_new = [0 for i in range(2*M_m)]
    b_new.extend(b)
    #print(M)
    #print("M_n=",M_n)
    #print(M_m)
#    print("A_new=", A_new)
#    print(b_new)
    #print(A_n)
    #print(len(A_new))
    A_new_proj, b_new_proj = FME(A_new, b_new, A_m, n)
    return A_new_proj, b_new_proj
    
#if __name__ == '__main__':
    
#    M = [[1, 0],
#        [0, 0],
#        [0, 0]]

#    A = [[1, 0],[0, 1]]
#    b = [0, 0]

#    logging.debug(f"M:{M}")
#    logging.debug(f"A:{A}")
#    logging.debug(f"b:{b}")
#    print(image(M,A,b))
