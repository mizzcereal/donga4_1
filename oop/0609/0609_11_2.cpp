#include <iostream>
#include <string>

using namespace std;

int main(){

    int arr[] = {10,20,30,77};
    double darr[] = {3.14, 7.99, -1.1};
    string sarr[] = {"딸기", "바나나", "우유"};

    for(int a : arr){
        cout << a << endl;
    }

    for(double a : darr){
        cout << a << endl;
    }

    for(string a: sarr){
        cout << a;
    }

    string ab = "test";
    for(char a : ab) cout << a << "\t";
}