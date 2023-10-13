#include <iostream>
using namespace std;

int main() {
    int arr[] = {5, 10, 15, 20, 25};
    int sum = 0;

    // Calculate the sum of elements in the array
    for (int i = 0; i < sizeof(arr) / sizeof(arr[0]); i++) {
        sum += arr[i];
    }

    cout << "The sum of elements in the array is: " << sum << endl;

    return 0;
}
