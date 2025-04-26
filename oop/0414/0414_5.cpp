#include <iostream>
#include <cctype>

using namespace std;

int main(){

    char ch;
    int count_alpha = 0, count_digit = 0, count_alnum = 0;
    cout << "�����Ӱ� �ۼ�!(^Z ����) : " << endl;

    while(cin >> noskipws >> ch){
        if(isalpha(ch)){
            count_alpha++;
        }if(isdigit(ch)){
            count_digit++;
        }if(isalnum(ch)){
            count_alnum++;
        }

        cout << (char)toupper(ch);
    }

    cout << "���ĺ� ���� = " << count_alpha << endl;
    cout << "���� ���� = " << count_digit << endl;
    cout << "���ĺ� or ���� ���� = " << count_alnum << endl;

}