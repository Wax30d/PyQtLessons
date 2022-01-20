from PyQt6.QtWidgets import *

import sys

app = QApplication(sys.argv)

w = QWidget()
w.setWindowTitle("QButtonGrounp")
w.resize(300, 150)

# Create 4 QRadioButton buttons
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
cs_group.addButton(cs1, 1)
cs_group.addButton(cs2, 2)
cs_group.addButton(cs3, 3)
cs_group.addButton(cs4, 4)


# Define the slot function and print the received parameters
def slot(object):
    print("Key was pressed, id is:", cs_group.id(object))


# connects the slot function and makes the argument of the band int type
cs_group.buttonClicked.connect(slot)
w.show()

if __name__ == '__main__':
    sys.exit(app.exec())
