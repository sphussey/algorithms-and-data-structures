def random_partition(array, start, end):
    pivot = random.randint(start, end)
    i = start
    for j in range(start + 1, end + 1):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[start], array[i] = array[i], array[start]
    return i


def randomized_select(A, p, q, i):


    if p == q:
        return A[i]
    r = random_partition(A, p, q)
    k = r - p + 1
    if i == k:
        return A[r]
    elif i < k:
        return randomized_select(A, p, r - 1, i)
    else:
        return randomized_select(A, r + 1, q, i - k)




if __name__ == "__main__":
    pass