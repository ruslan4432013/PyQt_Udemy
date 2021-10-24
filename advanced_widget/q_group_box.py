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


        self.lyt_main = QHBoxLayout()

        self.gbx_checkable = QGroupBox('Checkable')
        self.rbt_check_true = QRadioButton('True')
        self.rbt_check_false = QRadioButton('False')
        self.lyt_checkable = QVBoxLayout()
        self.lyt_checkable.addWidget(self.rbt_check_true)
        self.lyt_checkable.addWidget(self.rbt_check_false)
        self.gbx_checkable.setLayout(self.lyt_checkable)
        self.lyt_main.addWidget(self.gbx_checkable)
        self.rbt_check_true.toggled.connect(self.evt_rbt_check_true_toggled)

        self.gbx_flat = QGroupBox('Flat')
        self.rbt_flat_true = QRadioButton('True')
        self.rbt_flat_false = QRadioButton('False')
        self.lyt_flat = QVBoxLayout()
        self.lyt_flat.addWidget(self.rbt_flat_true)
        self.lyt_flat.addWidget(self.rbt_flat_false)
        self.gbx_flat.setLayout(self.lyt_flat)
        self.lyt_main.addWidget(self.gbx_flat)
        self.rbt_flat_true.toggled.connect(self.evt_rbt_flat_true_toggled)

        self.gbx_alignment = QGroupBox('Alignment')
        self.rbt_alignment_left = QRadioButton('Align Left')
        self.rbt_alignment_center = QRadioButton('Align Center')
        self.rbt_alignment_right = QRadioButton('Align Right')
        self.lyt_alignment = QVBoxLayout()
        self.lyt_alignment.addWidget(self.rbt_alignment_left)
        self.lyt_alignment.addWidget(self.rbt_alignment_center)
        self.lyt_alignment.addWidget(self.rbt_alignment_right)
        self.gbx_alignment.setLayout(self.lyt_alignment)
        self.lyt_main.addWidget(self.gbx_alignment)

        self.rbt_alignment_left.toggled.connect(self.evt_rbt_alignment_left_toggled)
        self.rbt_alignment_center.toggled.connect(self.evt_rbt_alignment_center_toggled)
        self.rbt_alignment_right.toggled.connect(self.evt_rbt_alignment_right_toggled)


        self.setLayout(self.lyt_main)

    def evt_rbt_check_true_toggled(self, sld):
        self.gbx_checkable.setCheckable(sld)

    def evt_rbt_flat_true_toggled(self, sld):
        self.gbx_flat.setFlat(sld)

    def evt_rbt_alignment_left_toggled(self, sld):
        if sld:
            self.gbx_alignment.setAlignment(Qt.AlignLeft)
            self.gbx_alignment.setTitle('Left Alignment')

    def evt_rbt_alignment_center_toggled(self, sld):
        if sld:
            self.gbx_alignment.setAlignment(Qt.AlignCenter)
            self.gbx_alignment.setTitle('Center Alignment')


    def evt_rbt_alignment_right_toggled(self, sld):
        if sld:
            self.gbx_alignment.setAlignment(Qt.AlignRight)
            self.gbx_alignment.setTitle('Right Alignment')

if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
