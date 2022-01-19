import sys
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *


class DropInList(QListWidget):
    def __init__(self):
        super(DropInList, self).__init__()
        self.setAcceptDrops(True)

    def dropEvent(self, QDropEvent):
        source_Widget = QDropEvent.source()
        items = source_Widget.selectedItems()
        print(items)
        for i in items:
            source_Widget.takeItem(source_Widget.indexFromItem(i).row())
            self.addItem(i)
        print('drop event')


class MainWidget(QWidget):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.setWindowTitle('Drag and Drop with QListView')
        self.main_layout = QHBoxLayout()
        self.left_widget = DropInList()
        self.right_widget = QListWidget()
        pre_list = ['A', 'B', 'C']
        self.right_widget.addItems(pre_list)
        self.right_widget.setDragEnabled(True)
        self.right_widget.setDragDropOverwriteMode(False)
        self.right_widget.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.right_widget.setDefaultDropAction(Qt.DropAction.MoveAction)
        self.main_layout.addWidget(self.left_widget)
        self.main_layout.addWidget(self.right_widget)
        self.setLayout(self.main_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = MainWidget()
    m.show()
    sys.exit(app.exec())
