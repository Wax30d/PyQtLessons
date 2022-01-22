# Here we provide the necessary imports.
# The basic widgets are located in PyQt6.QtWidgets module.
import sys
from PyQt6.QtWidgets import QApplication, QWidget


# Code example shows a small window on the screen.
def main():

    """
    Every PyQt6 application must create an application object.
    The sys.argv parameter is a list of arguments from a command line.
    Python scripts can be run from the shell.
    It is a way how we can control the startup of our scripts.
    """
    app = QApplication(sys.argv)

    """
    The QWidget widget is the base class of all user interface objects in PyQt6. 
    We provide the default constructor for QWidget. 
    The default constructor has no parent. 
    A widget with no parent is called a window.
    """
    w = QWidget()

    # The resize method resizes the widget.
    # It is 250px wide and 150px high.
    w.resize(250, 200)

    # The move method moves the widget to a position on the screen at x=300, y=300 coordinates.
    w.move(300, 300)

    # We set the title of the window with setWindowTitle.
    # The title is shown in the titlebar.
    w.setWindowTitle('Simple')

    # The show method displays the widget on the screen.
    # A widget is first created in memory and later shown on the screen.
    w.show()

    """
    Finally, we enter the mainloop of the application. 
    The event handling starts from this point. 
    The mainloop receives events from the window system and dispatches them to the application widgets. 
    The mainloop ends if we call the exit method or the main widget is destroyed. 
    The sys.exit method ensures a clean exit. The environment will be informed how the application ended.
    """
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
