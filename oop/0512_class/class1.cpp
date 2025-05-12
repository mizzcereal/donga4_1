#include <iostream>

using namespace std;

class Circle{
    private:
        double radius;
    public:
        double getRadius() const;
        double getArea() const;
        double getParameter() const;
        void setRadius(double value);
};

double Circle::getRadius() const{
    return radius;
}

double Circle::getArea() const{
    const double PI = 3.141592;
    return (radius * radius * PI);
}

double Circle::getParameter() const{
    const double PI = 3.141592;
    return (2 * PI * radius);
}

void Circle::setRadius(double value){
    radius = value;
}

int main(){

    Circle c1;
    c1.setRadius(10.0);
    cout << "c1의 반지름" << c1.getRadius() << endl;

    return 0;
}