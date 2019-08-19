#include <cstdio>

using namespace std;

int a[1001];
bool c[1001];

void dfs(int x) {
    if(c[x]) return;
    c[x] = true;
    dfs(a[x]);
}
void dfs2(int x) {
    while(c[x] == false) {
        c[x] = true;
        x = a[x];
    }
}

int main() {
    int t;
    scanf("%d\n", &t);
        while(t--) {
            int n;
            scanf("%d", &n);
            int ans = 0;
            for(int i = 1; i <= n; i++) {
                if(c[i] == false) {
                    dfs(i);
                    ans += 1;
                }
        }
    }
    return 0;
}