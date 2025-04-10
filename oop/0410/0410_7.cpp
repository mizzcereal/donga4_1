#include <iostream>

using namespace std;

long long mypow(int a, int b);

int main(){
    int a, b;
    cout << "a와 b를 입력 : " ;
    cin >>  a >> b;
    cout << a <<"의" << b << "승은" << mypow(a,b) << endl; 
}

long long mypow(int a, int b){
    int result = 1;
    for (int i = 1; i <= b; i++){
        result *= a;
    }
    return result;
}