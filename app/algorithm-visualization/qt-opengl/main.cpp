#include "mainwindow.h"

#include <QApplication>

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);

    MyOpenGLWidget widget;
    widget.resize(800, 600);
    widget.show();

    return QApplication::exec();
}
