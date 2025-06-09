#include <GL/glut.h>
#include <iostream>
#include <cmath>

using namespace std;

#define GL_PI 3.14

void RenderScene(void) {

    glClear(GL_COLOR_BUFFER_BIT);

    //3_7 폴리곤 그리기
    /*
    glBegin(GL_TRIANGLE_FAN);
    glVertex3f(0, 0, 0);
    for (GLfloat angle = 0; angle < (2.0f * 3.14); angle+= (3.14 / 8.0f)){
        GLfloat x = 50.0f*sin(angle);
        GLfloat y = 50.0f*cos(angle);
        glVertex3f(x, y, 0);
    }
    glEnd();
    */

    // 3_7_a 폴리곤 그리기
    GLint i = 0;

    glBegin(GL_TRIANGLE_FAN);
    glVertex3f(0, 0, 0);
        for (GLfloat angle = 0; angle < (2.0f * 3.14); angle+= (3.14 / 8.0f)){
        GLfloat x = 50.0f*sin(angle);
        GLfloat y = 50.0f*cos(angle);
        i++;
        if (i % 2 == 0) {
            glColor3f(0.0f,1.0f, 0);
        }
        else {
            glColor3f(1.0f, 0.0f, 0);
        }
        glVertex3f(x, y, 0);
        }
    glEnd();

    glFlush();
}

void SetupRC(void) {
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
    glShadeModel(GL_FLAT);
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
