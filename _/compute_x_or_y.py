from FME import FME
def compute_x_or_y(A, b):
    n = len(A[0])
    k = 1
    A_proj_min, b_proj_min = FME(A, b, k, n)
#
    return A_proj_min, b_proj_min
    index_list = True

    for i in range(len(A)):
        if A[i][0] == 0:
            if b[i] > 0:
                index_list = False
                break
    return index_list
