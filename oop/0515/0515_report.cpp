#include <iostream>
#include <string>
#include <typeinfo>

using namespace std;

class Person{
    private:
        string name;
    public:
        Person(string name);
        string getName();
        void setName(string name);

        ~Person();
};

Person::Person(string name){
    this->name = name;
}

Person::~Person(){
    cout << "name destroyed" <<endl;
}

string Person::getName(){
    return name;
}

void Person::setName(string name){
    if(this->name.substr(0,3) == name.substr(0,3)){
        this->name = name;
        cout << this->name << "(으)로 변경완료" << endl;
    }else{
        cout << "Family name change not allowed" << endl;
    }
}

int main() {  
    Person person("고길동");
    cout << "원래 이름: " + person.getName() << endl;
    person.setName("곡식");  // 첫 글자 다름 
    person.setName("고구마");   // 첫 글자 같음 (성공)
    person.setName("박길동");  // 첫 글자 다름
    cout << "최종 이름: " + person.getName() << endl;
 
    return 0;
}