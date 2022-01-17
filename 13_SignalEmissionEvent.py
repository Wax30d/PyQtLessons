import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import pyqtSignal, QObject

"""
An object created from a QObject can signal. 
In the following example, we’ll look at how we can customize the signal sent.
We create a new signal called closeApp. This signal is emitted by the mouse press event. 
This signal is connected to the close() slot in QMainWindow.
"""


class Communicate(QObject):
    closeApp = pyqtSignal()


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.c = None
        self.initUI()

    def initUI(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Mouse events')
        self.show()

    def mousePressEvent(self, event):
        self.c.closeApp.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())
