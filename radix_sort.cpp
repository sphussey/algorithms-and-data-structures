#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> counting_sort(vector<int> A, int d) {
    // k is always equal to 10 for counting sort
    const int k = 10;
    
    // create vectors B and C 
    vector<int> B(A.size(), 0);
    vector<int> C(k, 0);

    // assign C indices the count of each number 
    for (int j = 0; j < A.size(); j++) {
        int digit = (A[j] / d) % 10;
        C[digit]++;
    }
    
    for (int i = 1; i < k; i++) {
        C[i] += C[i - 1];
    }

    // output counts in C to B
    for (int j = A.size() - 1; j >= 0; j--) {
        int digit = (A[j] / d) % 10;
        B[C[digit] - 1] = A[j];
        C[digit]--;
    }

    // return the sorted array B
    return B;
}

vector<int> radix_sort(vector<int> A) {
    // find the max element to determine the number of digits
    vector<int>::iterator maxElementIterator = max_element(A.begin(), A.end());
    int maxElement = *maxElementIterator;
    
    // Perform counting sort for each digit position
    for (int d = 1; maxElement / d > 0; d *= 10) {
        A = counting_sort(A, d);
    }
    
    return A;
}

int main() {
    // Define the input vector
    vector<int> A =  {329, 457, 657, 839, 436, 720, 353};

    // Call radix sort on A
    vector<int> sortedArray = radix_sort(A);

    // Print out the sorted array
    for (int i = 0; i < sortedArray.size(); i++) {
        cout << sortedArray[i] << " ";
    }
    cout << "\n";

    return 0;
}
