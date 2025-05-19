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
    title = "제목없음";
    author = "작가미상";
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
    Book b2("해리포터", "j.k롤링");
    Book b3(b2); // b3는 합성 복사 생성자

    b1.print();
    b2.print();
    b3.print(); 

    return 0;
}