import numpy as np

def longest_common_subsequence_length(X, Y):
    '''

    :param X:
    :param Y:
    :return:
    '''
    m = len(X)
    n = len(Y)
    # create a 2d array with m rows and n columns
    b, c = np.zeros((m,n)), np.zeros((m,n))
    for i in range(0,m):
        for j in range(0,n):
            if X[i] == Y[j]:
                # might need to handle the case where i=0, or j=0
                b[i, j] = c[i - 1, j - 1] + 1
