import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.btn = QPushButton('Disable Label', self)
        self.btn.setIcon(QIcon(QPixmap('pictures/skull.png')))  # set Icon
        self.btn.setFlat(False)
        self.btn.move(50, 50)
        self.btn.clicked.connect(self.evt_btn_clicked)

        self.lbl = QLabel('Label Text', self)
        self.lbl.move(60, 100)
        self.lbl.resize(250, 356)
        font = QFont('Times New Roman', 24, 75, True)
        self.lbl.setFont(font)

    def evt_btn_clicked(self):
        if self.lbl.isEnabled():
            self.lbl.setDisabled(True)
            self.btn.setText('Enable Label')
        else:
            self.lbl.setEnabled(True)
            self.btn.setText('Disable Label')


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
