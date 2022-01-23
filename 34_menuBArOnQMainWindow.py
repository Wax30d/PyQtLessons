import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QIcon, QAction


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        """
        QAction is an abstraction for actions performed with a menubar, toolbar, or with a custom keyboard shortcut.
        In the above three lines, we create an action with a specific icon and an 'Exit' label.
        Furthermore, a shortcut is defined for this action.
        The third line creates a status tip which is shown in the statusbar when
         we hover a mouse pointer over the menu item.
        """
        exitAct = QAction(QIcon('python.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')

        """
        When we select this particular action, a triggered signal is emitted. 
        The signal is connected to the quit method of the QApplication widget. 
        This terminates the application.
        """
        exitAct.triggered.connect(QApplication.instance().quit)

        self.statusBar()

        """
        We create a menubar with one menu. 
        This menu contains one action which terminates the application if selected. 
        A statusbar is created as well. 
        The action is accessible with the Ctrl+Q shortcut.
        The menuBar method creates a menubar. We create a file menu with addMenu and add the action with addAction.
        """
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Simple menu')


def main():
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
