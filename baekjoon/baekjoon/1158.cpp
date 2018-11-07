#include <iostream>
#include <queue>

using namespace std;

int main() {
	int n, m, tmp;
	queue<int> q;

	cin >> n >> m;

	for (int i = 1; i <= n; i++)
		q.push(i);
	
	cout << "<";
	while (!q.empty()) {
		for (int i = 1; i < m; i++) {
			tmp = q.front();
			q.pop();
			q.push(tmp);
		}
		cout << q.front();
		if (q.size() > 1)
			cout << ", ";
		q.pop();
	}
	cout << ">" << endl;

	return 0;
}