#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool only_digits(string s);
char rotate(char c, int k);

int main(int argc, string argv[])
{
    if (argc < 2 || argc > 2 || !only_digits(argv[1]))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    int key = atoi(argv[1]);

    string ptext = get_string("plaintext: ");

    printf("ciphertext: ");

    for (int i = 0; ptext[i] != '\0'; i++)
    {
        printf("%c", rotate(ptext[i], key));
    }
    printf("\n");
}

bool only_digits(string s)
{
    for (int n = 0; s[n] != '\0'; n++)
    {
        if (!isdigit(s[n]))
        {
            return false;
        }
    }
    return true;
}

char rotate(char c, int k)
{
    if (!isalpha(c))
    {
        return c;
    }
    else if (isupper(c))
    {
        return ((((c - 65) + k) % 26) + 65);
    }
    else
    {
        return ((((c - 97) + k) % 26) + 97);
    }
}
