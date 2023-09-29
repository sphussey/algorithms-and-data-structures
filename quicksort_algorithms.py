import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import itertools
import timeit
import random




class QuicksortVariants():

    @staticmethod
    def quicksort_from_class(array, start, end):
        if start < end:
            midpoint = QuicksortVariants.partition_from_class(array, start, end)
            QuicksortVariants.quicksort_from_class(array,start, midpoint - 1)
            QuicksortVariants.quicksort_from_class(array,midpoint + 1, end)


    @staticmethod
    def partition_from_class(array, start, end):
        pivot = array[start]
        i = start
        for j in range(start + 1, end + 1):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[start], array[i] = array[i], array[start]
        return i

    @staticmethod
    def quicksort_class_random(array, start, end):
        if start < end:
            midpoint = QuicksortVariants.partition_class_random(array, start, end)
            QuicksortVariants.quicksort_class_random(array,start, midpoint - 1)
            QuicksortVariants.quicksort_class_random(array,midpoint + 1, end)

    @staticmethod
    def partition_class_random(array, start, end):
        pivot = random.randint(start, end)
        i = start
        for j in range(start + 1, end + 1):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[start], array[i] = array[i], array[start]
        return i


class SortingEval():
    '''

    '''

    def __init__(self, test_range=50, n = 1000):
        self.quicksort_class_runtime_data = []
        self.quicksort_random_runtime_data = []
        self.test_range = test_range
        self.quicksort_class_worst_runtime_data = []
        self.quicksort_random_worst_runtime_data = []
        self.quicksort_class_runtime_increasing_n_data = []
        self.quicksort_random_runtime_increasing_n_data = []
        self.n = n + 1



    def time_runs(self):

        elements = list(range(1, self.test_range + 1))
        permutations = list(itertools.permutations(elements, self.test_range))
        for perm in permutations:

            start, end = 0, len(perm) - 1

            quick_non_random_timer = timeit.Timer(lambda: QuicksortVariants.quicksort_from_class(list(perm).copy(),start, end))
            quick_non_random_runtime = quick_non_random_timer.timeit(number=3)
            self.quicksort_class_runtime_data.append(quick_non_random_runtime)

            quick_random_timer = timeit.Timer(lambda: QuicksortVariants.quicksort_class_random(list(perm).copy(), start, end))
            quick_random_runtime = quick_random_timer.timeit(number=3)
            self.quicksort_random_runtime_data.append(quick_random_runtime)

            worst_case_array = list(range(1, self.test_range + 1))[::-1]
            quick_non_random_worst_timer = timeit.Timer(
                lambda: QuicksortVariants.quicksort_from_class(worst_case_array.copy(), start, end))
            quick_non_random_worst_runtime = quick_non_random_worst_timer.timeit(number=3)
            self.quicksort_class_worst_runtime_data.append(quick_non_random_worst_runtime)

            quick_random_worst_timer = timeit.Timer(
                lambda: QuicksortVariants.quicksort_class_random(worst_case_array.copy(), start, end))
            quick_random_worst_runtime = quick_random_worst_timer.timeit(number=3)
            self.quicksort_random_worst_runtime_data.append(quick_random_worst_runtime)



    def make_average_graph(self,create=True):


        if create:
            plt.hist(self.quicksort_class_runtime_data, bins=150,edgecolor='black', alpha=0.4, density=True)
            sns.kdeplot(self.quicksort_class_runtime_data, color='blue', linewidth=2, alpha=0.6)
            plt.hist(self.quicksort_random_runtime_data, bins=150,edgecolor='black', alpha=0.4, density=True)
            sns.kdeplot(self.quicksort_random_runtime_data, color='red', linewidth=2, alpha=0.6)
            plt.xlabel('Runtime in seconds')
            plt.ylabel('Count')
            plt.title('Distribution of Average-case Execution Time for Quicksort')
            plt.show()


    def make_worst_graph(self,create=True):


        if create:
            plt.hist(self.quicksort_class_worst_runtime_data, bins=300,edgecolor='black', alpha=0.4, density=True)
            sns.kdeplot(self.quicksort_class_worst_runtime_data, color='blue', linewidth=2, alpha=0.6)
            plt.hist(self.quicksort_random_worst_runtime_data, bins=300,edgecolor='black', alpha=0.4, density=True)
            sns.kdeplot(self.quicksort_random_worst_runtime_data, color='red', linewidth=2, alpha=0.6)
            plt.xlabel('Runtime in seconds')
            plt.ylabel('Count')
            plt.title('Distribution of Worst-case Execution Time for Quicksort')
            plt.show()


    def increasing_n_time_runs(self):

        testing_array = []
        for x in range(1, self.n):
            testing_array.insert(0, x)
            start, end = 0, len(testing_array) - 1

            quick_timer = timeit.Timer(lambda: QuicksortVariants.quicksort_from_class(testing_array.copy(), start, end))
            quick_runtime = quick_timer.timeit(number=3)
            self.quicksort_class_runtime_increasing_n_data.append(quick_runtime)

            random_timer = timeit.Timer(lambda: QuicksortVariants.quicksort_class_random(testing_array.copy(), start, end))
            random_runtime = random_timer.timeit(number=3)
            self.quicksort_random_runtime_increasing_n_data.append(random_runtime)



    def make_increasing_n_graph(self,create=True):


        if create:
            x_values = list(range(1, self.n))
            plt.plot(x_values, self.quicksort_class_runtime_increasing_n_data, label='Normal Quicksort')

            plt.plot(x_values, self.quicksort_random_runtime_increasing_n_data, label='Randomized Quicksort')
            plt.xlabel('n')
            plt.ylabel('Seconds')
            plt.legend()
            plt.show()

if __name__ == "__main__":

    se = SortingEval(test_range = 8,n=1000)
    #se.time_runs()
    #se.make_average_graph()
    #se.make_worst_graph()
    se.increasing_n_time_runs()
    se.make_increasing_n_graph()

