#include <iostream>

using namespace std;

void change(int &a, int &b){
    int temp = a;
    a = b;
    b = temp;
}

int main(){
    int x, y;

    cin >> x >> y;

    change(x, y);
    swap(x,y); // 라이브러리 함수 (#include <algorithm> 헤더파일을 사용안해도되긴하는데 넣는게 좋음)

    cout << x << " " << y;
}