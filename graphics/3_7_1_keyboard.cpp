#include <GL/glut.h>
#include <iostream>
#include <cmath>

using namespace std;

#define GL_PI 3.14

GLfloat xTran = 0.0f;
GLfloat yTran = 0.0f;
GLfloat xRot = 0.0f;
GLfloat yRot = 0.0f;
void keyboard(unsigned char key, int x, int y) {
    if (key == 'a') {
        xTran -= 2.0f;
    }
    else if (key == 'd') {
        xTran += 2.0f;
    }
    else if (key == 'w') {
        yTran += 2.0f;
    }
    else if (key == 's') {
        yTran -= 2.0f;
    }

    glutPostRedisplay();
}

void Specialkeys(int key, int x, int y) {
    if (key == GLUT_KEY_UP) {
        xRot -= 2.0f;
    }if (key == GLUT_KEY_DOWN) {
        xRot += 2.0f;
    }if (key == GLUT_KEY_LEFT) {
        yRot -= 2.0f;
    }if (key == GLUT_KEY_RIGHT) {
        yRot += 2.0f;
    }

    if (xRot > 360.0f) {
        xRot -= 360.0f;
    }if (xRot < 0.0f) {
        xRot += 360.0f;
    }if (yRot > 360.0f) {
        yRot -= 360.0f;
    }if (yRot < 0.0f) {
        yRot += 360.0f;
    }

    glutPostRedisplay(); // dlutDisplayFunc()내에 콜백함수를 강제로 호출시키는 역할을 하는 함수
}

void RenderScene(void) {

    glClear(GL_COLOR_BUFFER_BIT);

    bool bcull = false;
    if (bcull) {
        glEnable(GL_CULL_FACE);
    }
    else {
        glDisable(GL_CULL_FACE);
    }

    glPushMatrix();
    glRotatef(xRot, 1.0f, 0.0f, 0.0f);
    glRotatef(yRot, 0.0f, 1.0f, 0.0f);

    glTranslatef(xTran, 0.0f, 0.0f);
    glTranslatef(0.0f, yTran, 0.0f);

    // 3_7_a 폴리곤 그리기
    GLint i = 0;

    glBegin(GL_TRIANGLE_FAN);
    glVertex3f(0, 0, 0);
    for (GLfloat angle = 0; angle < (2.0f * 3.14); angle += (3.14 / 8.0f)) {
        GLfloat x = 50.0f * sin(angle);
        GLfloat y = 50.0f * cos(angle);
        i++;
        if (i % 2 == 0) {
            glColor3f(0.0f, 1.0f, 0);
        }
        else {
            glColor3f(1.0f, 0.0f, 0);
        }
        glVertex3f(x, y, 0);
    }
    glEnd();


    glPopMatrix();
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
    glutKeyboardFunc(keyboard);
    glutSpecialFunc(Specialkeys);
    glutReshapeFunc(ChangeSize);

    SetupRC();

    glutMainLoop();
}
