import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('One', self)
        btn1.move(30, 50)
        btn2 = QPushButton('Two', self)
        btn2.move(150, 50)
        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Window')
        self.show()

    def buttonClicked(self):
        sender = self.sender().text()
        self.statusBar().showMessage(sender + ' changed')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())
