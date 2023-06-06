#include <stdio.h>
#include <string.h>
int count_words(char str[])
{
    int count = 0, i;
    for (i = 0; str[i] != '\0'; i++)
    {
        if (str[i] == ' ' || str[i] == '\n' || str[i] == '\t')
        {
            count++;
        }
    }
    return count + 1;
}
int main()
{
    char str[100];
    printf("Enter a string: ");
    fgets(str, 100, stdin);
    printf("Number of words: %d\n", count_words(str));
    return 0;
}