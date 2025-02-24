#ifndef MYOPENGLWIDGET_H
#define MYOPENGLWIDGET_H

#include <QOpenGLFunctions>
#include <QOpenGLShaderProgram>
#include <QOpenGLWidget>
#include <QTimer>

class MyOpenGLWidget : public QOpenGLWidget, protected QOpenGLFunctions {
    Q_OBJECT

public:
    explicit MyOpenGLWidget(QWidget *parent = nullptr);
    ~MyOpenGLWidget() override;

protected:
    void initializeGL() override;        // 初始化 OpenGL
    void resizeGL(int w, int h) override;// 处理窗口大小变化
    void paintGL() override;             // 渲染内容

private:
    QOpenGLShaderProgram shaderProgram;// 着色器程序
    GLuint vbo;                        // 顶点缓冲对象
    float rotationAngle;               // 当前旋转角度
};

#endif// MYOPENGLWIDGET_H
