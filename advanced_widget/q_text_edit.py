import random
import sys
from PyQt5.QtWidgets import *  # imports section
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')

        self.lyt_main = QVBoxLayout()
        self.setLayout(self.lyt_main)

        self.ted = QTextEdit()
        self.ted.setText('012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789')
        self.lyt_main.addWidget(self.ted)

        self.btn_background = QPushButton('Set Background Color')
        self.lyt_main.addWidget(self.btn_background)
        self.btn_background.clicked.connect(self.evt_btn_background_clicked)

        self.btn_html = QPushButton('Add HTML')
        self.lyt_main.addWidget(self.btn_html)
        self.btn_html.clicked.connect(self.evt_btn_html_clicked)


        cur_text = self.ted.textCursor()
        cur_text.setPosition(15, QTextCursor.MoveAnchor)
        cur_text.setPosition(25, QTextCursor.KeepAnchor)
        self.ted.setTextCursor(cur_text)
        self.ted.setTextColor(QColor('green'))

    def evt_btn_background_clicked(self):
        clr = QColorDialog.getColor(QColor('black'))
        self.ted.setTextBackgroundColor(QColor(clr))
        self.ted.setFontPointSize(20)


    def evt_btn_html_clicked(self):
        html = '''
        <h1>Rainbow Colors</h1>
        <ul>
            <li>Red</li>
            <li><b>Bold Orange</b></li>
            <li>Yellow</li>
            <li><i>Italic Green</i></li>
            <li>Blue</li>
            <li>Indigo</li>
            <li>Violet</li>
        </ul>        
        '''
        self.ted.setText(html)

if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
