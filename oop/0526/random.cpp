#include <iostream>
#include <cstdlib>
#include <ctime>
#include "random.h"

using namespace std;

RandomInteger::RandomInteger(){};

RandomInteger::RandomInteger(int low, int high){
    this->low = low;
    this->high = high;
    srand(time(0));
    value = rand() % (high-low+1) + low;
}

RandomInteger::~RandomInteger(){
    cout << "소멸!" << endl;
}

void RandomInteger::print() const{
    cout << value << endl;
}
