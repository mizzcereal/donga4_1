#include <iostream>
#include <GL/glut.h>
#include <stdio.h>

using namespace std;

void SetupRC() {
	glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
}

void ChangeSize(GLsizei w, GLsizei h) {

	GLfloat wSize = 100;
	GLfloat aspect = (GLfloat)w / (GLfloat)h;

	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();

	glViewport(0, 0, w, h);

	if (w <= h) {
		glOrtho(-wSize, wSize, -wSize / aspect, wSize / aspect, wSize, -wSize);
	}
	else {
		glOrtho(-wSize * aspect, wSize * aspect, -wSize, wSize, wSize, -wSize);
	}

	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
}

void RenderScene() {


	glClear(GL_COLOR_BUFFER_BIT);
	glPushMatrix();

	glRotatef(45, 1.0f, 0, 0);
	glRotatef(45, 0, 1.0f, 0);

	glColor3f(1.0f, 1.0f, 0.0f);
	glBegin(GL_LINE_STRIP);
		glVertex3f(0, 0, 0);
		glVertex3f(50, 0, 0);
		glVertex3f(50, 50, 0);
		glVertex3f(0, 50, 0);
		glVertex3f(0, 0, 0);
	glEnd();

	glColor3f(1.0f, 0.0f, 0.0f);
	glBegin(GL_LINE_STRIP);
		glVertex3f(0, 50, 0);
		glVertex3f(50, 50, 0);
		glVertex3f(50, 50, -50);
		glVertex3f(0, 50, -50);
		glVertex3f(0, 50, 0);
	glEnd();

	glColor3f(0.0f, 0.0f, 1.0f);
	glBegin(GL_LINE_STRIP);
		glVertex3f(0, 0, 0);
		glVertex3f(0, 0, -50);
		glVertex3f(0, 50, -50);
		glVertex3f(0, 50, 0);
		glVertex3f(0, 0, 0);
	glEnd();

	glEnable(GL_LINE_STIPPLE);
	glLineStipple(4, 0x5555);
	glColor3f(1.0f, 1.0f, 1.0f);
	glBegin(GL_LINE_STRIP);
		glVertex3f(50, 0, 0);
		glVertex3f(50, 0, -50);
		glVertex3f(0, 0, -50);
		glVertex3f(50, 0, -50);
		glVertex3f(50, 50, -50);
	glEnd();

	glPopMatrix();
	glFlush();
}

int main(int argv, char** argc) {

	glutInit(&argv, argc);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
	glutInitWindowSize(500, 500);
	glutInitWindowPosition(1000, 500);
	glutCreateWindow("정육면체 (안보이는 부분은 점선)");

	SetupRC();
	glutDisplayFunc(RenderScene);
	glutReshapeFunc(ChangeSize);
	glutMainLoop();
}