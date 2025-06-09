#include <GL/glut.h>
#include <iostream>
#include <cmath>

using namespace std;

#define GL_PI 3.14

void RenderScene(void) {

    glClear(GL_COLOR_BUFFER_BIT);

    /* 삼각형 그리기
    glBegin(GL_TRIANGLES);
        glColor3f(1.0f, 0.0f, 0.0f);
        glVertex2f(0.0f, 0.0f);
        glColor3f(0.0f, 1.0f, 0.0f);
        glVertex2f(50.0f, 0.0f);
        glColor3f(0.0f, 0.0f, 1.0f);
        glVertex2f(50.0f, 50.0f);
    glEnd();
    */

    /*3_6 폴리곤 그리기
    glBegin(GL_TRIANGLE_STRIP);
        glVertex2f(50.0f, 0.0f);
        glVertex2f(50.0f, 50.0f);
        glVertex2f(0.0f, 0.0f);
        glColor3f(1.0f, 0.0f, 0.0f);
        glVertex2f(0.0f, 50.0f);
    glEnd();
    */

    //3_6_1 폴리곤 그리기
    glBegin(GL_TRIANGLE_STRIP);
        glVertex2f(0.0f, 0.0f);
        glVertex2f(50.0f, 0.0f);
        glVertex2f(50.0f, 50.0f);
        glVertex2f(0.0f, 50.0f);
        glVertex2f(50.0f, 100.0f);
    glEnd();

    glFlush();
}

void SetupRC(void) {
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
    glShadeModel(GL_SMOOTH);
}

void ChangeSize(GLsizei w, GLsizei h) {
    cout << "w = " << w << ", h = " << h << endl;
    cout << "ChangeSize" << endl;

    GLint wSize = 100;
    GLfloat aspectRatio;

    if (h == 0) {
        h = 1;
    }

    glViewport(0, 0, w, h);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();

    // 올바른 near/far 설정
    aspectRatio = (GLfloat)w / (GLfloat)h;
    if (w <= h) {
        glOrtho(-wSize, wSize, -wSize / aspectRatio, wSize / aspectRatio, -100, 100);
    }
    else {
        glOrtho(-wSize * aspectRatio, wSize * aspectRatio, -wSize, wSize, -100, 100);
    }

    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
}



int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(500, 500);
    glutInitWindowPosition(100, 100);
    glutCreateWindow("simple");

    glutDisplayFunc(RenderScene);
    glutReshapeFunc(ChangeSize);

    SetupRC();

    glutMainLoop();
}
