#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

int main(){

    int all_student = 0;
    double score, sum, avg, max_score = -100;
    string name, top_name;

    ifstream fin;
    fin.open("scores.txt");
    if(!fin){
        cerr << "Error opening scores.txt" <<endl;
        return -1;
    }

    while(fin >> name >> score){
        sum += score;
        all_student++;
        if(score > max_score){
            max_score = score;
            top_name = name;
        }          
    }

    avg = sum/all_student;

    fin.close();

    ofstream fout("result.txt");

    if(!fout){
        cerr << "Error opening result.txt" << endl;
        return -1;
    }

    fout << setprecision(2) << fixed;
    fout << "총 " << all_student << "명" << endl;
    fout << "합계 : " << sum << endl;
    fout << "평균 : " << avg << endl;
    fout << "최고점" << top_name << " " << max_score;

    cout << "Result saved in result.txt" << endl;

    fout.close();

    return 0;

}