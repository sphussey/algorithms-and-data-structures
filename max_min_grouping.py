import numpy as np


class MinMaxGroupingError(Exception):
    pass

def min_max_grouping(A: list, N: int, M: int):
    '''

    :param A:
    :param N: index of the last element in the array (length - 1 for index)
    :param M: number of groups you wish to partition the array into
    :return G: array
    '''

    # confirm that all values are non-zero positive integers
    for x in A:
        if x < 1 or not isinstance(x, int):
            raise MinMaxGroupingError("Your array must consist of positive integers!")
            return

    #print(f"A = {A}")
    #print(f"N = {N}")
    #print(f"M = {M}")
    # initalize G with M elements
    G = [0 for i in range(0, M)]
    # initalize G with M elements
    B = [0 for i in range(0, M)]
    # initalize C as 2-d array (matrix) with M rows and N columns
    C = np.zeros((M, N), dtype=int)

    # for first row of C, C[0][i] is the cumulative sum of A[0:i]
    for i in range(0, N):
        if i == 0:
            C[0][i] = A[i]
        else:
            C[0][i] = C[0][i - 1] + A[i]


    for j in range(1, M):
        for i in range(j, N + 1):
            B_max = 0
            for k in range(j - 1 , i):
                B_max = max(B_max, min(C[j - 1][k], np.sum(A[k+1:i])))
            C[j][i - 1] = B_max


    #print("C = ", C, sep="\n")

    for j in range(0, M - 1):
        for i in range(j, N):
            if C[j][i] == C[M - 1][N - 1]:
                G[j] = i + 1
                break
            elif C[M - 1][N - 1] not in C[j] and C[j][i] > C[M - 1][N - 1]:
                G[j] = i + 1
                break
    G[M - 1] = N

    for j in range(len(G)):
        if j == 0:
            B[j] = sum(A[0:G[j]])
        else:
            B[j] = sum(A[G[j-1]:G[j]])

    #print(f"Bopt = {B}")

    for i in range(M - 1, 0, -1):
        G[i] = G[i] - G[i - 1]

    #print(f"Gopt = {G}")
    return G

def main():
    a1 = [3, 9, 7, 8, 2, 6, 5, 10, 1, 7, 6, 4]
    n1 = len(a1)
    m1 = 3
    #print("grouping1")
    min_max_grouping(a1, n1, m1)
    a2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    n2 = len(a2)
    m2 = 4
    #print("grouping2")
    min_max_grouping(a2, n2, m2)
    a3 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    n3 = len(a3)
    m3 = 3
    #print("grouping3")
    min_max_grouping(a3, n3, m3)
    a4 = [3, 9, 7, 8, 2, 6, 5, 10, 1, 7, 6, 4]
    n4 = len(a4)
    m4 = 4
    #print("grouping4")
    min_max_grouping(a4, n4, m4)
    a5 = [3, 9, 7, 8, 2, 6, 5, 10, 1, 7, 6, 4, 40, 3, 5, 2, 9, 8, 10]
    n5 = len(a5)
    m5 = 3
    #print("grouping5")
    min_max_grouping(a5, n5, m5)
    a6 = [3, 9, 7, 8, 2, 6, 5, 10, 1, 7, 6, 4, 40, 3, 5, 2, 9, 8, 10]
    n6 = len(a6)
    m6 = 7
    #print("grouping6")
    min_max_grouping(a6, n6, m6)
    a7 = [3, 9, 7, 14, 3, 5, 2, 9, 8, 10]
    n7 = len(a7)
    m7 = 3
    #print("grouping7")
    min_max_grouping(a7, n7, m7)


if __name__ == "__main__":
    main()
