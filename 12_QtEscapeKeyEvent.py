import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import Qt


# If we press the Esc key on the keyboard, the application terminates.
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('PyQt events with keyboard')
        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key.Key_Escape:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())
