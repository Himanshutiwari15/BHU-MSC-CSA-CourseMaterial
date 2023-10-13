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

void printAltRecursive(Node* head) {
   if (head == NULL)
     return;
     
   cout << head->data << " ";
   
   if (head->next != NULL) {
      printAltRecursive(head->next->next);
   }
}

void printAlt(Node* head) {

  while (head != NULL) {
    
    if (head == NULL)
      return;
      
    cout << head->data << " ";
      
    head = head->next;
  
    if (head != NULL)
       head = head->next;
  }
}

int main() {

  Node* head = NULL;
  
  int arr[] = {11, 16, 18, 10, 9, 2, 11, 19, 10, 15, 16, 17, 18, 14, 15, 13};

  for(int i=0; i<16; i++) {
    insert(&head, arr[i]);
  }

  printAltRecursive(head);
  cout<<endl;
  printAlt(head);

  return 0; 
}