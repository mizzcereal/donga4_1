#include <iostream>
#include <string>

using namespace std;

class Book{
    private:
        string title;
        string author;
    public:
        Book();
        Book(string title, string author);
        void print();
};

Book::Book(){
    title = "�������";
    author = "�۰��̻�";
};

Book::Book(string title, string author){
    this->title =  title;
    this->author = author;
};

void Book::print(){
    cout << title << " " << author << endl;
};

int main(){
    Book b1;
    Book b2("�ظ�����", "j.k�Ѹ�");
    Book b3(b2); // b3�� �ռ� ���� ������

    b1.print();
    b2.print();
    b3.print(); 

    return 0;
}