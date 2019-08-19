#include <cstdio>
#include <vector>

using namespace std;

vector<int> a[20001];
int color[20001];
void dfs(int node, int c) {
    color[node] = c;
    for(int i = 0; i < a[node][i]; i++) {
        int next = a[node][i];
        if(color[next] == 0) {
            dfs(next, 3-c);
            /*3-c가 되는 이유는
            0 - no visited
            1 - visited, color : red
            2 - visited, color : blue
            c + ? = 3
            ? = 3 - c
            */
        }
    }
}

bool dfs2(int node, int c) {
    color[node] = c;
    for(int i = 0; i < a[node].size(); i++) {
        int next = a[node][i];
        if(color[next] == 0) {
            if(dfs2(next, 3-c) == false) {
                return false;
            }
        } else if(color[next] == color[node]) {
            return false;
        }
    }
    return true;
}

int main() {
    int t;
    scanf("%d\n", &t);
    while(t--) {
        int n, m;
        scanf("%d %d", &n, &m);
        for(int i = 1; i <= n; i++) {
            a[i].clear();
            color[i] = 0;
        }
        for(int i = 0; i < m; i++) {
            int u, v;
            scanf("%d %d", &u, &v);
            a[u].push_back(v);
            a[v].push_back(u);
        }
        for(int i = 1; i <= n; i++) {
            if(color[i] == 0) {
                dfs(i, 1);
            }
        }
        bool ok = true;
        //dfs2를 이용하면 아래의 과정이 필요없게됨
        for(int i = 1; i <= n; i++) {
            for(int k = 0; k < a[i].size(); k++) {
                int j = a[i][k];
                if(color[i] == color[j]) {
                    ok = false;
                }
            }
        }
        printf("%s\n", ok ? "YES" : "NO");
    }
    return 0;
}