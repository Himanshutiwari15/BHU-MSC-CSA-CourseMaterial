#include <iostream>
#include <climits>

using namespace std;

int main() {
  int arr[] = {100,96,47,35,29,33,99,87,74,63,99,63};
  int n = sizeof(arr) / sizeof(arr[0]);
  
  int max = INT_MIN; 
  int min = INT_MAX;
  
  for(int i=0; i<n; i++) {
    if(arr[i] > max)
      max = arr[i];
    if(arr[i] < min)  
      min = arr[i];
  }

  cout << "Maximum element is " << max << endl;
  cout << "Minimum element is " << min;
  
  return 0;
}