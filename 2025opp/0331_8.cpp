#include <iostream>
#include <cmath>

using namespace std;

int main(){

    int n, sum1, sum2, sum3;

    cout << "n 입력 :";
    cin >> n;

    sum1 = n * (n+1) /2;
    sum2 = n * ((n+1) * (2 * n+1)) / 6;
    sum3 = (n*n) * ((n+1) * (n+1)) / 4;

    cout << "sum1의 값은 :" << sum1 << endl;
    cout << "sum2의 값은 :" << sum2 << endl;
    cout << "sum3의 값은 :" << sum3 << endl;


    return 0;
}