#include <iostream>
#include <iomanip>

using namespace std;

int main(){

    double num, fd, cd;

    cout << "¼±ÅÃÇÏ¼¼¿ä (1:È­¾¾->¼·¾¾, 2:¼·¾¾->È­¾¾)";
    cin >> num;
    if(num == 1){
        cout << "È­¾¾¿Âµµ ÀÔ·Â : ";
        cin  >> fd;
        cd = (fd-32) * 5 / 9; 
        cout << fixed << showpoint << setprecision(5);
        cout << "¼·¾¾¿Âµµ´Â " << cd << "ÀÔ´Ï´Ù.";
    }else if(num == 2){
        cout << "¼·¾¾¿Âµµ ÀÔ·Â : ";
        cin >> cd;
        fd = (cd * 9 / 5) + 32;
        cout << fixed << showpoint << setprecision(5);
        cout << "È­¾¾¿Âµµ´Â " << fd << "ÀÔ´Ï´Ù.";   
    }else{
        cout << "1, 2Áß¿¡ ÇÏ³ª¸¦ ÀÔ·ÂÇÏ¼¼¿ä.";
    }
}