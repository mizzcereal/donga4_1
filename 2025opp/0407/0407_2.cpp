#include <iostream>

using namespace std;

int main(){

    int rows, cols;
    char sym;
    cout << "���� �� �� ���� ���� �Է��ϼ���: ";
    cin >> rows >>cols;
    cout << "� ��ȣ�� �簢���� ������? : " ;
    cin >> sym;

    for(int i = 1; i <= rows; i++){
        for(int j = 1; j <= cols; j++){
            cout << sym;
        }
        cout << endl;
    }

}