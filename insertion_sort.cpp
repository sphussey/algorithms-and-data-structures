#include<iostream>
#include<vector>

void insertion_sort(std::vector<double>& arr) {
    for (int j = 1; j < arr.size(); j++) {
        double key = arr[j];
        int i = j - 1;
        while (i >= 0 && arr[i] > key) {
            arr[i + 1] = arr[i];
            i = i - 1;
        }
        arr[i + 1] = key;
    }
}

int main() {
    std::vector<double> arr = {7.0, 6.0, 5.0, 3.0, 2.0, 1.0};
    std::cout << "starting array: ";
    for (const double& element : arr) {
        std::cout << element << ' ';
    }
    std::cout << "\n";
    insertion_sort(arr);
    std::cout << "sorted array:";
    for (const double& element : arr) {
        std::cout << element << ' ';
    }
    std::cout << '\n';

    return 0;
}