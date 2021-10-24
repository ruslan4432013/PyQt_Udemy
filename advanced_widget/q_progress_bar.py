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
        self.resize(700, 300)


        self.prb = QProgressBar()


        self.btn_start = QPushButton('Start')
        self.btn_start.clicked.connect(self.evt_btn_start_clicked)

        self.lyt_main = QVBoxLayout()
        self.lyt_main.addWidget(self.prb)
        self.lyt_main.addWidget(self.btn_start)
        self.setLayout(self.lyt_main)

    def evt_btn_start_clicked(self):
        for i in range(101):
            time.sleep(0.1)
            self.prb.setValue(i)
            app.processEvents()


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
