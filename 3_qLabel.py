import sys
from PyQt6.QtWidgets import QVBoxLayout, QApplication, QLabel, QWidget
from PyQt6.QtGui import QPixmap


# A QLabel can be a plain label, contain links, contain colored text and even contain images.
class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText("<font color=yellow>PythonPyQt.com</font>")
        label1.setAutoFillBackground(True)

        label2.setText("<a href='#'>QLabel2</a>")

        label3.setPixmap(QPixmap("python.png"))

        label4.setOpenExternalLinks(True)
        label4.setText("<a href='https://python.org'>Python.org</a>")

        vbox = QVBoxLayout()

        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        self.setLayout(vbox)
        self.setWindowTitle('QLabel Example')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelDemo()
    main.show()
    sys.exit(app.exec())
