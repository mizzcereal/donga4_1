#include <iostream>
#include <cassert>
#include "circle.h"

Circle::Circle(){
    radius = 0.0;
    cout << "�⺻������ ȣ��" << endl;
}

Circle::Circle(double radius){
    this->radius = radius;
    cout << "�Ķ���� ������ ȣ��" << endl;
}

Circle::~Circle(){
    cout << "�Ҹ��� ȣ�� " << endl;
}

void Circle::setRadius(double radius){
    this->radius = radius;
}

double Circle::getArea() const{
    const double PI = 3.141592;
    return (PI * radius * radius);
}

double Circle::getRadius() const{
    return radius;
}

double Circle::getParameter() const{
    const double PI = 3.141592;
    return (2 * PI * radius);
}