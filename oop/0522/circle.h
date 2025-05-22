#ifndef CIRCLE_H
#define CIRCLE_H


using namespace std;

class Circle{
    private:
        double radius;
    public:
        Circle(double radius);
        Circle();
        Circle(const Circle &circle);
        ~Circle();
        void setRadius(double radius);
        double getRadius() const;
        double getArea() const;
        double getParameter() const;
};

#endif