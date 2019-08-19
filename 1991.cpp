#include <iostream>
using namespace std;
int node[50][2];

void preorder(int x) {
    if(x == -1) return;
    printf("%c", x + 'A');
    preorder(node[x][0]);
    preorder(node[x][1]);
}

void inorder(int x) {
    if(x == -1) return;
    inorder(node[x][0]);
    printf("%c", x + 'A');
    inorder(node[x][1]);
}

void postorder(int x) {
    if(x == -1) return;
    postorder(node[x][0]);
    postorder(node[x][1]);
    printf("%c", x + 'A');
}

int main() {
    int n;
    cin >> n;
    for(int i = 0; i < n; i++) {
        char x, y, z;
        cin >> x >> y >> z;
        x = x - 'A';
        if(y == '.') {
            node[x][0] = -1;
        } else {
            node[x][0] = y - 'A'; 
        }
        if(z == '.') {
            node[x][1] = -1;
        } else {
            node[x][1] = z - 'A';
        }
    }
    preorder(0);
    printf("\n");
    inorder(0);
    printf("\n");
    postorder(0);
    printf("\n");
    return 0;
}