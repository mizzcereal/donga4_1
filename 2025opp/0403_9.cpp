#include <iostream>

using namespace std;

int main(){

    int n, fact = 1;

    cout << "�� ���丮�� ? ==> ";
    cin >> n;
    for(int i = 1; i <= n; i++){
        fact *= i;
    }
    cout << n << "!�� " <<  fact << "�Դϴ�." << endl;
}