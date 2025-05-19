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
        cout << this->name << "(��)�� ����Ϸ�" << endl;
    }else{
        cout << "Family name change not allowed" << endl;
    }
}

int main() {  
    Person person("��浿");
    cout << "���� �̸�: " + person.getName() << endl;
    person.setName("���");  // ù ���� �ٸ� 
    person.setName("����");   // ù ���� ���� (����)
    person.setName("�ڱ浿");  // ù ���� �ٸ�
    cout << "���� �̸�: " + person.getName() << endl;
 
    return 0;
}