from PyQt6.QtWidgets import (QMainWindow, QTextEdit,
                             QFileDialog, QApplication)
from PyQt6.QtGui import QIcon, QAction
from pathlib import Path
import sys


# The example shows a menubar, centrally set text edit widget, and a statusbar.
# The example is based on the QMainWindow widget because we centrally set a text edit widget.
# QWidget widget has no attribute setCentralWidget
class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.textEdit = None
        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('key.ico'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 550, 450)
        self.setWindowTitle('File dialog')
        self.show()

    def showDialog(self):
        home_dir = str(Path.home())

        # QFileDialog is a dialog that allows users to select files or directories.
        # The files can be selected for both opening and saving.
        # The menu item shows the QFileDialog which is used to select a file.
        # The contents of the file are loaded into the text edit widget.
        fname = QFileDialog.getOpenFileName(self, 'Open file', home_dir)
        """
        We pop up the QFileDialog. 
        The first string in the getOpenFileName method is the caption. 
        The second string specifies the dialog working directory. 
        We use the path module to determine the user's home directory. 
        By default, the file filter is set to All files (*).
        """

        # The selected file name is read and the contents of the file are set to the text edit widget.
        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
