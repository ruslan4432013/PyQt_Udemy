import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(200, 200)
        self.btn = QPushButton('Open File', self)
        self.btn.move(35, 50)
        self.btn.clicked.connect(self.evt_btn_clicked)

    def evt_btn_clicked(self):
        pass

        # QFileDialog.getOpenFileName

        # res = QFileDialog.getOpenFileName(self, 'Open File', r'C:\Geekbrains\Методички\Python Алгоритмы\Урок_3.Хэши',
        #                                   'DOC File (*.docx);;PNG File (*.png);; All File (*.*)')

        # QFileDialog.getSaveFileName

        # print(res)
        # res = QFileDialog.getSaveFileName(self, 'Save File', r'C:\Geekbrains\Методички\Python Алгоритмы\Урок_3.Хэши',
        #                                   'DOC File (*.docx);;PNG File (*.png)')
        # print(res)

        # QFileDialog.getOpenFileNames

        # res = QFileDialog.getOpenFileNames(self, 'Save File', r'C:\Geekbrains\Методички\Python Алгоритмы\Урок_3.Хэши',
        #                                   'DOC File (*.docx);;PNG File (*.png)')
        # print(res)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
