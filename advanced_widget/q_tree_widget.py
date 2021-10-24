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

        # Create Widgets
        self.trw_qt = QTreeWidget()
        self.trw_qt.setColumnCount(3)
        self.trw_qt.setHeaderLabels(['Qt Class', 'Methods', 'Signals'])
        self.trw_qt.itemDoubleClicked.connect(self.evt_trw_qt_double_clicked)

        # Populate Tree

        # Create Top Level Items
        self.twi_qwidget = QTreeWidgetItem(self.trw_qt, ['QWidget Module'])
        self.twi_qgui = QTreeWidgetItem(self.trw_qt, ['QGui Module'])
        self.twi_qcore = QTreeWidgetItem(self.trw_qt, ['QCore Module'])

        # Add SubItems To QWidget Module
        lst_qwidget = ['QDialog', 'QLabel', 'QLineEdit', 'QGroupBox', 'QFrame']
        for cls in lst_qwidget:
            self.twi_qwidget.addChild(QTreeWidgetItem([cls, str(random.randrange(25)), str(random.randrange(10))]))

        # Add SubItems To QGui Module
        lst_qgui = ['QBitmap', 'QColor', 'QFont', 'QIcon', 'QFrame']
        for cls in lst_qgui:
            self.twi_qgui.addChild(QTreeWidgetItem([cls, str(random.randrange(25)), str(random.randrange(10))]))

        # Add SubItems To QCore Module
        lst_qcore = ['QThread', 'QDateTime', 'QPixmap', 'QUrl', 'QFile']
        for cls in lst_qcore:
            self.twi_qcore.addChild(QTreeWidgetItem([cls, str(random.randrange(25)), str(random.randrange(10))]))

        # Add SubItems To QDialog SubItem
        twi_qdialog = self.trw_qt.findItems('QDialog', Qt.MatchRecursive)[0]
        lst_qdialog = ['QFileDialog', 'QColorDialog', 'QFontDialog', 'QMessageBox']
        for cls in lst_qdialog:
            twi_qdialog.addChild(QTreeWidgetItem([cls, str(random.randrange(25)), str(random.randrange(10))]))

        # Sort trwQt
        self.trw_qt.sortItems(0, Qt.AscendingOrder)

        # Resize the first column
        self.trw_qt.setColumnWidth(0, 200)

        # Expand QWidget by default
        self.trw_qt.expandItem(self.twi_qwidget)

        # Setup Layout
        self.lyt_main = QVBoxLayout()
        self.lyt_main.addWidget(self.trw_qt)

        self.setLayout(self.lyt_main)

    # Custom Slots
    def evt_trw_qt_double_clicked(self, twi, col):
        QMessageBox.information(self, 'Qt Classes', f'You have clicked on the {twi.text(0)} class')


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
