#include <iostream>
using namespace std;

int main(){
    double fd, cd;
    cout << "ȭ���µ� �Է� : ";
    cin >> fd;

    cd = (fd - 32) * 5 / 9;

    cout.precision(5);
    cout << fixed;
    cout << "�����µ��� " << cd << " �Դϴ�. " << endl;
}