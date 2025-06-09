#include <iostream>

using namespace std;

template <typename T>
double sum(T a, T b, T c = 0){
    return a+b+c;
}

 int main(){

    cout << "두 정수의 합은 " << sum(10,20) << endl;
    cout << "세 실수의 합은" << sum(1.1,2.2,4.4) << endl;
 }