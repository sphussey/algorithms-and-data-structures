import numpy as np


'''
Matrix chain multiplication

Our goal is only to determine an order for multiplying 
# matrices that has the lowest cost. Typically, the time 
# invested in determining this optimal order is more than 
# paid for by the time saved later on when actually 
# performing the matrix multiplications (such as performing 
# only 7500 scalar multiplications instead of 75,000).




'''


class MatrixMultiplyError(Exception):
    '''
    Custom exeption for handling Matrix Multiplication errors
    '''
    pass


def matrix_multiply(A, B):
    '''
    For matrix multiplication, the number of columns in the first
    matrix must be equal to the number of rows in the second matrix.
    The result matrix has the number of rows of the first and the
    number of columns of the second matrix.
    :param A: 2- dimentional np.array
    :param B: 2- dimentional np.array
    :raise: if a_cols != b_rows: MatrixMultiplyError('incompatible dimensions')
    :return: 2- dimentional np.array product of matrix multiplication
    '''
    # convert A and B to np.arrays just in case
    # this can should be handled more efficiently
    a, b = np.array(A), np.array(B)

    #determine the number of columns and rows
    a_rows, a_cols = a.shape
    b_rows, b_cols = b.shape

    #assess premise for matrix multiplication
    if a_cols != b_rows:
        raise MatrixMultiplyError('incompatible dimensions')


    else:
        # Create a 2-D matrix called "C" with the dimentions
        # A:rows x B:columns
        C = np.zeros((a_rows,b_cols))
        print(C)

        # loop through each element in the matrix and compute
        # the matrix multiplication by
        for i in range(0, a_rows):
            for j in range(0, b_cols):
                for k in range(0, a_cols):
                    C[i, j] = C[i, j] + A[i, k] * B[k,j]
        return C


def matrix_chain_order(p: np.array) -> np.array:
    '''
    matrix chain order determines the optimal number of scalar
    multiplications needed to compute a matrix-chain product, it does
    not directly show how to multiply the matrices.
    :param p: 1-D np.array
    :return:
    '''


    n = len(p)
    m = np.zeros((n,n))
    s = np.zeros((n-1, n-1))

    # make the diagnonal zeros
    for i in range(0, n):
        m[i,i] = 0

    print(m)

    for l in range(2,n):
        for i in range(0,(n -l + 1)):

            j = i + l - 1
            # set elements in the matrix above the diagnol to infinity
            m[i, j] = np.inf

            for k in range(i, j - 1):
                # optimal substructure is found by dividing the sequence
                # of matrices A[i….j] into two parts A[i,k] and A[k+1,j]
                q = m[i, k] + m[k + 1, j] + (p[i] * p[k] * p[j]) # multiply matricies Pi-1 Pk Pj
                print("i : ",i, " j : ", j, " m[i, j] : ", m[i,j])
                if q > m[i,j]:
                    m[i, j] = q
                    s[i, j] = k




        return [m, s]

def print_optimal_parents(s, i, j):
    '''

    :param s:
    :param i:
    :param j:
    :return:
    '''
    if i == j:
        print('A')
        return 'A'
    else:
        print("(")
        print_optimal_parents(s, i , s[i, j])
        print_optimal_parents(s, s[i, j])
        print(")")



def main():
    # confirm in any efficiency loss from duplicates in an array



    m1 = np.array([[1,2,3,4], [1,2,3,4], [1,2,3,4], [1,2,3,4]])
    m2 = np.array([[1,2,3,4], [1,2,3,4], [1,2,3,4], [1,2,3,4]])
    C = matrix_multiply(m1, m2)
    print(C)

    p = np.array([1, 6, 4, 3, 7, 2, 4, 3, 6, 8, 9, 9])
    ms = matrix_chain_order(p)
    print(ms[0])
    print(ms[1])




if __name__ == "__main__" :
    main()

