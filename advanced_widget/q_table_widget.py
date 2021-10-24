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
        self.resize(1200, 700)

        # Create Widgets
        self.trw_qt = QTreeWidget()
        self.trw_qt.setColumnCount(1)
        self.trw_qt.setHeaderLabels(['Qt Class'])
        self.trw_qt.itemDoubleClicked.connect(self.evt_trw_qt_double_clicked)

        self.wev = QWebEngineView()

        self.wev.setUrl(QUrl.fromUserInput('https://doc.qt.io/qt-5/'))

        self.btn_back = QPushButton('Back')
        self.btn_back.clicked.connect(self.wev.back)

        self.btn_home = QPushButton('Home')
        self.btn_home.clicked.connect(self.evt_btn_home_clicked)

        self.btn_forward = QPushButton('Forward')
        self.btn_forward.clicked.connect(self.wev.forward)

        self.btn_history = QPushButton('Show History')
        self.btn_history.clicked.connect(self.evt_btn_history_clicked)

        self.tbl_history = QTableWidget(3, 4)
        self.tbl_history.hide()
        self.tbl_history.setColumnWidth(0, 200)
        self.tbl_history.setColumnWidth(1, 200)
        self.tbl_history.setColumnWidth(2, 300)
        self.tbl_history.setColumnWidth(3, 200)
        self.tbl_history.setHorizontalHeaderLabels(['Class', 'Module', 'URL', 'Last Visited'])
        self.tbl_history.cellClicked.connect(self.evt_tbl_history_clicked)

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

        self.lyt_wev_btn = QHBoxLayout()
        self.lyt_wev_btn.addWidget(self.btn_back)
        self.lyt_wev_btn.addWidget(self.btn_home)
        self.lyt_wev_btn.addWidget(self.btn_forward)
        self.lyt_wev_btn.addWidget(self.btn_history)

        self.lyt_wev = QVBoxLayout()
        self.lyt_wev.addWidget(self.wev)
        self.lyt_wev.addLayout(self.lyt_wev_btn)
        self.lyt_wev.addWidget(self.tbl_history)

        self.lyt_main = QHBoxLayout()
        self.lyt_main.addLayout(self.lyt_left, 1)
        self.lyt_main.addLayout(self.lyt_wev, 5)

        self.setLayout(self.lyt_main)

    # Custom Slots
    def evt_trw_qt_double_clicked(self, twi, col):
        url = f'https://doc.qt.io/qt-5/{twi.text(0).lower()}.html'
        self.wev.setUrl(QUrl.fromUserInput(url))
        self.refresh_history()

    def evt_btn_home_clicked(self):
        url = f'https://doc.qt.io/qt-5/'
        self.wev.setUrl(QUrl.fromUserInput(url))

    def evt_btn_history_clicked(self):
        if self.tbl_history.isHidden():
            self.tbl_history.show()
            self.btn_history.setText('Hide History')
            self.refresh_history()

        else:
            self.tbl_history.hide()
            self.btn_history.setText('Show History')

    def evt_tbl_history_clicked(self, row, col):
        url = self.tbl_history.item(row, 2).text()
        self.wev.setUrl(QUrl.fromUserInput(url))
        self.refresh_history()




    def refresh_history(self):
        self.tbl_history.clear()
        self.tbl_history.setHorizontalHeaderLabels(['Class', 'Module', 'URL', 'Last Visited'])
        # Fill table
        history = self.wev.history()
        cnt = history.count()
        self.tbl_history.setRowCount(cnt)
        for idx in range(cnt):
            item = history.itemAt(idx)
            if len(item.title().split(' | ')) == 2:
                s_class, s_module = item.title().split(' | ')
                self.tbl_history.setItem(cnt - idx - 1, 0, QTableWidgetItem(s_class))
                self.tbl_history.setItem(cnt - idx - 1, 1, QTableWidgetItem(s_module))
                self.tbl_history.setItem(cnt - idx - 1, 2, QTableWidgetItem(item.url().toString()))
                self.tbl_history.setItem(cnt - idx - 1, 3, QTableWidgetItem(item.lastVisited().toString()))

if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
