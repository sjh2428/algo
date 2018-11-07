#include <iostream>
#include <stack>

using namespace std;

int main() {
	stack<char> c1, c2;
	char str[100001], cmd, arg;
	int n;
	cin >> str;
	for (int j = 0; str[j] != '\0'; j++)
		c1.push(str[j]);
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> cmd;
		if (cmd == 'L') {
			if (!c1.empty()) {
				c2.push(c1.top());
				c1.pop();
			}
		}
		else if (cmd == 'D') {
			if (!c2.empty()) {
				c1.push(c2.top());
				c2.pop();
			}
		}
		else if (cmd == 'B') {
			if (!c1.empty())
				c1.pop();
		}
		else if (cmd == 'P') {
			cin >> arg;
			c1.push(arg);
		}
	}
	while (!c1.empty()) {
		c2.push(c1.top());
		c1.pop();
	}
	while (!c2.empty()) {
		cout << c2.top();
		c2.pop();
	}

	return 0;
}