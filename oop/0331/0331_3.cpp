#include <iostream>
#include <iomanip>

using namespace std;

int main(){

    int score, sum = 0;
    double average;

    for(int i = 0; i < 4; i++){
        cout << "점수 입력(0 ~ 100) :";
        cin >> score;
        sum += score;
    }
    average = static_cast<double>(sum)/4;
    cout << fixed << setprecision(2) << showpoint;
    cout << "평균 점수 = " << average;
}