#include <iostream>

using namespace std;

int main(){

    double n, sum = 0.0;
    do
    {
        cout << "실수 입력 : ";
        cin >> n;
        sum += n;
    } while ( n > 0);

    sum -= n; // 마지막으로 입력한게 음수일경우 이를 없애줌
    cout << "합 = " << sum;

    return 0;
    
}