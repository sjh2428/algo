#include <cstdio>
#include <cstring>

using namespace std;

int main() {
    char c[101], *token;
    gets(c);
    printf("%s\n", c);
    token = strtok(c, " ");
    while(token != NULL) {
        printf("%s\n", token);
        token = strtok(NULL, " ");
    }

    return 0;
}