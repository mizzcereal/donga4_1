#include <iostream>
#include <string>

using namespace std;

void kor_to_eng(string input){
    string hungry = input;
    if(hungry == "I am hungry" || hungry == "i am hungry"){
        cout << "�¾ҽ��ϴ�." << endl;
    }else{
        cout << input <<"�� ��ƴ�" << endl;
    }
}


int main(){

    string input;
    cout << "���� ������ٸ� ���� �������� �ۼ��ϼ���. " << endl;
    getline(cin, input);
    kor_to_eng(input);

    return 0;
}

