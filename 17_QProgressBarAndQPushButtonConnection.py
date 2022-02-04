from PyQt6.QtWidgets import (QWidget, QProgressBar,
                             QPushButton, QApplication)
from PyQt6.QtCore import QBasicTimer
import sys

"""
A progress bar is a widget that is used when we process lengthy tasks. 
It is animated so that the user knows that the task is progressing. 
The QProgressBar widget provides a horizontal or a vertical progress bar in PyQt6 toolkit. 
The programmer can set the minimum and maximum value for the progress bar. 
The default values are 0 and 99.
"""


"""
In our example we have a horizontal progress bar and a push button. 
The push button starts and stops the progress bar.
"""


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.step = None
        self.timer = None
        self.btn = None
        self.pbar = None

        self.initUI()

    def initUI(self):

        # This is a QProgressBar constructor.
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(40, 40, 200, 25)

        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        # To activate the progress bar, we use a timer object.
        self.timer = QBasicTimer()
        self.step = 0

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QProgressBar')
        self.show()

    # Each QObject and its descendants have a timerEvent event handler.
    # In order to react to timer events, we reimplement the event handler.
    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    # Inside the doAction method, we start and stop the timer.
    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            # To launch a timer event, we call its start method.
            # This method has two parameters: the timeout and the object which receive the events.
            self.timer.start(100, self)
            self.btn.setText('Stop')


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
