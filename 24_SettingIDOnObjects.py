from PyQt6.QtWidgets import *
import sys

# QButtonGroup can quickly set an ID for a button when adding a button
app = QApplication(sys.argv)

w = QWidget()
w.setWindowTitle("QButtonGrounp")
w.resize(300, 150)

cs1 = QRadioButton("Answer A", w)
cs1.move(20, 20)
cs1.setChecked(True)

cs2 = QRadioButton("Answer B", w)
cs2.move(20, 40)

cs_group = QButtonGroup(w)
cs_group.addButton(cs1, 1)  # ID 1
cs_group.addButton(cs2, 2)  # ID 2

print(cs_group.buttons())
print(cs_group.button(2))  # ID=2
print(cs_group.checkedButton())

w.show()

if __name__ == '__main__':
    sys.exit(app.exec())
