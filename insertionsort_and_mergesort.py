import numpy as np
import matplotlib.pyplot as plt
import timeit


class SortingAlgorithms():

    @staticmethod
    def insertion_sort(array):

        for j in range(1, len(array)):

            key = array[j]

            i = j - 1
            while i >= 0 and array[i] > key:
                array[i + 1] = array[i]
                i = i - 1
            array[i + 1] = key

    @staticmethod
    def merge(array, start, midpoint, end):

        n1 = midpoint - start + 1
        n2 = end - midpoint

        left = [None] * n1
        right = [None] * n2

        for i in range(0, n1):
            left[i] = array[start + i]

        for j in range(0, n2):
            right[j] = array[midpoint + j + 1]

        i, j = 0, 0

        for k in range(start, end + 1):
            if i < n1 and (j >= n2 or left[i] <= right[j]):
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1


    @staticmethod
    def merge_sort(array, start, end):

        if start < end:

            midpoint = (start + end) // 2

            SortingAlgorithms.merge_sort(array, start, midpoint)
            SortingAlgorithms.merge_sort(array, midpoint + 1, end)

            SortingAlgorithms.merge(array, start, midpoint, end)


class SortingEval():
    '''

    '''

    def __init__(self, test_range=1000):
        self.insertsort_data = []
        self.mergesort_data = []
        self.test_range = test_range + 1

    def time_runs(self):

        testing_array = []
        for x in range(1, self.test_range):
            testing_array.insert(0, x)

            insert_timer = timeit.Timer(lambda: SortingAlgorithms.insertion_sort(testing_array.copy()))
            insert_runtime = insert_timer.timeit(number=3)
            self.insertsort_data.append(insert_runtime)

            start = 0
            end = len(testing_array) - 1
            merge_timer = timeit.Timer(lambda: SortingAlgorithms.merge_sort(testing_array.copy(), start, end))
            merge_runtime = merge_timer.timeit(number=3)
            self.mergesort_data.append(merge_runtime)



    def make_graph(self,create=True):


        if create:
            x_values = list(range(1, self.test_range))
            plt.plot(x_values, self.insertsort_data, label='Insertion Sort')

            plt.plot(x_values, self.mergesort_data, label='Merge Sort')
            plt.xlabel('n')
            plt.ylabel('Seconds')
            plt.legend()
            plt.show()







if __name__ == "__main__":

    se = SortingEval(test_range = 100)
    se.time_runs()
    se.make_graph()
