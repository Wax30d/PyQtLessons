import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QAction

"""
The code example creates a View menu with one action. 
The action shows or hides a statusbar. 
When the statusbar is visible, the menu item is checked.
"""


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.statusbar = None
        self.initUI()

    def initUI(self):

        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')

        menubar = self.menuBar()
        viewMenu = menubar.addMenu('View')

        # With the checkable option we create a checkable menu.
        viewStatAct = QAction('View statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View statusbar from Wax30d')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)

        viewMenu.addAction(viewStatAct)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Check menu')

    def toggleMenu(self, state):
        # Depending on the state of the action, we show or hide the statusbar.
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
