import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()

    # QHBoxLayout class, add controls in order from left to right. A new horizontal layout here.
    layout = QHBoxLayout()

    # Create a new button
    btn = QPushButton("Assalamu Alaykum :)")

    # Add the buttons to the layout and the layout will arrange itself
    layout.addWidget(btn)
    w.setLayout(layout)
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()
    sys.exit(app.exec())
