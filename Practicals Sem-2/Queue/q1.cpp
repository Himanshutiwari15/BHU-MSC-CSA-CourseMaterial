#include <iostream>
using namespace std;

class Queue
{
private:
    int *data;
    int front;
    int rear;
    int capacity;

public:
    Queue(int size)
    {
        data = new int[size];
        capacity = size;
        front = 0;
        rear = -1;
    }

    void enqueue(int x)
    {
        if (rear == capacity - 1)
        {
            std::cout << "Queue is Full" << std::endl;
            return;
        }
        rear++;
        data[rear] = x;
    }

    void dequeue()
    {
        if (front > rear)
        {
            std::cout << "Queue is Empty" << std::endl;
            return;
        }
        front++;
    }

    int frontp()
    {
        return data[front];
    }

    int rearp()
    {
        return data[rear];
    }
};

int main()
{
    Queue q(5);

    q.enqueue(1);
    q.enqueue(2);
    q.enqueue(3);

    q.dequeue();

    std::cout << q.frontp() << std::endl;
    std::cout << q.rearp() << std::endl;

    return 0;
}