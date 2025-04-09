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
    cout << "a와 b를 입력하세요";
    cin >> a >> b;
    cout << a <<  "의 " << b << "승은 " << mypow(a,b) << endl; 
}