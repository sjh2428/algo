#include <cstdio>
using namespace std;
int check[1000000];
//check[i] = 0 -> 아직 방문 x
//check[i] != 0 -> 방문했고, 몇번째 방문인지
int pow(int x, int p) {
    int ans = 1;
    for(int i = 0; i < p; i++) {
        ans = ans * x;
    }
    return ans;
}

int next(int a, int p) {
    int ans = 0;
    while(a > 0) {
        ans += pow(a%10, p);
        a /= 10;
    }
    return ans;
}

int length(int a, int p, int cnt) {
    if(check[a] != 0) {
        return check[a]-1;
    }
    check[a] = cnt;
    int b = next(a, p);
    return length(b, p, cnt+1);
}

int main() {
    int a, p;
    scanf("%d %d", &a, &p);
    printf("%d\n", length(a, p, 1));
    return 0;
}