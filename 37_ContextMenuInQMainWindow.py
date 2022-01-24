import sys
from PyQt6.QtWidgets import QMainWindow, QMenu, QApplication

"""
A context menu, also called a popup menu, is a list of commands that appears under some context. 
For example, in a Opera web browser when we right click on a web page, we get a context menu. 
Here we can reload a page, go back, or view a page source. 
If we right click on a toolbar, we get another context menu for managing toolbars.
"""


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Context menu')
        self.show()

    def contextMenuEvent(self, event):
        cmenu = QMenu(self)

        newAct = cmenu.addAction("New")
        openAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")

        """
        The context menu is displayed with the exec method. 
        The get the coordinates of the mouse pointer from the event object. 
        The mapToGlobal method translates the widget coordinates to the global screen coordinates.
        """
        action = cmenu.exec(self.mapToGlobal(event.pos()))

        # If the action returned from the context menu equals to quit action,
        # we terminate the application.
        if action == quitAct:
            QApplication.instance().quit()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
