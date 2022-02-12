import random
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter
from PyQt6.QtWidgets import QWidget, QApplication


# In our example, we draw randomly 1000 red points on the client area of the window.
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setMinimumSize(50, 50)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Points')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)

        # We draw the point with the drawPoint method.
        self.drawPoints(qp)
        qp.end()

    def drawPoints(self, qp):
        # We set the pen to red colour.
        # We use a predefined Qt.GlobalColor.red colour constant.
        qp.setPen(Qt.GlobalColor.red)

        # Each time we resize the window, a paint event is generated.
        # We get the current size of the window with the size method.
        # We use the size of the window to distribute the points all over the client area of the window.
        size = self.size()

        for i in range(1000):
            x = random.randint(1, size.width() - 1)
            y = random.randint(1, size.height() - 1)
            qp.drawPoint(x, y)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
