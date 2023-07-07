// Write a C++ program to calculate the length of the string using pointer and concatenate by string function.

#include <iostream>
#include <string>
using namespace std;

int strLength(const char *str)
{
    int length = 0;
    while (*str != '\0')
    {
        length++;
        str++;
    }
    return length;
}

int main()
{
    const char *str = "Hello ";
    const char *name = "World";

    int length = strLength(str);
    cout << "Length of the string '" << str << "': " << length << endl;

    char result[50];
    strcpy(result, str);
    strcat(result, name);
    cout << "Concatenated string: " << result << endl;
    return 0;
}