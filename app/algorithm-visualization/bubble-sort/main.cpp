#include <QApplication>
#include <QPushButton>

// NOTE: THIS APPLICATIONS WILL BE USED FOR WEB ASSEMBLY
// and thus wasm is required to build

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    QPushButton button("Click me");
    QObject::connect(&button, &QPushButton::clicked, [](){
        qDebug() << "Hello, World!";
    });
    button.show();

    return a.exec();
}
