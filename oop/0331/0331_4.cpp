#include <iostream>

using namespace std;

int main(){

    int number;
    cout << "���� �Է�: ";
    cin >> number;

    cout << number << "������ �ڿ��� �� 3 Ȥ�� 5�� �����" << endl;
    cout << "-----------------------------------" << endl;

    int i = 1;
    int count = 0;
    while(i <= number){
        if(i %3 == 0 || i % 5 ==0){
            cout << i << endl;
            count++;
        }
    i++;
    }

    cout << "-----------------------------------" << endl;
    cout << "�� " << count << "�� �Դϴ�. " << endl;

    return 0;
}