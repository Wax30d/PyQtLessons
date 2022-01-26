import sys
from PyQt6.QtWidgets import QWidget, QLabel, QApplication

"""
The programmer specifies the position and the size of each widget in pixels. 
When you use absolute positioning, we have to understand the following limitations:

    * The size and the position of a widget do not change if we resize a window
    * Applications might look different on various platforms
    * Changing fonts in our application might spoil the layout
    * If we decide to change our layout, we must completely redo our layout, which is tedious and time consuming
"""


# The following example positions widgets in absolute coordinates.
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        """
        We use the move method to position our widgets.
        In our case these are labels.
        We position them by providing the x and y coordinates.
        The beginning of the coordinate system is at the left top corner.
        The x values grow from left to right. The y values grow from top to bottom.
        """
        lbl1 = QLabel('PyQt6', self)
        lbl1.move(15, 10)

        lbl2 = QLabel('tutorials', self)
        lbl2.move(35, 40)

        lbl3 = QLabel('for programmers', self)
        lbl3.move(55, 70)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Absolute')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
