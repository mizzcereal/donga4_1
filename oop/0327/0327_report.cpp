#include <iostream>
#include <iomanip>

using namespace std;

int main(){

    double num, fd, cd;

    cout << "�����ϼ��� (1:ȭ��->����, 2:����->ȭ��)";
    cin >> num;
    if(num == 1){
        cout << "ȭ���µ� �Է� : ";
        cin  >> fd;
        cd = (fd-32) * 5 / 9; 
        cout << fixed << showpoint << setprecision(5);
        cout << "�����µ��� " << cd << "�Դϴ�.";
    }else if(num == 2){
        cout << "�����µ� �Է� : ";
        cin >> cd;
        fd = (cd * 9 / 5) + 32;
        cout << fixed << showpoint << setprecision(5);
        cout << "ȭ���µ��� " << fd << "�Դϴ�.";   
    }else{
        cout << "1, 2�߿� �ϳ��� �Է��ϼ���.";
    }
}