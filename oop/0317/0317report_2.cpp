#include <iostream>

using namespace std;

int main(){

    unsigned int hour;
    unsigned int min;
    unsigned int second;
    unsigned int time;

    cout << "시 분 초를 입력하세요" << endl;
    cin >> hour >> min >> second;

    time = (hour * 3600) + (min * 60) + second;

    cout << "총 " << time << "초입니다.";

    return 0;
}