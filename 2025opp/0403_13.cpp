#include <iostream>

using namespace std;

int main(){

    double n, sum = 0.0;
    do
    {
        cout << "�Ǽ� �Է� : ";
        cin >> n;
        sum += n;
    } while ( n > 0);

    sum -= n; // ���������� �Է��Ѱ� �����ϰ�� �̸� ������
    cout << "�� = " << sum;

    return 0;
    
}