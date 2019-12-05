import copy 
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

from IMAGE import image

def transpose(X):
    m, n = len(X), len(X[0])
    X_T = [[0 for i in range(m)] for j in range(n)]
    
    for i in range(m):
        for j in range(n):
            X_T[j][i] = X[i][j]
    
    return X_T

def convex(A):
    #A is X
    #compute convex hull
    n, k = len(A), len(A[0])

    #Create Matrix
    # with last two rows consisting of ones
    #   because we need to have sum(lambda_i) == 1
    A_new = [[1 if i == j else 0 for i in range(k+2)] for j in range(k+2)]

    for i in range(k+2):
        A_new[-1][i] = 1
        A_new[-2][i] = 1

    #call project
    logging.debug(A_new)    
    b_new = [0 for i in range(n)] 
    b_new.append(1)
    b_new.append(-1)
    return A_new, b_new

def convex_hull(X):
    #transpose
    #X = transpose(X)
    A, b = convex(X)
    return image(X, A, b)

