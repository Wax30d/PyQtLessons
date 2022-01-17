"""
When we call the exec() method of the application, the application enters the main loop.
The main loop detects various events and sends them to the event object.
Signals and slots are used for communication between objects, and when a particular event occurs, the signal is fired.
"""

import sys

from PyQt6.QtWidgets import QApplication, QWidget, QSlider, QLCDNumber, QVBoxLayout
from PyQt6.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        lcd = QLCDNumber(self)

        sld = QSlider(Qt.Orientation(1), self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)

        sld.valueChanged.connect(lcd.display)

        self.setGeometry(250, 250, 250, 150)
        self.setWindowTitle('Events demo')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())
