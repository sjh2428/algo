#include <iostream>
#include <queue>
#include <vector>

using namespace std;

vector<int> a[100001];
bool check[100001];
int parent[100001];

int main() {
    int n;
    cin >> n;
    for(int i = 2; i <= n; i++) {
        int u, v;
        cin >> u >> v;
        a[u].push_back(v);
        a[v].push_back(u);
    }
    parent[1] = 0;
    check[1] = true;
    queue<int> q;
    q.push(1);
    while(!q.empty()) {
        int x = q.front();
        q.pop();
        for(int i = 0; i < a[x].size(); i++) {
            int y = a[x][i];
            if(check[y] == false) {
                check[y] = true;
                parent[y] = x;
                q.push(y);
            }
        }
    }
    for(int i = 2; i <= n; i++) {
        printf("%d\n", parent[i]);
    }

    return 0;
}