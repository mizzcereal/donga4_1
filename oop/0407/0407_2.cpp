#include <iostream>

using namespace std;

int main(){

    int rows, cols;
    char sym;
    cout << "행의 수 및 열의 수를 입력하세요: ";
    cin >> rows >>cols;
    cout << "어떤 기호로 사각형을 만들까요? : " ;
    cin >> sym;

    for(int i = 1; i <= rows; i++){
        for(int j = 1; j <= cols; j++){
            cout << sym;
        }
        cout << endl;
    }

}