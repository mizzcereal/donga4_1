#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main(){

    srand(time(0));
    int num = rand() % 11 + 5;
    for(int i = 0; i<10; i++){
        cout << num << endl;
    }

    return 0;
}