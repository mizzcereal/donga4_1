#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main(){

    // ���� ���� �Է� ex 12345 % 10
    // �ڸ��� �Է� : 2
    // ��� 2��° �ڸ����� �ִ� ������ 4�Դϴ�.

    int a;
    int n;

    cout << "���� ���� �Է� : ";
    cin >> a;
    cout << "�ڸ� �� �Է� : ";
    cin >> n;
    cout << (a /static_cast<int>(pow(10,n -1))) % 10;
    return 0;
}