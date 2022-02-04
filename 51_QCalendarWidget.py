from PyQt6.QtWidgets import (QWidget, QCalendarWidget,
                             QLabel, QApplication, QVBoxLayout)
from PyQt6.QtCore import QDate
import sys

# A QCalendarWidget provides a monthly based calendar widget.
# It allows a user to select a date in a simple and intuitive way.


# The example has a calendar widget and a label widget.
# The currently selected date is displayed in the label widget.
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.lbl = None
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout(self)

        # The QCalendarWidget is created.
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        # If we select a date from the widget, a clicked[QDate] signal is emitted.
        # We connect this signal to the user defined showDate method.
        cal.clicked[QDate].connect(self.showDate)

        vbox.addWidget(cal)

        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())

        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.show()

    def showDate(self, date):
        # We retrieve the selected date by calling the selectedDate method.
        # Then we transform the date object into string and set it to the label widget.
        self.lbl.setText(date.toString())


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
