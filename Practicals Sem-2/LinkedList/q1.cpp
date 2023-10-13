#include <iostream>

using namespace std;

struct Node {
    int data;
    Node* next;
};

void insert(Node** head_ref, int new_data) {
    Node* new_node = new Node();
    new_node->data = new_data;
    new_node->next = (*head_ref);
    (*head_ref) = new_node;
}

void printList(Node* node) {
    while (node != NULL) {
        cout << node->data << " ";
        node = node->next;
    }
    cout << endl;
}

Node* reverse(Node* head) {
    Node* prev = NULL;
    Node* current = head;
    Node* next = NULL;
    while (current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    return prev;
}

int main() {
    Node* head = NULL;
    for (int i = 7; i <= 17; i++)
        insert(&head, i);

    cout << "Original Linked list: " << endl;
    printList(head);

    head = reverse(head);

    cout << "Reversed Linked list: " << endl;
    printList(head);

    return 0;
}
