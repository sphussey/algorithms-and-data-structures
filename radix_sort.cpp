#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;



vector<int> counting_sort (vector<int> A, int d) {
    // create Vector B of A.length()
    vector<int> B(A.size(), 0);

    // k will always be equal to 10 for counting sort
    const int k = 10;
    
    // let C be a new array of length k + 1 (for 0), with each element being a zero
    vector<int> C(10, 0);

    // Assign C indecies the count of the number 
    for (int j = 0; j < A.size(); j++) {
        C[A[j]] = C[A[j]] + 1;
    }
    
    for (int i = 1; i <= k; i++) {
        C[i] = C[i] + C[i - 1];
    }
    // output counts in C to B
    for (int j = A.size() - 1; j >= 0; j-- ) {
        B[C[A[j]] - 1] = A[j];
        C[A[j]] = C[A[j]] - 1;
    }

    // return our sorted array C
    return B;
}



vector<int> radix_sort(vector<int> A, int d) {
    for (i =0; i < d; i++) {

    }
}


int main() {
    // define our input vector
    vector<int> A = {999, 621, 877, 358, 534, 723, 423, 365, 443, 223, 153};

    // create an vector B with A.size() elements filled with 0s
    vector<int> B(A.size(), 0);

    // determine the highest number k for counting sort
    vector<int>::iterator maxElementIterator = max_element(A.begin(), A.end());
    int k = *maxElementIterator;
    cout << k << "\n";


    // call counting sort on A
    vector<int> C = counting_sort(A, B, k);

    // print out sorted array
    for (int i = 0; i < A.size(); i++) {
        cout << C[i] << " ";
    }
    cout << "\n";

    return 0;
}