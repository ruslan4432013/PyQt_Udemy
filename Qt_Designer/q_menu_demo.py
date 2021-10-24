import sys, os
from PyQt5.QtWidgets import *  # imports section
from PyQt5.QtCore import *
from ui_to_py.menu_demo import *
import qdarkstyle
sys.path.append(r'C:\\Geekbrains\\Lessons\\PyQt_Udemy\\advanced_widget')
import q_tree_widget_homework

class MenuMain(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MenuMain, self).__init__()
        self.setupUi(self)

        # Установка layout
        self.lyt_main = QVBoxLayout()
        self.lyt_main.addWidget(self.splitter)
        self.centralwidget.setLayout(self.lyt_main)


        self.btn = QPushButton('Click me')
        self.statusbar.addPermanentWidget(self.btn)

        self.prg = QProgressBar()
        self.prg.setValue(50)
        self.prg.setStyle(QStyleFactory.create('Windows'))
        self.statusbar.addPermanentWidget(self.prg)

        self.listWidget.addItems(os.listdir('ui/'))

        self.actionOpen.triggered.connect(self.evt_open_triggered)
        self.actionQuit.triggered.connect(self.evt_quit_triggered)
        self.actionHelp.triggered.connect(self.evt_help_triggered)
        self.listWidget.itemDoubleClicked.connect(self.evt_list_widget_clicked)

    def evt_list_widget_clicked(self, lwi):
        # QMessageBox.information(self, 'File', f'You have selected {lwi.text()}')
        f = open('ui/'+lwi.text())
        self.plainTextEdit.setPlainText(f.read())

    def evt_open_triggered(self):
        s_file, s_filter = QFileDialog.getOpenFileName(self, 'Open File', 'ui/', 'Any Text Files (*.*)')
        if s_file:
            f = open(s_file)
            self.plainTextEdit.setPlainText(f.read())
        else:
            print('Action was cancelled')

    def evt_quit_triggered(self):
        sys.exit(0)

    def evt_btn_display_clicked(self):
        self.statusbar.showMessage(self.led_message.text(), self.spinBox.value())

    def evt_help_triggered(self):
        dlg_trw = q_tree_widget_homework.DlgMain()
        dlg_trw.show()
        dlg_trw.exec_()



if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    menu_main = MenuMain()  # create main GUI window
    menu_main.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
