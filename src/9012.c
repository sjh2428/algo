#include <stdio.h>

int main() {
    int i, j, t, cnt;
    char a[51] = "\0";
    scanf("%d", &t);
    for(i = 0; i < t; i++) {
        cnt = 0;
        scanf(" %s", a);
        for(j = 0; a[j] != '\0'; j++) {
            if(a[j] == '(') {cnt++;}
            else if(a[j] == ')') {cnt--;}
            if(cnt < 0) {break;}
        }
        if(cnt == 0) {printf("YES\n");}
        else {printf("NO\n");}
    }
    return 0;
}