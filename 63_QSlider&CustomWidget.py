from PyQt6.QtWidgets import (QWidget, QSlider, QApplication,
                             QHBoxLayout, QVBoxLayout)
from PyQt6.QtCore import QObject, Qt, pyqtSignal
from PyQt6.QtGui import QPainter, QFont, QColor, QPen
import sys

"""
We have a QSlider and a custom widget. 
The slider controls the custom widget. 
This widget shows graphically the total capacity of a medium and the free space available to us. 
The minimum value of our custom widget is 1, the maximum is OVER_CAPACITY. 
If we reach value MAX_CAPACITY, we begin drawing in red colour. This normally indicates over-burning.
"""


class Communicate(QObject):
    updateBW = pyqtSignal(int)


# The burning widget is based on the QWidget widget.
class BurningWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.num = None
        self.value = None
        self.initUI()

    def initUI(self):
        # We change the minimum size (height) of the widget.
        # The default value is a bit small for us.
        self.setMinimumSize(1, 30)
        self.value = 75
        self.num = [75, 150, 225, 300, 375, 450, 525, 600, 675]

    def setValue(self, value):
        self.value = value

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()

    def drawWidget(self, qp):

        MAX_CAPACITY = 700
        OVER_CAPACITY = 750

        # We use a smaller font than the default one.
        # This better suits our needs.
        font = QFont('Serif', 12, QFont.Weight.Light)
        qp.setFont(font)

        """
        We draw the widget dynamically. 
        The greater is the window, the greater is the burning widget and vice versa. 
        That is why we must calculate the size of the widget onto which we draw the custom widget. 
        The till parameter determines the total size to be drawn. 
        This value comes from the slider widget. 
        It is a proportion of the whole area. 
        The full parameter determines the point where we begin to draw in red colour.

        The actual drawing consists of three steps. 
        We draw the yellow or the red and yellow rectangle. 
        Then we draw the vertical lines which divide the widget into several parts. 
        Finally, we draw the numbers which indicate the capacity of the medium.
        """
        size = self.size()
        w = size.width()
        h = size.height()

        step = int(round(w / 10))

        till = int(((w / OVER_CAPACITY) * self.value))
        full = int(((w / OVER_CAPACITY) * MAX_CAPACITY))

        if self.value >= MAX_CAPACITY:

            qp.setPen(QColor(255, 255, 255))
            qp.setBrush(QColor(255, 255, 184))
            qp.drawRect(0, 0, full, h)
            qp.setPen(QColor(255, 175, 175))
            qp.setBrush(QColor(255, 175, 175))
            qp.drawRect(full, 0, till - full, h)

        else:

            qp.setPen(QColor(255, 255, 255))
            qp.setBrush(QColor(255, 255, 184))
            qp.drawRect(0, 0, till, h)

        pen = QPen(QColor(20, 20, 20), 1,
                   Qt.PenStyle.SolidLine)

        qp.setPen(pen)
        qp.setBrush(Qt.BrushStyle.NoBrush)
        qp.drawRect(0, 0, w - 1, h - 1)

        j = 0

        for i in range(step, 10 * step, step):
            # We use font metrics to draw the text.
            # We must know the width of the text in order to center it around the vertical line.
            qp.drawLine(i, 0, i, 5)
            metrics = qp.fontMetrics()
            fw = metrics.horizontalAdvance(str(self.num[j]))

            x, y = int(i - fw / 2), int(h / 2)
            qp.drawText(x, y, str(self.num[j]))
            j = j + 1


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.c = None
        self.wid = None
        self.initUI()

    def initUI(self):
        OVER_CAPACITY = 750

        # When we move the slider, the changeValue method is called.
        # Inside the method, we send a custom updateBW signal with a parameter.
        # The parameter is the current value of the slider.
        # The value is later used to calculate the capacity of the Burning widget to be drawn.
        # The custom widget is then repainted.
        sld = QSlider(Qt.Orientation.Horizontal, self)
        sld.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        sld.setRange(1, OVER_CAPACITY)
        sld.setValue(75)
        sld.setGeometry(30, 40, 150, 30)

        self.c = Communicate()
        self.wid = BurningWidget()
        self.c.updateBW[int].connect(self.wid.setValue)

        sld.valueChanged[int].connect(self.changeValue)

        # The burning widget is placed at the bottom of the window.
        # This is achieved using one QHBoxLayout and one QVBoxLayout.
        hbox = QHBoxLayout()
        hbox.addWidget(self.wid)
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 390, 210)
        self.setWindowTitle('Burning widget')
        self.show()

    def changeValue(self, value):
        self.c.updateBW.emit(value)
        self.wid.repaint()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
