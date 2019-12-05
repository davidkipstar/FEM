import copy 
import logging
from FME import FME
from utils import _parser

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def image(M, A, b):
    #TODO:
    #   like in exercise session 4
    #   image of polyhedron under
    #   affine mapping
    #   with block structure matrix
    #size of submatrices
    M_m, M_n = len(M), len(M[0])
    A_m, A_n = len(A), len(A[0])

    #Size of final matrix
    m = 2*M_m + A_m
    n = M_n   + M_m

    #generate pos and neg identity matrix
    I_pos = [[0 if i != j else 1  for i in range(M_m)] for j in range(M_m)]
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

    A_new = M_pos + M_neg + A_in
    #create new b vector whcih is redudant
    b_new = [0 for i in range(2*M_m)]
    b_new.extend(b)
    #project onto dimension of n-A_n
    A_new_proj, b_new_proj = FME(A_new, b_new, M_n, n)

    return A_new_proj, b_new_proj
