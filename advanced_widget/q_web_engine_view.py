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
        self.resize(1200, 800)

        self.lyt_main = QVBoxLayout()
        self.setLayout(self.lyt_main)

        self.wev = QWebEngineView()
        self.lyt_main.addWidget(self.wev)

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
        self.wev.setHtml(html)

        self.led_class = QLineEdit('QWebChannel')
        self.lyt_main.addWidget(self.led_class)

        self.btn_html = QPushButton('Go To The Page')
        self.lyt_main.addWidget(self.btn_html)
        self.btn_html.clicked.connect(self.evt_btn_html_clicked)

        self.btn_local_html = QPushButton('Load HTML File')
        self.lyt_main.addWidget(self.btn_local_html)
        self.btn_local_html.clicked.connect(self.evt_btn_local_html_clicked)


    def evt_btn_html_clicked(self):
        url = f'https://doc.qt.io/qt-5/{self.led_class.text().lower()}.html'
        self.wev.setUrl(QUrl.fromUserInput(url))

    def evt_btn_local_html_clicked(self):
        url = r'C:\Geekbrains\Lessons\PyQt_Udemy\advanced_wiget\html\test_text_browser.html'
        self.wev.setUrl(QUrl.fromLocalFile(url))

if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
