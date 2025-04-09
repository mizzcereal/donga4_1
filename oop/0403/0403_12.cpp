#include <iostream>
#include <fstream>

using namespace std;

int main(){
    int n, sum = 0;
    
    ifstream fin;
    fin.open("numbers.dat");
    if(!fin){
        cerr << "Error input file" << endl;
        return -1;
    }
    while(fin >> n){
        sum += n;
    }
    fin.close();
    
    ofstream fout;
    fout.open("numbers_sum.txt");
    if(!fout){
        cerr << "Error output file" << endl;
        return -1;
    }
    fout << "гу = " << sum << endl;
    fout.close();

    return 0;
}