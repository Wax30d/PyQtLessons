from PyQt6.QtWidgets import *
import sys

app = QApplication(sys.argv)

w = QWidget()
w.setWindowTitle("QButtonGroup")
w.resize(300, 150)

# Create group 1 QRadioButton button
cs1 = QRadioButton("Super Cup", w)
cs1.move(80, 20)

cs2 = QRadioButton("Big Cup", w)
cs2.move(80, 40)

cs3 = QRadioButton("Medium Cup", w)
cs3.move(80, 60)

cs4 = QRadioButton("Small Cup", w)
cs4.move(80, 80)

# Create a key group and add keys
cs_group = QButtonGroup(w)
cs_group.addButton(cs1)
cs_group.addButton(cs2)
cs_group.addButton(cs3)
cs_group.addButton(cs4)

# Set cs_group to not be mutually exclusive
cs_group.setExclusive(False)

w.show()

if __name__ == '__main__':
    sys.exit(app.exec())
