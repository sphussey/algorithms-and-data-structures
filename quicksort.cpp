#include<iostream>
#include <cstdlib>
#include<vector>
#include<cmath>
using namespace std;


int partition(vector<int>& arr, int start, int end) {
    
    int pivot = arr[start];
    int i = start;
    for (int j = start + 1; j <= end ;j++){
        if (arr[j] <= pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[start], arr[i]);
    return i;
    }



void quicksort(vector<int>& arr, int start, int end) {
    if (start < end) {
        int midpoint = partition(arr, start, end);
        quicksort(arr, start, midpoint - 1);
        quicksort(arr, midpoint + 1, end);
    }
}


int random_partition(vector<int>& arr, int start, int end) {
    
    
    int p = rand() % (end + 1);
    cout << p << "\n";
    int pivot = arr[start];
    int i = start;
    for (int j = start + 1; j <= end ;j++){
        if (arr[j] <= pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[start], arr[i]);
    return i;
    }



void random_quicksort(vector<int>& arr, int start, int end) {
    if (start < end) {
        int midpoint = random_partition(arr, start, end);
        random_quicksort(arr, start, midpoint - 1);
        random_quicksort(arr, midpoint + 1, end);
    }
}



int main() {
    srand (time(0));
    vector<int> arr = {1,3,8,2,5,4,9,6};
    random_quicksort(arr ,0,arr.size() - 1);
    for (int x = 0; x < arr.size(); x++) {
        cout << " " << arr[x];
    }
    cout << "\n";
    return 0;
}