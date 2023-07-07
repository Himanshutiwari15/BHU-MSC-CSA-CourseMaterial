// Write a program to add two variables x and y using call by reference.

#include <iostream>
using namespace std;

void add(int &a, int &b)
{
    a += b; // Add the value of b to a
}

int main()
{
    int x = 5;
    int y = 3;

    cout << "Before addition: x = " << x << ", y = " << y << endl;

    add(x, y); // Pass x and y by reference to the add() function

    cout << "After addition: x = " << x << ", y = " << y << endl;

    return 0;
}
