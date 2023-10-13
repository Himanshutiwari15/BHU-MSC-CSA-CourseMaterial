#include <iostream>
using namespace std;

class Stack
{
private:
    int arr[100];
    int top;

public:
    Stack(){
        top = -1;
    }

    void Push(int x){
        if (top == 99){
            cout<<"Stack Overflow"<<endl;
            return;
        }
        top += 1;
        arr[top] = x;
    }

    void Pop(){
        if( top == -1){
            cout<< "Underflow"<<endl;
            return;
        }
        cout <<arr [top-- ] <<" is popped from stack" << endl;
    }

    int Peek(){
        if ( top == -1){
            cout<<"Empty Stack"<<endl;
            return -1 ;
        }
        return arr[top ];

    }
};

int main(){
    Stack s;
    s.Push(1);
    s.Push(2);
    s.Push(3);
    cout<< "TOP"<<s.Peek()<<endl;
    s.Pop();
    cout<< "TOP"<<s.Peek()<<endl;
    return 0;


}