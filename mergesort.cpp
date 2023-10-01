#include<iostream>
#include<vector>
#include<cmath>
using namespace std;




void merge(vector<int>& arr, int start, int midpoint, int end) {
    int n1 = (midpoint - start) + 1; // index of last element in the first half.
    int n2 = (end - midpoint); // 

    vector<int> left(n1, 0);
    vector<int> right(n2, 0);

    for (int i = 0; i < n1; i++) {
        left[i] = arr[start + i];
    }
    for (int j = 0; j < n2; j++) {
        right[j] = arr[midpoint + j + 1];
    }
    int i = 0;
    int j = 0;
    for (int k = start; k <= end; k++) {
        bool condition1 = i < n1;
        bool condition2 = (j >= n2) | (left[i] <= right[j]);
        if (condition1 & condition2) {
            arr[k] = left[i];
            i++;
        }
        else {
            arr[k] = right[j];
            j++;
        }

    }


}


void mergesort(vector<int>& arr, int start, int end) {
    bool end_greaterthan_start = start < end;
    if (end_greaterthan_start) {
        int midpoint = floor((start + end) / 2);
        mergesort(arr, start, midpoint);
        mergesort(arr, (midpoint + 1), end);
        merge(arr, start, midpoint, end);
    }
}


int main() {
    // your code goes here
    vector<int> arr = {7,3,9,5,3,8,4,1};
    mergesort(arr , 0, arr.size()-1 );
    for (int x = 0; x < arr.size(); x++) {
        cout << " "<< arr[x];
    }
    cout << "\n";
    return 0;
    
}