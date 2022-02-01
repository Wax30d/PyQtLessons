from PyQt6.QtWidgets import QWidget, QPushButton, QFrame, QColorDialog, QApplication
from PyQt6.QtGui import QColor
import sys


# The application example shows a push button and a QFrame.
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.btn = None
        self.frm = None
        self.initUI()

    def initUI(self):
        # The widget background is set to black colour.
        # Using the QColorDialog, we can change its background.
        col = QColor(0, 0, 0)

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)

        self.btn.clicked.connect(self.showDialog)

        self.frm = QFrame(self)
        # This is an initial colour of the QFrame background.
        self.frm.setStyleSheet("QWidget { background-color: %s }"
                               % col.name())
        self.frm.setGeometry(130, 22, 200, 200)

        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle('Color dialog')
        self.show()

    def showDialog(self):
        # QColorDialog provides a dialog widget for selecting colour values.
        # This line pops up the QColorDialog.
        col = QColorDialog.getColor()

        # We check if the colour is valid.
        # If we click on the Cancel button, no valid colour is returned.
        # If the colour is valid, we change the background colour using style sheets.
        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }"
                                   % col.name())


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
