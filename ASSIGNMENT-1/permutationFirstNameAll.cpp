// WAP to show all the permutation of your first name using string function and using pointer with strings in C++.


#include<iostream>
#include <string>
using namespace std;

int COUNT = 1;
/*Function for swapping two characters*/
void swap(char* a, char* b) {
    char temp = *a;
    *a = *b;
    *b = temp;
}
// Function to print all permutations of string
void permutations(string& a, int l, int r)
{
	if (l == r)
		cout << a << endl;
	else {
		for (int i = l; i <= r; i++) {
			swap(a[l], a[i]);
			permutations(a, l + 1, r);
			swap(a[l], a[i]);
		}
	}
    ++COUNT;
}

int main()
{
	string str = "himanshu";
	int n = str.size();
	permutations(str, 0, n - 1);
    cout<<COUNT;
	return 0;
}
