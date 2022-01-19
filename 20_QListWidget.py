import sys
from PyQt6.QtWidgets import *


class ListWidget(QListWidget):
    def clicked(self, item):
        QMessageBox.information(self, "ListWidget", "ListWidget: "+item.text(), QMessageBox.StandardButton.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    listWidget = ListWidget()

    listWidget.resize(300, 120)
    listWidget.addItem("Item 1")
    listWidget.addItem("Item 2")
    listWidget.addItem("Item 3")
    listWidget.addItem("Item 4")
    listWidget.setWindowTitle('QListwidget Example')
    listWidget.itemClicked.connect(listWidget.clicked)

    listWidget.show()
    sys.exit(app.exec())
