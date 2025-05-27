#include <iostream>
#include <string>

using namespace std;

class Car{
    public:
        static string getClassNaame();
};

string Car::getClassNaame(){
    return "car";
}

int main(){

    cout << Car::getClassNaame() << endl;
    return 0;
}