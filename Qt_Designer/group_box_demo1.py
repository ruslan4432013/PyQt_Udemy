import sys
from PyQt5.QtWidgets import *  # imports section
from PyQt5.QtCore import *
from PyQt5 import uic


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(r'ui/group_box.ui', self)

        self.rbt_check_true.toggled.connect(self.evt_rbt_check_true_toggled)
        self.rbt_flat_true.toggled.connect(self.evt_rbt_flat_true_toggled)
        self.rbt_left.toggled.connect(self.evt_rbt_alignment_left_toggled)
        self.rbt_center.toggled.connect(self.evt_rbt_alignment_center_toggled)
        self.rbt_right.toggled.connect(self.evt_rbt_alignment_right_toggled)

    def evt_rbt_check_true_toggled(self, checked):
        self.gbx_checkable.setCheckable(checked)

    def evt_rbt_flat_true_toggled(self, checked):
        self.gbx_flat.setFlat(checked)

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
