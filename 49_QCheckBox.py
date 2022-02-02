from PyQt6.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt6.QtCore import Qt
import sys

"""
QCheckBox is a widget that has two states: on and off. 
It is a box with a label. 
Checkboxes are typically used to represent features in an application that can be enabled or disabled.
"""


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # We create a checkbox that toggles the window title.
        cb = QCheckBox('Show title', self)
        cb.move(20, 20)
        # This is a QCheckBox constructor.
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('QCheckBox')
        self.show()

    def changeTitle(self, state):
        # We connect the user defined changeTitle method to the stateChanged signal.
        # The changeTitle method toggles the window title.
        if state == Qt.CheckState.Checked.value:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
