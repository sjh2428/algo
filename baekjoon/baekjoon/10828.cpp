//https://www.acmicpc.net/problem/10828
#include <iostream>

using namespace std;

class Stack {
private:
	int top = 0;
	int size;
	int *stack;

public:
	Stack(int size) {
		stack = new int[size];
		this->size = size;
	}

	void push(int data) {
		stack[top] = data;
		top++;
		cout << "push : " << data << endl;
	}

	void pop() {
		if (top == 0) {
			cout << "error! size is 0!" << endl;
			return;
		}
		cout << "pop : " << stack[top - 1] << endl;
		--top;
	}

	void getSize() {
		cout << "size : " << top << endl;
	}

	void isEmpty() {
		if (top == 0)
			cout << "Empty!" << endl;
		else
			cout << "Not Empty!" << endl;
	}

	void getTop() {
		if (top == 0)
			cout << "Empty stack!" << endl;
		else
			cout << "top : " << stack[top - 1] << endl;
	}
};

int main() {
	Stack s(100);
	s.push(20);
	s.push(30);
	s.push(40);
	s.getTop();
	s.isEmpty();
	s.pop();
	s.getSize();
	s.pop();
	s.pop();
	s.pop();

	return 0;
}