from PyQt6.QtWidgets import QApplication, QToolButton, QMainWindow
from PyQt6.QtGui import QIcon
import sys


class ToolButtonClass(QMainWindow):

    def __init__(self):
        super(ToolButtonClass, self).__init__()

        self.detailsButton = QToolButton()
        self.toolbar = self.addToolBar("toolBar")

        self.initUI()

    def initUI(self):
        self.setWindowTitle("ToolButton")
        self.setGeometry(400, 400, 300, 260)

        self.detailsButton.setCheckable(True)
        self.detailsButton.setChecked(False)
        self.detailsButton.setIcon(QIcon("key.ico"))
        self.detailsButton.setAutoRaise(True)
        self.detailsButton.clicked.connect(self.showDetail)

        self.toolbar.addWidget(self.detailsButton)

    def showDetail(self):
        if self.detailsButton.isChecked():
            self.statusBar().showMessage("Show Detail....")
        else:
            self.statusBar().showMessage("Close Detail....")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ToolButtonClass()
    ex.show()
    sys.exit(app.exec())
