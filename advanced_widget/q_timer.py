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


        self.lyt_main = QHBoxLayout()
        self.setLayout(self.lyt_main)

        self.lbl_color = QLabel()
        self.pxm = QPixmap(50, 50)

        self.lst_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
        self.pxm.fill(QColor(random.choice(self.lst_colors)))
        self.lbl_color.setPixmap(self.pxm)
        self.lyt_main.addWidget(self.lbl_color)

        self.btn_start = QPushButton('Start')
        self.lyt_main.addWidget(self.btn_start)
        self.btn_start.clicked.connect(self.evt_btn_start_clicked)

        self.btn_stop = QPushButton('Stop')
        self.lyt_main.addWidget(self.btn_stop)
        self.btn_stop.clicked.connect(self.evt_btn_stop_clicked)

        self.sld = QSlider(Qt.Vertical)
        self.sld.setRange(1, 1000)
        self.sld.setValue(500)
        self.lyt_main.addWidget(self.sld)
        self.sld.valueChanged.connect(self.evt_sld_value_changed)

        self.tmr = QTimer()
        self.tmr.timeout.connect(self.evt_tmr_timeout)

    def evt_tmr_timeout(self):
        self.pxm.fill(QColor(random.choice(self.lst_colors)))
        self.lbl_color.setPixmap(self.pxm)

    def evt_btn_start_clicked(self):
        self.tmr.start(500)

    def evt_btn_stop_clicked(self):
        self.tmr.stop()

    def evt_sld_value_changed(self, val):
        self.tmr.setInterval(val)



if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
