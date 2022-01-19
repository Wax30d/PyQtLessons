import sys
import time
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import QWidget, QPushButton, QProgressBar, QVBoxLayout, QApplication, QHBoxLayout


class Thread(QThread):
    _signal = pyqtSignal(int)

    def __init__(self):
        super(Thread, self).__init__()

    def run(self):
        for i in range(100):
            time.sleep(0.1)
            self._signal.emit(i)


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.thread = None
        self.setWindowTitle('QProgressBar')

        self.btn = QPushButton('Click me')
        self.btn.clicked.connect(self.btnFunc)

        self.pbar = QProgressBar(self)
        self.pbar.setValue(0)

        self.vbox = QVBoxLayout()
        self.vbox.addStretch(1)
        self.vbox.addWidget(self.pbar)
        self.vbox.addWidget(self.btn)

        self.hbox = QHBoxLayout()
        self.hbox.addStretch(1)
        self.hbox.addLayout(self.vbox)

        self.setLayout(self.hbox)
        self.show()

    def btnFunc(self):
        self.thread = Thread()
        self.thread._signal.connect(self.signal_accept)
        self.thread.start()
        self.btn.setEnabled(False)

    def signal_accept(self, msg):
        self.pbar.setValue(int(msg))
        if self.pbar.value() == 99:
            self.pbar.setValue(0)
            self.btn.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
