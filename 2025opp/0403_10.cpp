#include <iostream>

using namespace std;

int main(){
    int n, sum = 0;
    cout << "정수를 여러 개 입력(종료 EOF) : " << endl;
    while(cin >> n){
        sum += n;
    }

    cout << "합 = " << sum << endl;
}