import copy 
import logging
from _.FME import FME
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
    # #############
    # M_pos I_pos # 0
    # M_neg I_neg # 0
    # A     0     # b
    # ############# #

    M_m, M_n = len(M), len(M[0])
    A_m, A_n = len(A), len(A[0])
    logging.debug(f"M: {M}, A: {A}, b: {b}")
    logging.debug(f"Image with M has {M_m} rows, {M_n} columns")

    #Size of final matrix
    m = 2*M_m + A_m
    n = M_n   + M_m

    #generate pos and neg identity matrix
    I_pos = [[0 if i != j else 1  for i in range(M_m)] for j in range(M_m)]
    I_neg = [[0 if i != j else -1 for i in range(M_m)] for j in range(M_m)]

    M_pos = copy.deepcopy(M)
    M_neg = [[-1*M[i][j] for j in range(M_n)] for i in range(M_m)]

    #First Block
    for i in range(M_m):
        I_neg[i].extend(M_pos[i])
        #M_pos[i].extend(I_neg[i])
    logging.debug(f"First Block: {I_neg}")
    First_block = copy.deepcopy(M_neg)

    #Second Block
    M_neg = copy.deepcopy(M)
    
    for i in range(M_m):
        #for j in range(M_n):
        #    M_neg[i][j] = -1*M_neg[i][j]
        #M_neg[i].extend(I_pos[i])
        I_pos[i].extend(M_neg[i])

    logging.debug(f"Second Block: {I_pos}")
    Second_block = copy.deepcopy(I_pos)

    #Third Block
    A_in = copy.deepcopy(A)
    Third_block = []
    for i in range(A_m):
        logging.debug([0 for i in range(M_m)])
        logging.debug(A_in[i])
        logging.debug([0 for i in range(M_m)].extend(A_in[i]))
        Third_block.append([0 for i in range(M_m)].extend(A_in[i]))

    logging.debug(f"Third_block: {Third_block}")

    A_new = First_block + Second_block + Third_block 

    #create new b vector whcih is redudant
    b_new = [0 for i in range(2*M_m)]
    b_new.extend(b)

    logging.debug(f"Size: b: {len(b_new)}, A: {len(A_new)}")
    #project onto dimension of n-A_n
    #
    logging.debug(f"Project: M {M_n}, n: {n}, A_n: {A_n}")
    A_new_rows = 2*M_n+A_n
    logging.debug(f"\t rows: {A_new_rows} reduction: {A_new_rows - A_n}")

    A_new_proj, b_new_proj = FME(A_new, b_new, A_new_rows, A_new_rows - A_n)
    logging.debug(f"A_new_proj: {A_new_proj}")
    logging.debug(f"b_new_proj: {b_new_proj}")

    return A_new_proj, b_new_proj
