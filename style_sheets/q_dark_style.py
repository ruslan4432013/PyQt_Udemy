import sys
from PyQt5.QtWidgets import *  # imports section
import qdarkstyle

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.dark = False

        self.gbx_dark_style = QGroupBox('Dark Style')
        self.gbx_dark_style.setCheckable(True)


        self.rbt_normal = QRadioButton('Normal')
        self.rbt_normal.setChecked(True)
        self.rbt_normal.setStyleSheet(style_radio_button(self.dark))
        self.rbt_normal.toggled.connect(self.evt_rbt_normal_toggled)
        self.rbt_dark = QRadioButton('Dark Style')
        self.rbt_dark.setStyleSheet(style_radio_button(self.dark))

        self.txt_style = QPlainTextEdit()

        self.lyt_buttons = QVBoxLayout()
        self.lyt_buttons.addWidget(self.rbt_normal)
        self.lyt_buttons.addWidget(self.rbt_dark)

        self.lyt_group_box = QHBoxLayout()
        self.lyt_group_box.addLayout(self.lyt_buttons)
        self.lyt_group_box.addWidget(self.txt_style)

        self.gbx_dark_style.setLayout(self.lyt_group_box)

        self.lyt_main = QHBoxLayout()
        self.lyt_main.addWidget(self.gbx_dark_style)
        self.lyt_main.addLayout(self.lyt_group_box)

        self.setLayout(self.lyt_main)

    def evt_rbt_normal_toggled(self, checked):
        if checked:
            app.setStyleSheet('')
            self.dark = False

        else:
            app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
            self.dark = True
        self.txt_style.setPlainText(app.styleSheet())
        self.rbt_normal.setStyleSheet(style_radio_button(self.dark))
        self.rbt_dark.setStyleSheet(style_radio_button(self.dark))

def style_radio_button(dark):
    if dark:
        s_style = '''
        QRadioButton {
            background-color: white;
            color: black;
            padding: 10px;
        }
        QRadioButton::indicator {
            background-color: white;
            color: black;
            padding: 10px;
        }
    '''
    else:
        s_style = '''
            QRadioButton {
                background-color: black;
                color: white;
                padding: 10px;
            }
            QRadioButton::indicator {
                background-color: black;
                color: white;
                padding: 10px;
            }
        '''
    return s_style



if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
