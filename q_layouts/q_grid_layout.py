import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.resize(400, 200)
        self.main_layout = QGridLayout()


        # Create Widgets
        self.btn0 = QPushButton('0')
        self.btn1 = QPushButton('1')
        self.btn2 = QPushButton('2')
        self.btn3 = QPushButton('3')
        self.btn4 = QPushButton('4')
        self.btn5 = QPushButton('5')
        self.btn6 = QPushButton('6')
        self.btn7 = QPushButton('7')
        self.btn8 = QPushButton('8')
        self.btn9 = QPushButton('9')
        self.btn_calc = QPushButton('Calculate')

        self.setup_layout()

    def setup_layout(self):
        # Setup Layout

        self.main_layout.addWidget(self.btn1, 4, 0)  # 4я строка 0 столбец
        self.main_layout.addWidget(self.btn2, 4, 1)
        self.main_layout.addWidget(self.btn3, 4, 2)
        self.main_layout.addWidget(self.btn4, 3, 0)
        self.main_layout.addWidget(self.btn5, 3, 1)
        self.main_layout.addWidget(self.btn6, 3, 2)
        self.main_layout.addWidget(self.btn7, 2, 0)
        self.main_layout.addWidget(self.btn8, 2, 1)
        self.main_layout.addWidget(self.btn9, 2, 2)
        self.main_layout.addWidget(self.btn0, 5, 1)
        self.main_layout.addWidget(self.btn_calc, 0, 0, 1, 3)  # 1 - занимать одну строку 3 - занимать три столбца

        self.setLayout(self.main_layout)










if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
