#include <iostream>

using namespace std;

int main(){

    int number;
    int count = 0;
    cout << "���� �Է�: ";
    cin >> number;

    cout << number << "������ �ڿ��� �� 3 Ȥ�� 5�� �����" << endl;
    cout << "-----------------------------------" << endl;

    for(int i = 1; i < number; i++){
        if(i % 3 ==0 || i % 5 == 0){
            cout << i << endl;
            count++;
        }
    }

    cout << "-----------------------------------" << endl;
    cout << "�� " << count << "�� �Դϴ�. " << endl;

    return 0;
}