#include <iostream>
#include <iomanip>
#include <typeinfo>
#include <limits>

using namespace std;

int main(){

    int a = 5;
    cout << sizeof(a);

    cout << numperic_limits<unsigned int>::max();
}