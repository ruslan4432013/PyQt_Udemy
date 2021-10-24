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
        self.resize(900, 600)

        # Create Widgets
        self.trw_qt = QTreeWidget()
        self.trw_qt.setColumnCount(1)
        self.trw_qt.setHeaderLabels(['Qt Class'])
        self.trw_qt.itemDoubleClicked.connect(self.evt_trw_qt_double_clicked)

        self.led_class = QLineEdit('QWebChannel')

        self.wev = QWebEngineView()

        self.wev.setUrl(QUrl.fromUserInput('https://doc.qt.io/qt-5/'))

        self.btn_back = QPushButton('Back')
        self.btn_back.clicked.connect(self.wev.back)

        self.btn_home = QPushButton('Home')
        self.btn_home.clicked.connect(self.evt_btn_home_clicked)

        self.btn_forward = QPushButton('Forward')
        self.btn_forward.clicked.connect(self.wev.forward)

        self.history = []

        # Populate Tree

        # Create Top Level Items
        self.twi_qwidget = QTreeWidgetItem(self.trw_qt, ['QWidget Module'])
        self.twi_qgui = QTreeWidgetItem(self.trw_qt, ['QGui Module'])
        self.twi_qcore = QTreeWidgetItem(self.trw_qt, ['QCore Module'])

        # Add SubItems To QWidget Module
        lst_qwidget = ['QDialog', 'QLabel', 'QLineEdit', 'QGroupBox', 'QFrame']
        for cls in lst_qwidget:
            self.twi_qwidget.addChild(QTreeWidgetItem([cls]))

        # Add SubItems To QGui Module
        lst_qgui = ['QBitmap', 'QColor', 'QFont', 'QIcon', 'QFrame']
        for cls in lst_qgui:
            self.twi_qgui.addChild(QTreeWidgetItem([cls]))

        # Add SubItems To QCore Module
        lst_qcore = ['QThread', 'QDateTime', 'QPixmap', 'QUrl', 'QFile']
        for cls in lst_qcore:
            self.twi_qcore.addChild(QTreeWidgetItem([cls]))

        # Add SubItems To QDialog SubItem
        twi_qdialog = self.trw_qt.findItems('QDialog', Qt.MatchRecursive)[0]
        lst_qdialog = ['QFileDialog', 'QColorDialog', 'QFontDialog', 'QMessageBox']
        for cls in lst_qdialog:
            twi_qdialog.addChild(QTreeWidgetItem([cls]))

        # Sort trwQt
        self.trw_qt.sortItems(0, Qt.AscendingOrder)

        # Resize the first column
        self.trw_qt.setColumnWidth(0, 200)

        # Expand QWidget by default
        self.trw_qt.expandItem(self.twi_qwidget)

        # Setup Layout

        self.lyt_left = QVBoxLayout()
        self.lyt_left.addWidget(self.trw_qt)

        self.lyt_right_btn = QHBoxLayout()
        self.lyt_right_btn.addWidget(self.btn_back)
        self.lyt_right_btn.addWidget(self.btn_home)
        self.lyt_right_btn.addWidget(self.btn_forward)

        self.lyt_right = QVBoxLayout()
        self.lyt_right.addWidget(self.wev)
        self.lyt_right.addWidget(self.led_class)
        self.lyt_right.addLayout(self.lyt_right_btn)

        self.lyt_main = QHBoxLayout()
        self.lyt_main.addLayout(self.lyt_left)
        self.lyt_main.addStretch()
        self.lyt_main.addLayout(self.lyt_right)

        self.setLayout(self.lyt_main)

    # Custom Slots
    def evt_trw_qt_double_clicked(self, twi, col):
        url = f'https://doc.qt.io/qt-5/{twi.text(0).lower()}.html'
        self.wev.setUrl(QUrl.fromUserInput(url))

    def evt_btn_home_clicked(self):
        url = f'https://doc.qt.io/qt-5/'
        self.wev.setUrl(QUrl.fromUserInput(url))


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
