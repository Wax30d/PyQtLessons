import sys

from PyQt6.QtWidgets import QApplication, QWidget, QToolTip, QPushButton
from PyQt6.QtGui import QFont


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # In this example, we show a tooltip for two PyQt6 widgets.
        # To create a tooltip, we call the setTooltip method.
        # We can use rich text formatting.
        QToolTip.setFont(QFont('Arial', 14))
        self.setToolTip('Tooltip for <b>QWidget</b>')

        btn = QPushButton('Button', self)

        # We create a push button widget and set a tooltip for it.
        btn.setToolTip('Tooltip for <b>QPushButton</b>')

        # The button is being resized and moved on the window.
        # The sizeHint method gives a recommended size for the button.
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('PyQt tooltip')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())
