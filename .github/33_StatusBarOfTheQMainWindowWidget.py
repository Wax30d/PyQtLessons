import sys
from PyQt6.QtWidgets import QMainWindow, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        """
        The statusbar is created with the help of the QMainWindow widget.
        To get the statusbar, we call the statusBar method of the QMainWindow class.
        The first call of the method creates a status bar.
        Subsequent calls return the statusbar object.
        The showMessage displays a message on the statusbar.
        """
        self.statusBar().showMessage('Ready')

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Statusbar')


def main():
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
