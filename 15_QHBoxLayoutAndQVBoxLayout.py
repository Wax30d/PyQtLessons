import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout


"""This example places the two buttons in the lower right corner of the window. 
When we resize the app window, they are fixed in the lower right corner. 
We use both QHBoxLayout and QVBoxLayout layouts."""


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        """A stretch factor was added before adding the two buttons,
        which will push the two buttons to the right side of the window."""

        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        """To get the layout we want, we also need to put the horizontal layout into the vertical layout. 
        The stretch factor on the vertical box pushes 
        the horizontal box including the controls inside to the bottom of the window."""

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        """Finally, we set the main layout of the window."""
        self.setLayout(vbox)
        self.setGeometry(300, 300, 350, 150)
        self.setWindowTitle('Box layout example, QHBoxLayout, QVBoxLayout')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())
