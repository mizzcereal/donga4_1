#include <iostream>
#include <cmath>

using namespace std;

int main(){

    int n, sum1, sum2, sum3;

    cout << "n 입력 :";
    cin >> n;

    for(int i = 1; i<=n; i++){
        sum1 += i;
        sum2 += pow(i,2);
        sum3 += pow(i,3);
    }

    cout << "sum1의 값은 :" << sum1 << endl;
    cout << "sum2의 값은 :" << sum2 << endl;
    cout << "sum3의 값은 :" << sum3 << endl;


    return 0;
}