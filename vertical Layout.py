import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vertical Box Layout")
        self.setGeometry(350, 150, 500, 500)

        self.UI()

    def UI(self):
        vbox = QVBoxLayout()
        button1 = QPushButton("SAVE")
        button2 = QPushButton("EXIT")

        vbox.addWidget(button1)
        vbox.addWidget(button2)
        # vbox.addStretch() #Push buttons to top if use before
        self.setLayout(vbox)
        # vbox.addStretch() #Push buttons to bottom if use after
        self.show()


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()