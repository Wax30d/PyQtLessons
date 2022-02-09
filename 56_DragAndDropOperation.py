"""
Drag & drop operations.

In computer graphical user interfaces,
drag-and-drop is the action of (or support for the action of) clicking on a virtual object
and dragging it to a different location or onto another virtual object.
In general, it can be used to invoke many kinds of actions,
or create various types of associations between two abstract objects.

Drag and drop is part of the graphical user interface.
Drag and drop operations enable users to do complex things intuitively.

Usually, we can drag and drop two things: data or some graphical objects.
If we drag an image from one application to another, we drag and drop binary data.
If we drag a tab in Firefox and move it to another place, we drag and drop a graphical component.

QDrag.
QDrag provides support for MIME-based drag and drop data transfer.
It handles most of the details of a drag and drop operation.
The transferred data is contained in a QMimeData object.
"""

import sys

from PyQt6.QtWidgets import (QPushButton, QWidget,
                             QLineEdit, QApplication)

"""
In order to drop text on the QPushButton widget, we must reimplement some methods. 
Therefore, we create our own Button class which inherits from the QPushButton class.
"""


# We have a QLineEdit and a QPushButton.
# We drag plain text from the line edit widget and drop it onto the button widget.
# The button's label will change.
class Button(QPushButton):

    def __init__(self, title, parent):
        super().__init__(title, parent)

        # We enable drop events for the widget with setAcceptDrops.
        self.setAcceptDrops(True)

    # First, we reimplement the dragEnterEvent method.
    # We inform about the data type that we accept.
    # In our case it is plain text.
    def dragEnterEvent(self, e):

        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):

        self.setText(e.mimeData().text())


# The example presents a simple drag & drop operation.
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # The QLineEdit widget has a built-in support for drag operations.
        # All we need to do is to call the setDragEnabled method to activate it.
        edit = QLineEdit('', self)
        edit.setDragEnabled(True)
        # Drag meaning "ushlab kotarib turish"
        # Drop meaning "ushlab turgan holda tushirish"
        edit.move(30, 65)

        button = Button("Button", self)
        button.move(190, 65)

        self.setWindowTitle('Simple drag and drop')
        self.setGeometry(300, 300, 300, 150)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec()


if __name__ == '__main__':
    main()
