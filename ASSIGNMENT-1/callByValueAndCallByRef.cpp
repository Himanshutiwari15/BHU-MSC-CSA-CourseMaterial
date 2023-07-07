// C++ program to illustrate simple call by value and call by reference

#include <iostream>
using namespace std;
/* Function definition for addition using Call By Value Method. Here we pass two integers */

void add(int a, int b)
{
    a += b;
}

/* Function definition for addition using Call By Reference Method. Here we pass two integers */

void addRef(int *p_num1, int *p_num2)
{
    (*p_num1) += (*p_num2);
}

int main()
{
    // call by value
    int num = 50;
    cout << "Before calling the function: " << num << endl;
    add(num, 30);
    cout << "After Calling The Addition Using CallByValue :" << num << endl;
    // Call by Refrence Example
    int x = 789465;
    int y = -1234;
    printf("Before adding values of %d , %d\n",x ,y );
    addRef(&x,&y);   /* Passing address as arguments*/
    printf("\n After Adding Values %d , %d",x,y);
    return 0;
}
