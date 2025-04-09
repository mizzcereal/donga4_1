#include <iostream>

using namespace std;

int main(){
    const double pi = 3.141592;
    double a, b, h;

    cout << "밑변(반지름)과 윗변, 높이를 입력하세요 : ";
    cin >> a >> b >> h;
    cout << "밑변 " << a << "윗변 " << b << "높이 " << h << "인 사다리꼴의 넓이는 " << (a+b)*h * 1/2 << "입니다." << endl;
    cout << "반지름 " << a << "인 원의 넓이는 " << a * a * pi << "입니다." << endl;
    cout << "반지름 " << a<< "높이 " << h << "인 원기둥의 부피는 " << a * a * h * pi << "입니다." << endl;

}