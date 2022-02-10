import sys
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QPainter, QColor, QFont
from PyQt6.QtCore import Qt


# We begin with drawing some Unicode text on the client area of a window.
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.text = None
        self.initUI()

    def initUI(self):
        self.text = "Shaxzodbek Sobitov Ravshan o'g'li\nInagamova Shoira"

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Drawing text')
        self.show()

    # In our example, we draw some text in Cylliric.
    # The text is vertically and horizontally aligned.
    def paintEvent(self, event):
        # Drawing is done within the paint event.
        qp = QPainter()
        qp.begin(self)

        """
        The QPainter class is responsible for all the low-level painting. 
        All the painting methods go between begin and end methods. 
        The actual painting is delegated to the drawText method.
        """
        self.drawText(event, qp)
        qp.end()

    def drawText(self, event, qp):
        # Here we define a pen and a font which are used to draw the text.
        qp.setPen(QColor(168, 34, 3))
        qp.setFont(QFont('Decorative', 10))

        """
        The drawText method draws text on the window. 
        The rect method of the paint event returns the rectangle that needs to be updated. 
        With the Qt.Alignment.AlignCenter we align the text in both dimensions.
        """
        qp.drawText(event.rect(), Qt.AlignmentFlag.AlignCenter, self.text)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
