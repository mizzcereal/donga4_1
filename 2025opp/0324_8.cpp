#include <iostream>
using namespace std;

int main(){
    double fd, cd;
    cout << "È­¾¾¿Âµµ ÀÔ·Â : ";
    cin >> fd;

    cd = (fd - 32) * 5 / 9;

    cout.precision(5);
    cout << fixed;
    cout << "¼·¾¾¿Âµµ´Â " << cd << " ÀÔ´Ï´Ù. " << endl;
}