#include <iostream>
using namespace std;

struct Node
{
    int data;
    Node *next;
};

void printList(Node *head)
{
    if (head == NULL)
    {
        return;
    }

    cout << head->data << " ";

    printList(head->next);
}

void insert(Node **head_ref, int new_data)
{
    Node *new_node = new Node();
    new_node->data = new_data;
    new_node->next = (*head_ref);
    (*head_ref) = new_node;
}

int main()
{

    Node *head = NULL;

    insert(&head, 1);
    insert(&head, 2);
    insert(&head, 3);
    insert(&head, 4);

    printList(head);

    return 0;
}