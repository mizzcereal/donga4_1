#include <iostream>
#include <cmath>

using namespace std;

int main(){

    int n, sum1, sum2, sum3;

    cout << "n �Է� :";
    cin >> n;

    int i = 1;
    while(i <= n){
        sum1 += i;
        sum2 += i * i;
        sum3 += i * i * i;
        i++;
    }

    cout << "sum1�� ���� :" << sum1 << endl;
    cout << "sum2�� ���� :" << sum2 << endl;
    cout << "sum3�� ���� :" << sum3 << endl;


    return 0;
}