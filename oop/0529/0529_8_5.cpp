#include <iostream>
#include <string>

using namespace std;

int main(){

    string question[] = {"��", "�����", "�⸰", "�ڳ���", "ǥ��"};
    string answer[] = {"dog", "cat", "giraffe", "elephant", "leopard"};
    string ox = "";
    int score = 0;

    cout << "���ܾ�� �ٲټ���." << endl;
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

    cout << "==> " << ox << " " << score << " �� " << endl;

    return 0;
}