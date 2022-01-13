from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtGui import QIcon
import sys


class PushButtonClass(QWidget):
    def __init__(self):
        super(PushButtonClass, self).__init__()

        self.closeButton = QPushButton(self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("PushButton")

        self.setGeometry(400, 400, 300, 260)
        self.closeButton.setText("Close")  # text
        self.closeButton.setIcon(QIcon("key.ico"))  # icon
        self.closeButton.setShortcut('Ctrl+D')  # shortcut key
        self.closeButton.clicked.connect(self.close)
        self.closeButton.setToolTip("Close the widget")  # Tool tip
        self.closeButton.move(100, 100)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PushButtonClass()
    ex.show()
    sys.exit(app.exec())
