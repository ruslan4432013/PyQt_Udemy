import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(200, 200)
        self.btn = QPushButton('Show Input', self)
        self.btn.move(35, 50)
        self.btn.clicked.connect(self.evt_btn_clicked)

    def evt_btn_clicked(self):
        pass

        # QInputDialog.getText

        # s_name, b_ok = QInputDialog.getText(self, 'Title', 'Enter your name:')
        # if b_ok:
        #     QMessageBox.information(self, 'Name', 'Your name is ' + s_name)
        # else:
        #     QMessageBox.critical(self, 'Canceled', 'User have clicked cancel')

        # QInputDialog.getInt

        # i_age, b_ok = QInputDialog.getInt(self, 'Title', 'Enter your age:', 18, 18, 65, 1)
        # if b_ok:
        #     QMessageBox.information(self, 'Age', f'Your age is {i_age}')
        # else:
        #     QMessageBox.critical(self, 'Canceled', 'User have clicked cancel')

        # QInputDialog.getDouble

        # d_high, b_ok = QInputDialog.getDouble(self, 'Title', 'Enter your age:', 1.70, 0.50, 2.50, 2)
        # if b_ok:
        #     QMessageBox.information(self, 'Height', f'Your height is {d_high}')
        # else:
        #     QMessageBox.critical(self, 'Canceled', 'User have clicked cancel')

        # QInputDialog.getItem

        # colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
        # s_color, b_ok = QInputDialog.getItem(self, 'Title', 'Enter your favorite color:', colors, editable=True)
        # if b_ok:
        #     QMessageBox.information(self, 'Height', f'Your favorite color is {s_color}')
        # else:
        #     QMessageBox.critical(self, 'Canceled', 'User have clicked cancel')

if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.setWindowTitle('Калькулятор')
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
