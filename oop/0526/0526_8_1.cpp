#include <iostream>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <cassert>

using namespace std;

int main(){

    ifstream fin("scores.txt");
    ofstream fout("result.txt");
    assert(fin && fout); // ������ ������
    if(!fin || !fout){
        cout << "���Ͼ���" << endl;
        return 0;
    }

    string name;
    double arr[100];
    int count = 0;
    while(fin >> name >> arr[count]){
        count++;
    }

    sort(arr, arr+count);

    for(int i = 0; i < count; i++){
        fout << arr[i] << endl;
    }

    fout << "��" << endl;
    fin.close();
    fout.close();
    
    return 0;
}