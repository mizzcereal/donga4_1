#include <GL/glut.h>
#include <iostream>
#include <cmath>

using namespace std;

#define GL_PI 3.14

void RenderScene(void) {

    GLfloat sizes[2];
    GLfloat step;

    glGetFloatv(GL_POINT_SIZE_RANGE, sizes);
    glGetFloatv(GL_POINT_SIZE_GRANULARITY, &step);

    glClear(GL_COLOR_BUFFER_BIT);
    glColor3f(1.0f, 1.0f, 1.0f);

    glPushMatrix();
    glRotatef(30, 1.0f, 0.0f, 0.0f);
    glRotatef(0, 0.0f, 1.0f, 0.0f);

    GLfloat x,y,z;
    GLfloat angle;

    //중앙
    glEnable(GL_LINE_STIPPLE);
    glLineStipple(4, 0x5555);
    glBegin(GL_LINE_STRIP);
    glVertex3f(0, 0, 0);
    glVertex3f(45, 0, 0);
    glVertex3f(45, 0, 45);
    glVertex3f(45, 0, 0);
    glVertex3f(45, 45, 0);
    glEnd();
    glDisable(GL_LINE_STIPPLE);

    glBegin(GL_LINE_STRIP);
    glVertex3f(0, 0, 0);
    glVertex3f(0, 0, 45);
    glVertex3f(45, 0, 45);
    glVertex3f(45, 45, 45);
    glVertex3f(45, 45, 0);
    glVertex3f(0, 45, 0);
    glVertex3f(0, 0, 0);
    glVertex3f(0, 45, 0);
    glVertex3f(0, 45, 45);
    glVertex3f(45, 45, 45);
    glVertex3f(0, 45, 45);
    glVertex3f(0, 0, 45);
    glEnd();

    glPopMatrix();
    glutSwapBuffers();
    glFlush();
}

void SetupRC(void) {
    cout << "SetupRC" << endl;
    glClearColor(0.0f, 0.0f, 0.0f, 0.0f);
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
