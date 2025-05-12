#include <iostream>

using namespace std;

void change(int *x, int *y){
    int temp = *x;
    *x = *y;
    *y= temp;
}

int main(){

    int x, y;

    cin >> x >> y;

    change(&x,&y);
    
    cout << x << " " << y << endl;
}