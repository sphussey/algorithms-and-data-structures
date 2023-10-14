import timeit
import random
from quicksort_algorithms import QuicksortVariants



class Quicksort_new_Variants():

    @staticmethod
    def quicksort_3(array, start, end):
        if start < end:
            repeated = Quicksort_new_Variants.partition_3(array, start, end)
            Quicksort_new_Variants.quicksort_3(array,start, repeated[0] - 1)
            Quicksort_new_Variants.quicksort_3(array,repeated[1] + 1, end)


    @staticmethod
    def partition_3(array, start, end):
        pivot = array[start]
        repeated = [0, 0]
        i = start

        while i <= end:
            if array[i] < pivot:
                array[i], array[start] = array[start], array[i]
                start += 1
                i += 1
            elif array[i] == pivot:
                i += 1
            else:
                array[i], array[end] = array[end], array[i]
                end -= 1
        repeated[0], repeated[1] = start, end
        return repeated

    @staticmethod
    def quicksort_random_3(array, start, end):
        if start < end:
            repeated = Quicksort_new_Variants.partition_random_3(array, start, end)
            Quicksort_new_Variants.quicksort_random_3(array,start, repeated[0] - 1)
            Quicksort_new_Variants.quicksort_random_3(array,repeated[1] + 1, end)

    @staticmethod
    def partition_random_3(array, start, end):
        pivot = array[random.randint(start, end)]
        repeated = [0, 0]
        i = start

        while i <= end:
            if array[i] < pivot:
                array[i], array[start] = array[start], array[i]
                start += 1
                i += 1
            elif array[i] == pivot:
                i += 1
            else:
                array[i], array[end] = array[end], array[i]
                end -= 1
        repeated[0], repeated[1] = start, end
        return repeated


if __name__ == "__main__":

    quicksort_normal_runtime_data = []
    quicksort_random_runtime_data = []
    quicksort3_normal_runtime_data = []
    quicksort3_random_runtime_data = []
    lst = [1,1,1,1,1,1,1,1,2,2,2,2,7,7,77,3,5,2,67,3,5,2,7,4,4,99,66,3,4,3,5,7,5,3,5,7,4,3,5,7,5,32,45,7,5,4,3,5,7,8,5,3,3,2,4,6,7,5,3]
    lst2 = [33,66,44,22,33,55,33,77,55,99,22,33,55,44,33,55,66,11,99,55,77,55,33,22,11]
    start, end = 0, len(lst) - 1
    quick_non_random_timer = timeit.Timer(lambda: QuicksortVariants.quicksort_from_class(lst.copy(), start, end))
    for i in range(0, 5):
        quick_non_random_runtime = quick_non_random_timer.timeit(number=1)
        quicksort_normal_runtime_data.append(quick_non_random_runtime)

    quick_random_timer = timeit.Timer(lambda: QuicksortVariants.quicksort_class_random(lst.copy(), start, end))
    for i in range(0, 5):
        quick_random_runtime = quick_random_timer.timeit(number=1)
        quicksort_random_runtime_data.append(quick_random_runtime)

    quick3_non_random_timer = timeit.Timer(lambda: Quicksort_new_Variants.quicksort_3(lst.copy(), start, end))
    for i in range(0, 5):
        quick3_non_random_runtime = quick3_non_random_timer.timeit(number=1)
        quicksort3_normal_runtime_data.append(quick3_non_random_runtime)

    quick3_random_timer = timeit.Timer(lambda: Quicksort_new_Variants.quicksort_random_3(lst.copy(), start, end))
    for i in range(0, 5):
        quick3_random_runtime = quick_random_timer.timeit(number=1)
        quicksort3_random_runtime_data.append(quick3_random_runtime)

    print("quicksort_normal_runtime_data", quicksort_normal_runtime_data)
    print("quicksort_random_runtime_data", quicksort_random_runtime_data)
    print("quicksort3_normal_runtime_data", quicksort3_normal_runtime_data)
    print("quicksort3_random_runtime_data", quicksort3_random_runtime_data)

