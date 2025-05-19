#include <iostream>

using namespace std;

int sum(int a, int b){
    return a+b;
}

int sum(int a, int b, int c){
    return a+b+c;
}

int main(){

    cout <<sum(3,7) << endl;
    cout << sum(3,7,100) << endl;

    return 0;
}