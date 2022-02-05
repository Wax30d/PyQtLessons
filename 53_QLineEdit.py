import sys
from PyQt6.QtWidgets import (QWidget, QLabel,
                             QLineEdit, QApplication)

"""
QLineEdit is a widget that allows to enter and edit a single line of plain text. 
There are undo and redo, cut and paste, and drag & drop functions available for the widget.
"""

"""
This example shows a line edit widget and a label. 
The text that we key in the line edit is displayed immediately in the label widget.
"""


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.lbl = None
        self.initUI()

    def initUI(self):
        self.lbl = QLabel(self)
        # The QLineEdit widget is created.
        qle = QLineEdit(self)

        qle.move(60, 100)
        self.lbl.move(60, 40)

        # If the text in the line edit widget changes, we call the onChanged method.
        qle.textChanged[str].connect(self.onChanged)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('QLineEdit')
        self.show()

    def onChanged(self, text):
        # Inside the onChanged method, we set the typed text to the label widget.
        # We call the adjustSize method to adjust the size of the label to the length of the text.
        self.lbl.setText(text)
        self.lbl.adjustSize()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
