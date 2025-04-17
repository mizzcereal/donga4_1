#include <iostream>
#include <cstdlib>

using namespace std;

int main(){

    for(int i = 0; i<10; i++){
        cout << rand() << endl; // rand를 실행하는데 랜던으로 나온 숫자가 한번 나오고 그 숫자가 계속 나옴
    }

    return 0;
}