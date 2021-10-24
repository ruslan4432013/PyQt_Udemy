import sys
from PyQt5.QtWidgets import *  # imports section
from ui.group_box2 import *


class DlgMain(QDialog, Ui_Dialog):
    def __init__(self):
        super(DlgMain, self).__init__()
        self.setupUi(self)
        self.setLayout(self.lyt_main)

    def evt_rbt_check_true_toggled(self, checked):
        self.gbx_checkable.setCheckable(checked)

    def evt_rbt_flat_true_toggled(self, checked):
        self.gbx_flat.setFlat(checked)

    def evt_rbt_alignment_left_toggled(self, sld):
        if sld:
            self.gbx_alignment.setAlignment(QtCore.Qt.AlignLeft)
            self.gbx_alignment.setTitle('Left Alignment')

    def evt_rbt_alignment_center_toggled(self, sld):
        if sld:
            self.gbx_alignment.setAlignment(QtCore.Qt.AlignCenter)
            self.gbx_alignment.setTitle('Center Alignment')

    def evt_rbt_alignment_right_toggled(self, sld):
        if sld:
            self.gbx_alignment.setAlignment(QtCore.Qt.AlignRight)
            self.gbx_alignment.setTitle('Right Alignment')


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
