import random


def max_heapify(array, n, i):
    '''
    The MAX-HEAPIFY procedure, which runs in O(lg n) time,
    is the key to maintaining the max-heap property.
    :param array: array
    :param n: length of array
    :param i: index
    '''
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and array[left] > array[largest]:
        largest = left

    if right < n and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        max_heapify(array, n, largest)

def build_max_heap(array):
    '''
    The BUILD-MAX-HEAP procedure, which runs in linear time,
    produces a max- heap from an unordered input array.
    :param array: array to be built into a max heap
    '''
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(array, n, i)

def heap_sort(array):
    '''
    The HEAPSORT procedure takes time O(n lg n), since the call
    to BUILD-MAX- HEAP takes time O(n) and each of the n - 1
    calls to MAX-HEAPIFY takes time O(lg n).
    :param array: array to be sorted
    '''

    build_max_heap(array)
    for i in range(len(array) - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        max_heapify(array, i, 0)



if __name__ == "__main__":
    array = list(range(1,101))
    random.shuffle(array)
    print(array)
    heap_sort(array)
    print(array)

