import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QIcon, QAction


# Toolbars provide quick access to the most frequently used commands.
class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.toolbar = None
        self.initUI()

    def initUI(self):
        """
        we create a simple toolbar.
        The toolbar has one tool action, an exit action which terminates the application when triggered.
        you can move toolbar.
        we create an action object.
        The object has a label, icon, and a shortcut.
        A quit method of the QApplication is connected to the triggered signal.
        """
        exitAct = QAction(QIcon('cat.gif'), 'ggg', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(QApplication.instance().quit)

        """
        The toolbar is created with the addToolBar method. 
        We add an action object to the toolbar with addAction.
        """
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Toolbar')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
