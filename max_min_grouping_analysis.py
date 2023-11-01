import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import timeit
import pandas as pd
from max_min_grouping import min_max_grouping


class MaxMinGroupingEval():
    '''

    '''

    def __init__(self, n_iterations = 100):
        self.mix_max_grouping_runtime_data = []
        self.n_iterations = n_iterations + 1



    def time_runs(self):
        self.M = 3
        A = []
        for i in range(self.n_iterations):
            for i in range(self.M):
                random_integer = random.randint(4, 20)
                A.append(random_integer)
            timer = timeit.Timer(lambda: min_max_grouping(A, len(A), self.M))
            runtime = timer.timeit(number=3)
            self.mix_max_grouping_runtime_data.append([len(A),runtime])

        print(self.mix_max_grouping_runtime_data)

    def make_increasing_n_graph(self, create=True):
        M = 3
        if create:
            x_values = [self.mix_max_grouping_runtime_data[i][0] for i in range(len(self.mix_max_grouping_runtime_data))]
            x_nm_values = [self.mix_max_grouping_runtime_data[i][0] * M for i in range(len(self.mix_max_grouping_runtime_data))]
            x_nmmult_values = [self.mix_max_grouping_runtime_data[i][0] * 200 * M for i in range(len(self.mix_max_grouping_runtime_data))]
            x_nsquared_values = [self.mix_max_grouping_runtime_data[i][0] ** 2 for i in range(len(self.mix_max_grouping_runtime_data))]
            y_values = [self.mix_max_grouping_runtime_data[i][1] for i in range(len(self.mix_max_grouping_runtime_data))]
            plt.plot(x_values, y_values, label='MinMaxGrouping (M = 3) x=n')
            plt.plot(x_nm_values, y_values, label='MinMaxGrouping (M = 3) x=n*m')
            plt.plot(x_nmmult_values, y_values, label='MinMaxGrouping (M = 3) x=n*200m')
            plt.plot(x_nsquared_values, y_values, label='MinMaxGrouping (M = 3) x=n**2')
            plt.xlabel('adjusted n')
            plt.ylabel('Seconds')
            plt.legend()
            plt.show()


if __name__ == "__main__":
    eval = MaxMinGroupingEval()
    eval.time_runs()
    eval.make_increasing_n_graph()