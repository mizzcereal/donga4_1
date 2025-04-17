#include <iostream>

using namespace std;

void change(int &a, int &b){
    int temp = a;
    a = b;
    b = temp;
}

int main(){
    int x, y;

    cin >> x >> y;

    change(x, y);

    cout << x << " " << y;
}