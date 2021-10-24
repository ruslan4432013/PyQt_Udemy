import random
import sys
import time

from PyQt5.QtWidgets import *  # imports section
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')

        self.btn_add_1 = QPushButton('Add')
        self.btn_add_1.setStyleSheet(style_add_button())
        self.btn_add_2 = QPushButton('Add')
        self.btn_add_2.setStyleSheet(style_add_button())
        self.btn_delete_1 = QPushButton('Delete')
        self.btn_delete_1.setStyleSheet(style_delete_button())
        self.btn_delete_2 = QPushButton('Delete')
        self.btn_delete_2.setStyleSheet(style_delete_button())

        self.lyt_main = QVBoxLayout()
        self.lyt_main.addWidget(self.btn_add_1)
        self.lyt_main.addWidget(self.btn_add_2)
        self.lyt_main.addWidget(self.btn_delete_1)
        self.lyt_main.addWidget(self.btn_delete_2)
        self.setLayout(self.lyt_main)


def style_add_button():
    s_style = '''
        QPushButton {
            background-color: green;
            border-radius: 5px;
            padding: 10 px;
        }
        QPushButton:hover {
            background-color: green;
            border-radius: 5px;
            border: 3px solid grey;
            padding: 10 px;
        }
    '''
    return s_style


def style_delete_button():
    s_style = '''
        QPushButton {
            background-color: darkred;
            color: white;
            border-radius: 5px;
            padding: 10 px;
        }
        QPushButton:hover {
            background-color: darkred;
            color: white;
            border-radius: 5px;
            border: 3px solid grey;
            padding: 10 px;
        }
    '''
    return s_style


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
