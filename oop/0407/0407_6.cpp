#include <iostream>

using namespace std;

long long mypow(int a, int b){
    long long result = 1;
    for(int i =0; i < b; i++){
        result *= a;
    }
    return result;
}

int main(){
    int a,b;
    cout << "a�� b�� �Է��ϼ���";
    cin >> a >> b;
    cout << a <<  "�� " << b << "���� " << mypow(a,b) << endl; 
}