#include <iostream>
#include <cmath>

using namespace std;

int main(){

    long long n;
    int a, result;

    cout << "���� �Է� : ";
    cin >> n;
    cout << "�ڸ��� �Է� : ";
    cin >> a;

    result = (int)(n / pow(10,a-1)) % 10;

    if((int)(n / pow(10, a-1)) != 0){
        cout << "�����ʿ��� �����ؼ� " << a << "��° �ڸ��� �ִ� ���ڴ� " << result;
    }else{
        cout << "�ڸ��� ������ ������ϴ�.";    

    }


}