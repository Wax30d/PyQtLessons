from PyQt6.QtWidgets import (QWidget, QSlider,
                             QLabel, QApplication)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
import sys

"""
A QSlider is a widget that has a simple handle. 
This handle can be pulled back and forth. 
This way we are choosing a value for a specific task. 
Sometimes using a slider is more natural than entering a number or using a spin box.

In our example we show one slider and one label. 
The label displays an image. The slider controls the label.
"""


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.label = None
        self.initUI()

    def initUI(self):

        # In our example we simulate a volume control.
        # By dragging the handle of a slider, we change an image on the label.
        # Here we create a horizontal QSlider.
        sld = QSlider(Qt.Orientation.Horizontal, self)
        sld.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        sld.setGeometry(30, 40, 200, 30)
        # We connect the valueChanged signal to the user defined changeValue method.
        sld.valueChanged[int].connect(self.changeValue)

        # We create a QLabel widget and set an initial mute image to it.
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("mute.png"))
        self.label.setGeometry(250, 40, 500, 500)

        self.setWindowTitle('QSlider')
        self.show()

    def changeValue(self, value):

        if value == 0:
            self.label.setPixmap(QPixmap("mute.png"))

        elif 0 < value <= 30:
            self.label.setPixmap(QPixmap('min.png'))

        elif 30 < value < 80:
            self.label.setPixmap(QPixmap('med.png'))

        else:
            self.label.setPixmap(QPixmap('max.png'))


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
