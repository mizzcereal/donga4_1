#include <iostream>
#include <string>

using namespace std;

void kor_to_eng(string input){
    string hungry = input;
    if(hungry == "I am hungry" || hungry == "i am hungry"){
        cout << "맞았습니다." << endl;
    }else{
        cout << input <<"은 답아님" << endl;
    }
}


int main(){

    string input;
    cout << "나는 배고프다를 영어 문장으로 작성하세요. " << endl;
    getline(cin, input);
    kor_to_eng(input);

    return 0;
}

