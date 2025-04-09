#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main(){

    // 양의 정수 입력 ex 12345 % 10
    // 자릿수 입력 : 2
    // 출력 2번째 자릿수에 있는 정수는 4입니다.

    int a;
    int n;

    cout << "양의 정수 입력 : ";
    cin >> a;
    cout << "자릿 수 입력 : ";
    cin >> n;
    cout << (a /static_cast<int>(pow(10,n -1))) % 10;
    return 0;
}