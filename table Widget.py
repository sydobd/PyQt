import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Table Widget")
        self.setGeometry(350, 150, 500, 500)

        self.UI()

    def UI(self):
        vbox = QVBoxLayout()
        self.table = QTableWidget()
        btn = QPushButton("Get")
        self.table.setRowCount(5)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem("Name"))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem("Surname"))
        self.table.setHorizontalHeaderItem(2, QTableWidgetItem("Age"))
        # self.table.horizontalHeader().hide() # To hide horizontal header
        # self.table.verticalHeader().hide() # To hide vertical header
        self.table.setItem(0,0,QTableWidgetItem("Obaid"))
        self.table.setItem(0,1,QTableWidgetItem("Haq"))
        self.table.setItem(0,2,QTableWidgetItem("27"))
        self.table.setItem(4,2,QTableWidgetItem("31"))
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers) # stops editing field in table
        btn.clicked.connect(self.getValue)
        self.table.doubleClicked.connect(self.doubleClicked)


        vbox.addWidget(self.table)
        vbox.addWidget(btn)
        self.setLayout(vbox)
        self.show()

    def getValue(self):
        for item in self.table.selectedItems():
            print(item.text(), item.row(), item.column())

    def doubleClicked(self):
        for item in self.table.selectedItems():
            print(item.text(), item.row(), item.column())



def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()