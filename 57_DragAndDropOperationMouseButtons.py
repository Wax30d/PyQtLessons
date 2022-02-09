import sys

from PyQt6.QtCore import Qt, QMimeData
from PyQt6.QtGui import QDrag
from PyQt6.QtWidgets import QPushButton, QWidget, QApplication

"""
In our code example, we have a QPushButton on the window. 
If we click on the button with a left mouse button, the 'press' message is printed to the console. 
By right clicking and moving the button, we perform a drag and drop operation on the button widget.
"""


# We create a Button class which derives from the QPushButton.
# We also reimplement two methods of the QPushButton: the mouseMoveEvent and the mousePressEvent.
# The mouseMoveEvent method is the place where the drag and drop operation begins.
class Button(QPushButton):

    def __init__(self, title, parent):
        super().__init__(title, parent)

    def mouseMoveEvent(self, e):

        # Here we decide that we can perform drag and drop only with a right mouse button.
        # The left mouse button is reserved for clicking on the button.
        if e.buttons() != Qt.MouseButton.RightButton:
            return

        mimeData = QMimeData()

        # The QDrag object is created.
        # The class provides support for MIME-based drag and drop data transfer.
        drag = QDrag(self)
        drag.setMimeData(mimeData)

        drag.setHotSpot(e.position().toPoint() - self.rect().topLeft())

        # The exec method of the drag object starts the drag and drop operation.
        dropAction = drag.exec(Qt.DropAction.MoveAction)

    # We print 'press' to the console if we left-click on the button with the mouse.
    # Notice that we call mousePressEvent method on the parent as well.
    # Otherwise, we would not see the button being pushed.
    def mousePressEvent(self, e):

        super().mousePressEvent(e)

        if e.button() == Qt.MouseButton.LeftButton:
            print('press')


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.button = None
        self.initUI()

    def initUI(self):
        self.setAcceptDrops(True)

        self.button = Button('Button', self)
        self.button.move(100, 65)

        self.setWindowTitle('Click or Move')
        self.setGeometry(300, 300, 550, 450)

    def dragEnterEvent(self, e):
        print("Ho")
        e.accept()

    # In the dropEvent method we specify what happens after we release the mouse button
    # and finish the drop operation.
    # In our case, we find out the current mouse pointer position and move the button accordingly.
    def dropEvent(self, e):
        position = e.position()
        self.button.move(position.toPoint())

        # We specify the type of the drop action with setDropAction.
        # In our case it is a move action.
        e.setDropAction(Qt.DropAction.MoveAction)
        e.accept()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec()


if __name__ == '__main__':
    main()
