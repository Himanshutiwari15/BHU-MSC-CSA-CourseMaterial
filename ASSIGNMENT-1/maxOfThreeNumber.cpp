// write a c++ program to find the maximum number between three number, the variables are x,y and z.

#include <iostream>
using namespace std;

int maxFinder(int a, int b, int c)
{
    if (a >= b && a >= c)
    {
        // returning the maximum value
        return a;
    }
    else
    {
        /*if condition is false then it means that either of two values are greater than or equal to*/
        /*the third one. So we will compare them and find out which one has more number.*/
        if ((b - a) > (c - a))
        {
            return b; // returning second largest element as per given conditions in problem statement
        }
        else
        {
            return c;
        }
    }
}

int main()
{
    int x, y, z;
    cout << "Enter three numbers: ";
    cin >> x >> y >> z;
    int result = maxFinder(x, y, z);
    cout << "\nThe Maximum Number among Three Numbers Entered Is : "<<result<<endl;

    return 0;
}