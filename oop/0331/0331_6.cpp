#include <iostream>
#include <cmath>

using namespace std;

int main(){

    int n, sum1, sum2, sum3;

    cout << "n �Է� :";
    cin >> n;

    for(int i = 1; i<=n; i++){
        sum1 += i;
        sum2 += pow(i,2);
        sum3 += pow(i,3);
    }

    cout << "sum1�� ���� :" << sum1 << endl;
    cout << "sum2�� ���� :" << sum2 << endl;
    cout << "sum3�� ���� :" << sum3 << endl;


    return 0;
}