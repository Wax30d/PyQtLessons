import sys
from PyQt6 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
windows = QtWidgets.QWidget()
windows.resize(500, 500)
windows.move(100, 100)

windows.setWindowTitle('Hey Name Me')

windows.show()

sys.exit(app.exec())
