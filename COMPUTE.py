import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

from FME import FME 

def is_feasible(A, b, n):
    #check trivial feasible condition
    feasible = True
    for i in range(n):
        if A[i][0] == 0:
            if b[i] > 0:
                feasible = False
                break
    return feasible

def compute_x_or_y(A, b):
    #dummy solution 
    #TODO: 
    #   We need to savee each step in FME
    #   then we can reconstruct the interval described below
    #   for each increasing dimension we can then decide
    #   if it is still feasible or not anymore

    A, b = FME(A, b, 1, len(A))
    logging.debug(f"A: {A} \n b : {b}")
    
    n = len(A)
    A_neg = {}
    A_pos = {}

    if is_feasible(A, b, n):
        #

        for i in range(n):
            if A[i][0] < 0: 
                A_neg[i] = A[i][0]

            elif A[i][0] > 0:
                A_pos[i] = A[i][0]
            
        logging.debug(f"A_neg : {A_neg}")
        logging.debug(f"A_pos : {A_pos}")
        #calculate constraint coefficeint
        pos_coeff = [ b[i]/A[i][0] for i in A_pos.keys()]
        neg_coeff = [ b[i]/A[i][0] for i in A_neg.keys()]

        logging.debug(f"POS COE: {pos_coeff}")
        logging.debug(f"MIN POS: {neg_coeff}")
        #if one set is empty we found feasible solution
        if len(pos_coeff) == 0 or len(neg_coeff) == 0:
            return True

        min_pos_coeff = min(pos_coeff)
        max_neg_coeff = max(neg_coeff)

        logging.debug(f"MIN POS: {min_pos_coeff}")
        logging.debug(f"MAX NEG: {max_neg_coeff}")

        #check if intersection is non empty
        if min_pos_coeff < max_neg_coeff:
            return False
        else:
            return True
    else:
        return False
    

if __name__ == '__main__':
    #
    A = [[-1], [1], [1], [-1], [-2]]
    b = [1, -1, -1,  1, -3]

    print(compute_x_or_y(A, b))

