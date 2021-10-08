#include <iostream>
#include <stack>

using namespace std;

int main() {
    stack<int> stack, stack_new;
    int size;
    stack.push(36);
    stack.push(35);
    stack.push(34);
    stack.push(33);
    size = stack.size();
    cout << "Original Stack" << endl;
    for (int i = 0; i < size; ++i) {
        cout << stack.top() << endl;
        if (i == size/2) {
            stack_new.push(32);
        }
        stack_new.push(stack.top());
        stack.pop();
    }
    size = stack_new.size();
    cout << "New Stack" << endl;
    for (int i = 0; i < size; ++i)
    {
        cout << stack_new.top() << endl;
        stack_new.pop();
    }
    return 0;
}
