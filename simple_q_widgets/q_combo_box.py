import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.resize(400, 200)

        self.cmbState = QComboBox(self)
        self.cmbState.move(50, 50)
        # self.cmbState.addItems(['AL', 'AR', 'MA', 'MO', 'MI'])
        self.cmbState.addItem('Alabama', 'AL')
        self.cmbState.addItem('Alaska', 'AR')
        self.cmbState.addItem('Minnesota', 'MA')
        self.cmbState.addItem('Missouri', 'MO')
        self.cmbState.addItem('Michigan', 'MI')
        self.cmbState.currentIndexChanged.connect(self.evt_cmb_state_changed)
        self.cmbState.highlighted.connect(self.evt_cmb_state_highlighted)

        self.lblAbbr = QLabel('State Abbreviation: AL', self)
        self.lblAbbr.move(170, 50)
        self.lblAbbr.resize(170, 30)

        self.cmbPosts = QComboBox(self)
        self.cmbPosts.move(50, 90)
        self.cmbPosts.resize(200, 20)
        self.cmbPosts.setEditable(True)
        self.cmbPosts.setDuplicatesEnabled(False)
        self.cmbPosts.addItem('First Post', 'First')
        self.cmbPosts.addItem('Second Post', 'Second')
        self.cmbPosts.addItem('Third Post', 'Third')
        self.cmbPosts.addItem('Forth Post', 'Forth')
        self.cmbPosts.currentIndexChanged.connect(self.evt_cmb_posts_changed)

    def evt_cmb_posts_changed(self, idx):
        if not self.cmbPosts.itemData(idx):
            s_str, b_ok = QInputDialog.getText(self, 'Your Nickname',
                                               f'Enter your nickname for {self.cmbPosts.itemText(idx)}')
            if b_ok:
                self.cmbPosts.setItemData(idx, s_str)

        QMessageBox.information(self, 'Post', f'You have selected {self.cmbPosts.itemData(idx)}')

    def evt_cmb_state_changed(self, idx):
        QMessageBox.information(self, 'ComboBox', f'You have selected {self.cmbState.itemData(idx)}')

    def evt_cmb_state_highlighted(self, idx):
        self.lblAbbr.setText(f'State Abbreviation: {self.cmbState.itemData(idx)}')


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
