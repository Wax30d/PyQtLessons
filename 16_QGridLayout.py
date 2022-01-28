import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout

"""
QGridLayout is the most universal layout class. 
It divides the space into rows and columns.
"""


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Created a grid of buttons.
        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+', ]

        # positions variable is a list of tuples
        positions = [(i, j) for i in range(5) for j in range(4)]

        # it zips to list
        for position, name in zip(positions, names):
            # print(*position)

            if name == '':
                continue
            button = QPushButton(name)
            # Buttons are created and added to the layout with the addWidget method.
            # sign * changes list to smth
            grid.addWidget(button, *position)

        self.move(300, 150)
        self.setWindowTitle('PyQt window')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())
