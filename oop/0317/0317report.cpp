#include <iostream>

using namespace std;

int main(){

    unsigned int a;
    unsigned int hour;
    unsigned int min;
    unsigned int second;

    cout << "�� �Է�" << endl;
    cin >> a;

    hour = a / 3600;
    min = a % 3600 / 60;
    second = a % 3600 % 60;
    cout << hour << "�ð� " << min << "�� " << second << "���Դϴ�." << endl;
}