#include <iostream>

using namespace std;

int main(){

    int num;
    do{
        cout << "���� ���� �Է� : ";
        cin >> num;
    }while(num <=0);

    if(num == 1){
        cout << "1�� �Ҽ��� �ռ����� �ƴ�." << endl;
        return 0;
    }
    
    for(int i =2; i < num; i++){
        if(num % i == 0){
            cout << num << " --> �ռ��� " << endl;
            cout << i <<"�� ���������ϴ�." << endl;
            return 0;         
        }
    }
    cout << num <<" --> �Ҽ�" <<endl;
}