// Write a program to find the size of different pointer types in C++

#include <iostream>
using namespace std;

int main()
{
    cout << "Size of char: " << sizeof(char) << endl;                            // size of character is
    cout << "Size of short:" << sizeof(short) << endl;                           // size of short
    cout << "Size of long :" << sizeof(long) << endl;                            // size of long
    cout << "Size of float :" << sizeof(float) << endl;                          // size of float
    cout << "Size of double : " << sizeof(double) << endl;                       // size of
    cout << "Size of void* : " << sizeof(void *) << endl;                        // size
    cout << "Size of Integer Pointer : " << sizeof(int *) << endl;               // pointer
    cout << "Size of Char Pointer : " << sizeof(char *) << endl;                 // char
    cout << "Size of Double Pointer : " << sizeof(double *) << " bytes" << endl; // pointer

    return 0;
}
