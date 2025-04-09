#include <iostream>

using namespace std;

int main(){

    int a, b;
    cout << "두 수 입력 : " ;
    cin >> a >> b;

    cout << "큰 수는 " << (a > b ? a : b) << " 입니다." << endl;

    cout << b << "의 절댓값은 " << abs(b) << "입니다." << endl;

    cout << a << "는 짝수일까요 홀수일까요? ==> ";
    cout << ((a%2 == 0) ? "짝수" : "홀수");

    return 0;
}