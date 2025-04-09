#include <iostream>
#include <iomanip>

using namespace std;

int main(){

    int size;

    do{
        cout << "표의 크기 입력(2~10) :" ;
        cin >> size;
    }while(size<2 || size >10);
    int i = 1;
    while(i <= size){
        int j = 1;
        while(j <= size){
            cout << setw(4) << i * j;
            j++;
        }
        cout << endl;
        i++;
    }
}