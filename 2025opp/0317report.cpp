#include <iostream>

using namespace std;

int main(){

    unsigned int a;
    unsigned int hour;
    unsigned int min;
    unsigned int second;

    cout << "초 입력" << endl;
    cin >> a;

    hour = a / 3600;
    min = a % 3600 / 60;
    second = a % 3600 % 60;
    cout << hour << "시간 " << min << "분 " << second << "초입니다." << endl;
}