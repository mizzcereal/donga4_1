#include <iostream>

using namespace std;

int main(){

    unsigned int hour;
    unsigned int min;
    unsigned int second;
    unsigned int time;

    cout << "�� �� �ʸ� �Է��ϼ���" << endl;
    cin >> hour >> min >> second;

    time = (hour * 3600) + (min * 60) + second;

    cout << "�� " << time << "���Դϴ�.";

    return 0;
}