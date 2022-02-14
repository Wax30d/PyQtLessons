from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QPainter, QPen
from PyQt6.QtCore import Qt
import sys


"""
The QPen is an elementary graphics object. 
It is used to draw lines, curves and outlines of rectangles, ellipses, polygons, or other shapes.
"""


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 280, 270)
        self.setWindowTitle('Pen styles')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()

    @staticmethod
    def drawLines(qp):
        # Draw six lines.
        # The lines are drawn in six different pen styles.
        # There are five predefined pen styles.
        # We can create also custom pen styles.
        # The last line is drawn using a custom pen style.
        pen = QPen(Qt.GlobalColor.black, 2, Qt.PenStyle.SolidLine)

        qp.setPen(pen)
        qp.drawLine(20, 40, 250, 40)

        pen.setStyle(Qt.PenStyle.DashLine)
        qp.setPen(pen)
        qp.drawLine(20, 80, 250, 80)

        pen.setStyle(Qt.PenStyle.DashDotLine)
        qp.setPen(pen)
        qp.drawLine(20, 120, 250, 120)

        pen.setStyle(Qt.PenStyle.DotLine)
        qp.setPen(pen)
        qp.drawLine(20, 160, 250, 160)

        pen.setStyle(Qt.PenStyle.DashDotDotLine)
        qp.setPen(pen)
        qp.drawLine(20, 200, 250, 200)

        pen.setStyle(Qt.PenStyle.CustomDashLine)
        pen.setDashPattern([1, 4, 5, 4])
        qp.setPen(pen)
        qp.drawLine(20, 240, 250, 240)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
