import random
import sys
from PyQt5.QtWidgets import *  # imports section
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.resize(700, 300)

        self.lcd = QLCDNumber()
        self.lcd.setDigitCount(10)
        self.lcd.display(0)
        self.lcd.setSegmentStyle(QLCDNumber.Flat)
        self.lcd.setStyleSheet('background-color: red; color: yellow')

        self.sld = QSlider(Qt.Vertical)
        self.sld.valueChanged.connect(self.evt_sld_value_changed)
        self.sld.setTickPosition(QSlider.TicksBothSides)
        self.sld.setTickInterval(20)

        self.dial = QDial()
        self.dial.setWrapping(True)
        self.dial.setNotchesVisible(True)
        self.dial.setNotchTarget(20)
        self.dial.valueChanged.connect(self.evt_sld_value_changed)

        self.lyt_main = QVBoxLayout()
        self.lyt_main.addWidget(self.lcd)
        self.setLayout(self.lyt_main)

        self.gbx_num_sys = QGroupBox()
        self.rbt_dec = QRadioButton('Dec')
        self.rbt_bin = QRadioButton('Bin')
        self.rbt_oct = QRadioButton('Oct')
        self.rbt_hex = QRadioButton('Hex')
        self.lyt_num_sys = QHBoxLayout()
        self.lyt_num_sys.addWidget(self.rbt_dec)
        self.lyt_num_sys.addWidget(self.rbt_bin)
        self.lyt_num_sys.addWidget(self.rbt_oct)
        self.lyt_num_sys.addWidget(self.rbt_hex)
        self.gbx_num_sys.setLayout(self.lyt_num_sys)

        self.lyt_main.addWidget(self.gbx_num_sys)
        self.lyt_lcd = QHBoxLayout()
        self.lyt_lcd.addWidget(self.sld)
        self.lyt_lcd.addWidget(self.dial)
        self.lyt_lcd.addWidget(self.lcd)

        self.lyt_main.addLayout(self.lyt_lcd)

        self.rbt_dec.clicked.connect(self.evt_rbt_clicked)
        self.rbt_bin.clicked.connect(self.evt_rbt_clicked)
        self.rbt_oct.clicked.connect(self.evt_rbt_clicked)
        self.rbt_hex.clicked.connect(self.evt_rbt_clicked)


    def evt_rbt_clicked(self):
        sender = self.sender()


        if sender.text() == 'Dec':
            self.lcd.setDecMode()

        elif sender.text() == 'Bin':
            self.lcd.setBinMode()

        elif sender.text() == 'Oct':
            self.lcd.setOctMode()

        elif sender.text() == 'Hex':
            self.lcd.setHexMode()

    def evt_sld_value_changed(self, val):
        self.lcd.display(val)
        self.sld.setValue(val)
        self.dial.setValue(val)



if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
