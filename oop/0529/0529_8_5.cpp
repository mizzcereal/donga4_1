#include <iostream>
#include <string>

using namespace std;

int main(){

    string question[] = {"개", "고양이", "기린", "코끼리", "표범"};
    string answer[] = {"dog", "cat", "giraffe", "elephant", "leopard"};
    string ox = "";
    int score = 0;

    cout << "영단어로 바꾸세요." << endl;
    for(int i = 0; i <5; i++){
        string animal;

        cout << question[i] << ": ";
        getline(cin, animal);

        if(answer[i] == animal){
            ox += 'O';
            score += 20;
        }else{
            ox += 'X';
        }
    }

    cout << "==> " << ox << " " << score << " 점 " << endl;

    return 0;
}