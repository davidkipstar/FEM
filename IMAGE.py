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
    First_block = []

    for i in range(M_m):
        L = I_neg[i]
        L.extend(M_pos[i])
        logging.debug(f" {len(L)}")
        First_block.append(L)

    #logging.debug(f"First Block: {First_block}")
    
    Second_block = []
    for i in range(M_m):
        logging.debug(f" {len(L)}")
        L = I_pos[i]
        L.extend(M_neg[i])
        Second_block.append(L)

    #logging.debug(f"Second Block: {Second_block}")

    #Third Block
    Third_block = []
    A_in = copy.deepcopy(A)
    for i in range(A_m):
        logging.debug([0 for i in range(M_m)])
        L = [0 for i in range(M_m)]
        L.extend(A_in[i])
        logging.debug(f" {len(L)}")
        Third_block.append(L)
    
    #logging.debug(f"Third_block: {Third_block}")
    A_new = First_block + Second_block + Third_block 
    logging.info(f"A_new: {A_new}")

    #create new b vector whcih is redudant
    b_new = [0 for i in range(2*M_m)]
    b_new.extend(b)
    logging.info(f"b_new: {b_new}")
    
    logging.info( f"b_new: size : {len(b)} + {M_n}")
    logging.info( f"\t rows: {len(A_new)}, cols: {len(A_new[0])}")
    logging.debug(f"")

    logging.debug(f"From {len(A_new[0])} to {2*M_m}")
    A_new_proj, b_new_proj = FME(A_new, b_new, M_m, len(A_new)) 
    logging.debug(f"A_new_proj: {A_new_proj}")
    logging.debug(f"b_new_proj: {b_new_proj}")

    return A_new_proj, b_new_proj
