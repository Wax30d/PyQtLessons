from PyQt6.QtWidgets import (QWidget, QHBoxLayout,
                             QLabel, QApplication)
from PyQt6.QtGui import QPixmap
import sys

"""
A QPixmap is one of the widgets used to work with images. 
It is optimized for showing images on screen. 
In our code example, we will use the QPixmap to display an image on the window.
"""


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)
        # We create a QPixmap object.
        # It takes the name of the file as a parameter.
        pixmap = QPixmap('cat.gif')

        # We put the pixmap into the QLabel widget.
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(300, 200)
        self.setWindowTitle('Pic')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
