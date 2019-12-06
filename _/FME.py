import logging 
import math

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)

def FME(A, b, k, n):
    n_it = n - k
    logging.debug("FME")
    for m in range(n_it):
   
        if A == [0 for j in range(n)]:
            A = [[0] for j in range(n-1)]
            b = [0 for j in range(n-1)]
            logging.debug(f"A: {A}, b: {b}")
            return A, b 

        else:
            n_pos, n_neg, n_zero = 0, 0, 0
            for i in range(len(A)):
                if A[i][n-1] > 0:
                    n_pos = n_pos + 1
                elif A[i][n-1] < 0:
                    n_neg = n_neg + 1
                else:
                    n_zero = n_zero + 1

            x_n_bigger = [[0 for i in range(n)] for j in range(n_pos)]
            x_n_smaller = [[0 for i in range(n)] for j in range(n_neg)]
            x_n_zero = [[0 for i in range(n)] for j in range(n_zero)]
            t = 0
            t2 = 0
            t3 = 0

            for i in range(len(A)):
                if A[i][n-1] > 0:
                    x_n_bigger[t][0] = float(b[i]/A[i][n-1])#teiler änder
                    for j in range(len(A[0])-1):
                        x_n_bigger[t][j+1] = float(-A[i][j]/A[i][n-1])
                    t = t+1

                elif A[i][n - 1] < 0:
                    x_n_smaller[t2][0] = float(b[i]/A[i][n-1])
                    for j in range(len(A[0]) - 1):
                        x_n_smaller[t2][j+1] = float(-A[i][j] / A[i][n - 1])
                    t2 = t2 + 1

                else:
                    x_n_zero[t3][0] = int(b[i])
                    for j in range(len(A[0]) - 1):
                        x_n_zero[t3][j+1] = float(A[i][j])
                    t3 = t3 + 1

#            print("bigger", x_n_bigger)
#            print(x_n_smaller)
#            print(x_n_zero)

            P_proj = []
            fill = [0 for i in range(n)]
            for i in range(n_pos):

                for j in range(n_neg):
                    for k in range(n):
                        fill[k] = -x_n_bigger[i][k] + x_n_smaller[j][k]
                    P_proj.append(fill[:])
#            print(P_proj)
            b_proj = [0 for i in range(len(P_proj))]

            for i in range(len(P_proj)):
                b_proj[i] = -P_proj[i][0]
                del P_proj[i][0]

            if n_zero > 0:
                for i in range(n_zero):
                    b_proj.append(x_n_zero[i][0])
                    del x_n_zero[i][0]
                    P_proj.append(x_n_zero[i][:])

            else:
                logging.debug("no zero constraints")
                pass

            if len(P_proj) == 0:
                P_proj = [0 for j in range(n - 1)]
                b_proj = [0]

            A = P_proj
            b = b_proj
            n = int(n-1)
    #logging.debug(f"FME: \n A: {A}, \n {b}")
    return A, b
