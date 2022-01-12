import sys
from PyQt6.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QGridLayout, QApplication


class QLabelBuddy(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QLabel Example')
        self.setFixedWidth(250)

        nameLabel = QLabel('&Name', self)
        nameLineEdit = QLineEdit(self)
        nameLabel.setBuddy(nameLineEdit)

        passwordLabel = QLabel('&Password', self)
        passwordLineEdit = QLineEdit(self)
        passwordLabel.setBuddy(passwordLineEdit)

        btnOK = QPushButton('&OK')
        btnCancel = QPushButton('&Cancel')

        mainLayout = QGridLayout(self)
        mainLayout.addWidget(nameLabel)
        mainLayout.addWidget(nameLineEdit)

        mainLayout.addWidget(passwordLabel)
        mainLayout.addWidget(passwordLineEdit)

        mainLayout.addWidget(btnOK)
        mainLayout.addWidget(btnCancel)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelBuddy()
    main.show()
    sys.exit(app.exec())
