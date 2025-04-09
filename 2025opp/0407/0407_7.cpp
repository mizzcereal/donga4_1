#include <iostream>
#include <fstream>

using namespace std;

int main(){

    ifstream fin("triangle.txt");
    ofstream fout("triangle_result.txt");

    int num, a, b, c;
    while(fin >> num >> a >> b >> c){
        if(a + b <c || a +c < b || b+c < a){
            fout << num << " X " << endl;
        }else if(a == b && b == c && c == a){
            fout << num << " O 정삼각형 " <<endl;
        }else if(a == b || b == c || c == a){
            fout << num << " O 이등변삼각형" << endl;
        }else{
            fout << num << " O " << endl;
        }
    }
    cout << "complete!!" << endl;
    fin.close();
    fout.close();
}