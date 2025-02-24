#include "mainwindow.h"


auto vertexShaderSource =
#ifdef EMSCRIPTEN
        "precision mediump float;\n"
#endif
        R"(
attribute vec2 position;
attribute vec3 color;
varying vec3 fragColor;
uniform float angle;

void main() {
    float rad = radians(angle);
    mat2 rotation = mat2(
        cos(rad), -sin(rad),
        sin(rad),  cos(rad)
    );
    vec2 rotatedPosition = rotation * position;
    gl_Position = vec4(rotatedPosition, 0.0, 1.0);
    fragColor = color;
}
)";

auto fragmentShaderSource =
#ifdef EMSCRIPTEN
        "precision mediump float;\n"
#endif
        R"(
varying vec3 fragColor;

void main() {
    gl_FragColor = vec4(fragColor, 1.0);
}
)";

MyOpenGLWidget::MyOpenGLWidget(QWidget *parent)
    : QOpenGLWidget(parent), vbo(0), rotationAngle(0.0f) {
    // 使用定时器更新动画
    auto *timer = new QTimer(this);
    connect(timer, &QTimer::timeout, this, [this] {
        rotationAngle += 0.5f;// 每次增加1度
        if (rotationAngle >= 360.0f)
            rotationAngle -= 360.0f;
        update();// 触发重新绘制
    });
    timer->start(8);// 每8毫秒触发一次，相当于约120帧/秒
}

MyOpenGLWidget::~MyOpenGLWidget() {
    makeCurrent();
    glDeleteBuffers(1, &vbo);
    doneCurrent();
}

void MyOpenGLWidget::initializeGL() {
    initializeOpenGLFunctions();

    // 初始化背景色
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f);

    // 初始化着色器程序
    // 编译顶点着色器
    if (!shaderProgram.addShaderFromSourceCode(QOpenGLShader::Vertex, vertexShaderSource)) {
        qDebug() << "Vertex shader compilation failed:" << shaderProgram.log();
        exit(1);
    }

    // 编译片段着色器
    if (!shaderProgram.addShaderFromSourceCode(QOpenGLShader::Fragment, fragmentShaderSource)) {
        qDebug() << "Fragment shader compilation failed:" << shaderProgram.log();
        exit(1);
    }

    // 链接着色器程序
    if (!shaderProgram.link()) {
        qDebug() << "Shader program link failed:" << shaderProgram.log();
        exit(1);
    }

    qDebug() << "Shader program link succeeded";

    // 顶点数据：位置 (x, y) 和颜色 (r, g, b)
    constexpr GLfloat vertices[] = {
            // Position     // Color
            0.0f, 0.5f, 1.0f, 0.0f, 0.0f,  // 顶点 1
            -0.5f, -0.5f, 0.0f, 1.0f, 0.0f,// 顶点 2
            0.5f, -0.5f, 0.0f, 0.0f, 1.0f  // 顶点 3
    };

    // 创建并绑定顶点缓冲对象 (VBO)
    glGenBuffers(1, &vbo);
    glBindBuffer(GL_ARRAY_BUFFER, vbo);
    glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);
}

void MyOpenGLWidget::resizeGL(int w, int h) {
    glViewport(0, 0, w, h);// 设置视口大小
}

void MyOpenGLWidget::paintGL() {
    glClear(GL_COLOR_BUFFER_BIT);// 清除颜色缓存

    shaderProgram.bind();

    // 设置旋转角度的 uniform
    shaderProgram.setUniformValue("angle", rotationAngle);

    // 绑定 VBO 并设置属性指针
    glBindBuffer(GL_ARRAY_BUFFER, vbo);

    const int positionLoc = shaderProgram.attributeLocation("position");
    shaderProgram.enableAttributeArray(positionLoc);
    glVertexAttribPointer(positionLoc, 2, GL_FLOAT, GL_FALSE, 5 * sizeof(GLfloat), nullptr);

    const int colorLoc = shaderProgram.attributeLocation("color");
    shaderProgram.enableAttributeArray(colorLoc);
    glVertexAttribPointer(colorLoc, 3, GL_FLOAT, GL_FALSE, 5 * sizeof(GLfloat), reinterpret_cast<void *>(2 * sizeof(GLfloat)));

    // 绘制三角形
    glDrawArrays(GL_TRIANGLES, 0, 3);

    shaderProgram.disableAttributeArray(positionLoc);
    shaderProgram.disableAttributeArray(colorLoc);

    shaderProgram.release();
}
