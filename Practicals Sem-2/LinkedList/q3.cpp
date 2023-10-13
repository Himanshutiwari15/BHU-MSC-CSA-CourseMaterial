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

void printMiddle(Node* head) {
  Node* slow = head;
  Node* fast = head;

  while (fast != NULL && fast->next != NULL) {
    fast = fast->next->next;
    slow = slow->next;
  }

  cout << "The middle element is: " << slow->data << endl;
}

int main() {

  Node* head = NULL;
  
  int arr[] = {0, 9, 5, 6, 7, 1, 0, 1, 9};

  for(int i=0; i<9; i++) {
    insert(&head, arr[i]);
  }

  printMiddle(head);

  return 0;
}