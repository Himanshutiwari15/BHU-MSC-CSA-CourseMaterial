#include <iostream>
using namespace std;

class CircularQueue
{
    int *arr;
    int size;
    int front;
    int rear;

public:
    CircularQueue(int n)
    {
        size = n;
        arr = new int[size];
        front = -1;
        rear = -1;
    }

    void enqueue(int data)
    {
        if ((front == 0 && rear == size - 1) || (rear == (front - 1) % (size - 1)))
        {
            cout << "Queue is Full" << endl;
            return;
        }
        else if (front == -1)
        { // first element
            front = rear = 0;
        }
        else if (rear == size - 1 && front != 0)
        {
            rear = 0;
        }
        else
        {
            rear++;
        }
        arr[rear] = data;
    }

    void dequeue()
    {
        if (front == -1)
        {
            cout << "Queue is Empty" << endl;
            return;
        }
        cout << "Dequeued element: " << arr[front] << endl;

        if (front == rear)
        {
            front = rear = -1;
        }
        else if (front == size - 1)
        {
            front = 0;
        }
        else
        {
            front++;
        }
    }
};

int main()
{

    CircularQueue q(5);

    q.enqueue(14);
    q.enqueue(22);
    q.enqueue(13);
    q.enqueue(-6);

    q.dequeue();

    q.enqueue(9);
    q.enqueue(20);
    q.enqueue(5);

    q.dequeue();

    return 0;
}