#include <iostream>

using namespace std;

class Calculator{
    public:
    // 첫번째 방법
    /* 
    int add(int a, int b){
        return a + b;
    }*/
    
    int add(int a, int b);
};

// 두번째 방법
int Calculator::add(int a, int b){
    return a + b;
}

int main(){

    Calculator cal;
    cout << cal.add(3,4) << endl; // 해당 방법이 인라인방법
    return 0;
}