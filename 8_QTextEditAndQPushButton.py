from PyQt6.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton
import sys


class TextEditDemo(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("QTextEdit")
        self.resize(300, 270)

        self.textEdit = QTextEdit()
        self.btnPress1 = QPushButton("Button 1")
        self.btnPress2 = QPushButton("Button 2")

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.btnPress1)
        layout.addWidget(self.btnPress2)
        self.setLayout(layout)

        self.btnPress1.clicked.connect(self.btnPress1_Clicked)
        self.btnPress2.clicked.connect(self.btnPress2_Clicked)

    def btnPress1_Clicked(self):
        self.textEdit.setPlainText("Hello PyQt6!\nfrom Wax30d")

    def btnPress2_Clicked(self):
        self.textEdit.setHtml("<font color='red' size='6'><red>Hello PyQt6!\nHello</font>")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = TextEditDemo()
    win.show()
    sys.exit(app.exec())
