#include <iostream>
#include <stack>

using namespace std;

int main() {
	int answer = 0;
	char c[100001];
	stack<int> s;
	cin >> c;
	for (int i = 0; c[i] != '\0'; i++) {
		if (c[i] == '(')
			s.push(i);
		else if (c[i] == ')') {
			if (i == s.top() + 1) {
				s.pop();
				answer += s.size();
			}
			else {
				s.pop();
				answer += 1;
			}
		}
	}
	cout << answer << endl;

	return 0;
}