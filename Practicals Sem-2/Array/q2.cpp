#include <iostream>
using namespace std;

int main() {
  int arr[] = {1,0,6,6,4,3,2,9,8,5,7,8,9,3,6,3,3,5,4,0,9,9,0,1,2,6};
  int freq[10] = {0};
  
  for(int i=0; i<26; i++) {
    freq[arr[i]]++; 
  }
  
  for(int i=0; i<10; i++) {
    if(freq[i] != 0) {
      cout << i << " occurs " << freq[i] << " times" << endl; 
    }
  }

  return 0;
}