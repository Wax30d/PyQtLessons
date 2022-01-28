import sys
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication

"""
We create a window in which we have three labels, two line edits and one text edit widget. 
The layout is done with the QGridLayout.
"""


# Widgets can span multiple columns or rows in a grid.
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1, 1, 9)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1, 1, 1)

        grid.addWidget(review, 3, 0)
        # If we add a widget to a grid, we can provide row span and column span of the widget.
        grid.addWidget(reviewEdit, 3, 1, 9, 9)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
