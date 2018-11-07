#include <iostream>

using namespace std;

class Node {
public:
	Node *prev;
	int data;
	Node *next;
};

class LinkedList {
private:
	Node *head;
	Node *curNode;
	int length;

public:
	LinkedList() {
		this->head = NULL;
		length = 0;
	}

	~LinkedList() {
		cout << "LinkedList deleted!" << endl;
	}

	void add(int data) {
		if (this->head == NULL) {
			this->head = new Node();
			this->head->prev = NULL;
			this->head->data = data;
			this->head->next = NULL;
			curNode = this->head;
		}
		else {
			Node *node = new Node();
			node->prev = curNode;
			node->data = data;
			node->next = NULL;
			curNode->next = node;
			curNode = node;
			length++;
		}
	}

	void print() {
		int i = 1;
		Node* node = this->head;
		while (node) {
			cout << i++ << " : " << node->data << endl;
			node = node->next;
		}
	}
};

int main() {
	LinkedList *lst = new LinkedList();
	lst->add(10);	lst->add(30);	lst->add(50);	lst->add(40);
	lst->print();
	delete lst;

	return 0;
}