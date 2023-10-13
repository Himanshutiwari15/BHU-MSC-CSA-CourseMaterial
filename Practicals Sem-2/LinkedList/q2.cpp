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

void countElements(Node* head) {
    Node* current = head;

    while (current != NULL) {
        int count = 0;
        Node* temp = head; // Start from the head each time

        while (temp != NULL) {
            if (temp->data == current->data) {
                count++;
            }
            temp = temp->next;
        }

        // Print the count for the current data if not already printed
        Node* checkPrinted = head;
        bool alreadyPrinted = false;
        while (checkPrinted != current) {
            if (checkPrinted->data == current->data) {
                alreadyPrinted = true;
                break;
            }
            checkPrinted = checkPrinted->next;
        }
        if (!alreadyPrinted) {
            cout << current->data << " - " << count << endl;
        }

        current = current->next;
    }
}

int main() {
    Node* head = NULL;

    int arr[] = {0, 13, 12, 46, 28, 19, 19, 0, 1, 2, 8, 6, 
                 6, 8, 2, 5, 3, 2, 5, 6, 9};

    for (int i = 0; i < 21; i++) {
        insert(&head, arr[i]);
    }

    printList(head);

    countElements(head);

    return 0;
}
