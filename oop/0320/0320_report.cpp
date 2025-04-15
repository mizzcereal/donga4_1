#include <iostream>
#include <cmath>

using namespace std;

int main(){

    long long n;
    int a, result;

    cout << "정수 입력 : ";
    cin >> n;
    cout << "자릿수 입력 : ";
    cin >> a;

    result = (int)(n / pow(10,a-1)) % 10;

    if((int)(n / pow(10, a-1)) != 0){
        cout << "오른쪽에서 시작해서 " << a << "번째 자리에 있는 숫자는 " << result;
    }else{
        cout << "자릿수 범위를 벗어났습니다.";    

    }


}