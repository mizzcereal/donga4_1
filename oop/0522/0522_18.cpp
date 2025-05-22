#include <iostream>

using namespace std;

class Example{
    static int val;
    public:
        void show(){
            cout << val << endl;
        }
};

int Example::val = 0;

int main(){
    Example e;
    e.show();
    return 0;
}
