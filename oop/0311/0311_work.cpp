#include <iostream>

using namespace std;

int main(){
    const double pi = 3.141592;
    double a, b, h;

    cout << "�غ�(������)�� ����, ���̸� �Է��ϼ��� : ";
    cin >> a >> b >> h;
    cout << "�غ� " << a << "���� " << b << "���� " << h << "�� ��ٸ����� ���̴� " << (a+b)*h * 1/2 << "�Դϴ�." << endl;
    cout << "������ " << a << "�� ���� ���̴� " << a * a * pi << "�Դϴ�." << endl;
    cout << "������ " << a<< "���� " << h << "�� ������� ���Ǵ� " << a * a * h * pi << "�Դϴ�." << endl;

}