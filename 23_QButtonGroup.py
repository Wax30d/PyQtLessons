from PyQt6.QtWidgets import *
import sys

app = QApplication(sys.argv)

w = QWidget()
w.setWindowTitle("QButtonGrounp")
w.resize(300, 150)

cs1 = QRadioButton("Beginner", w)
cs1.move(130, 20)

cs2 = QRadioButton("Senior", w)
cs2.move(130, 40)

cs3 = QRadioButton("Expert", w)
cs3.move(130, 60)

cs4 = QRadioButton("Best", w)
cs4.move(130, 80)

cs_group = QButtonGroup(w)
cs_group.addButton(cs1)
cs_group.addButton(cs2)
cs_group.addButton(cs3)
cs_group.addButton(cs4)

drs1 = QRadioButton("Python", w)
drs1.move(20, 20)

drs2 = QRadioButton("Golang", w)
drs2.move(20, 40)

drs3 = QRadioButton("Java", w)
drs3.move(20, 60)

drs_group = QButtonGroup(w)
drs_group.addButton(drs1)
drs_group.addButton(drs2)
drs_group.addButton(drs3)

w.show()

if __name__ == '__main__':
    sys.exit(app.exec())
