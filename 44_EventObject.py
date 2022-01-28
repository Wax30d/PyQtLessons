import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QApplication, QGridLayout, QLabel

"""
Event object is a Python object that contains a number of attributes describing the event. 
Event object is specific to the generated event type.
"""


# In this example, we display the x and y coordinates of a mouse pointer in a label widget.
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.text = None
        self.label = None
        self.initUI()

    def initUI(self):
        grid = QGridLayout()

        x = 0
        y = 0

        self.text = f'x: {x},  y: {y}'

        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignmentFlag.AlignTop)

        """
        Mouse tracking is disabled by default, 
        so the widget only receives mouse move events when at least one mouse button is pressed 
        while the mouse is being moved. 
        If mouse tracking is enabled, the widget receives mouse move events even if no buttons are pressed.
        """
        self.setMouseTracking(True)
        self.setLayout(grid)

        self.setGeometry(300, 300, 450, 300)
        self.setWindowTitle('Event object')
        self.show()

    """
    The e is the event object; it contains data about the event that was triggered. 
    In our case it is mouse move event. With the position().x() and e.position().y() methods 
    we determine the x and y coordinates of the mouse pointer.
    """
    def mouseMoveEvent(self, e):
        x = int(e.position().x())
        y = int(e.position().y())

        text = f'x: {x},  y: {y}'
        self.label.setText(text)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
