import sys
from PyQt5.QtWidgets import *  # imports section
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.resize(400, 200)

        # Create Main Widgets
        self.cmb_selector = QComboBox()
        self.cmb_selector.addItems(['General', 'Species', 'Location', 'Surveys'])
        self.cmb_selector.currentIndexChanged.connect(self.evt_cmb_selector_changed)

        self.wdg_general = QWidget()
        self.wdg_species = QWidget()
        self.wdg_location = QWidget()
        self.wdg_surveys = QWidget()

        # General Widgets
        self.lbl_nest_id = QLabel('24')
        self.dte_found = QDateTimeEdit(QDate(2017, 7, 11))
        self.dte_last = QDateTimeEdit(QDate(2021, 6, 19))
        self.chk_active = QCheckBox()

        # Species Widgets
        self.cmb_species = QComboBox()
        self.cmb_species.addItem('Rhesus macaque', 123)
        self.cmb_species.addItem('Emperor tamarin', 321)
        self.cmb_species.addItem('Other', 333)

        self.led_species = QLineEdit()
        self.spb_codes = QSpinBox()
        self.spb_codes.setValue(123)

        # Location Widgets
        self.spb_latitude = QDoubleSpinBox()
        self.spb_longitude = QDoubleSpinBox()

        # Survey Widgets
        self.lst_surveys = QListWidget()
        self.lst_surveys.addItem('02/25/2020 - INACTIVE')
        self.lst_surveys.addItem('03/21/2020 - INACTIVE')
        self.lst_surveys.addItem('05/15/2020 - INACTIVE')
        self.lst_surveys.addItem('06/10/2020 - ACTIVE')
        self.btn_add_survey = QPushButton('Add Survey')

        self.setup_layout()

    def setup_layout(self):
        # Setup Main Layout
        self.lyt_main = QHBoxLayout()
        self.lyt_left = QVBoxLayout()
        self.lyt_right = QStackedLayout()

        self.lyt_main.addLayout(self.lyt_left)
        self.lyt_main.addLayout(self.lyt_right)

        # Add Widgets To Left Layout
        self.lyt_left.addWidget(self.cmb_selector)
        self.lyt_left.addStretch()

        # Add Widgets To Right Layout
        self.lyt_right.addWidget(self.wdg_general)
        self.lyt_right.addWidget(self.wdg_species)
        self.lyt_right.addWidget(self.wdg_location)
        self.lyt_right.addWidget(self.wdg_surveys)

        # Setup General Widget
        self.lyt_general = QFormLayout()
        self.lyt_general.addRow('Nes ID', self.lbl_nest_id)
        self.lyt_general.addRow('Date Found', self.dte_found)
        self.lyt_general.addRow('Date Last Surveyed', self.dte_last)
        self.lyt_general.addRow('Currently Active', self.chk_active)
        self.wdg_general.setLayout(self.lyt_general)

        # Setup Species Widget
        self.lyt_species = QFormLayout()
        self.lyt_species.addRow('Species', self.cmb_species)
        self.lyt_species.addRow('Species', self.led_species)
        self.lyt_species.addRow('Codes', self.spb_codes)
        self.wdg_species.setLayout(self.lyt_species)

        # Setup Location Widget
        self.lyt_location = QFormLayout()
        self.lyt_location.addRow('Latitude', self.spb_latitude)
        self.lyt_location.addRow('Longitude', self.spb_longitude)
        self.wdg_location.setLayout(self.lyt_location)

        # Setup Surveys Widget
        self.lyt_surveys = QVBoxLayout()
        self.lyt_surveys.addWidget(self.lst_surveys)
        self.lyt_surveys.addWidget(self.btn_add_survey)
        self.wdg_surveys.setLayout(self.lyt_surveys)

        self.setLayout(self.lyt_main)

    def evt_cmb_selector_changed(self, idx):
        self.lyt_right.setCurrentIndex(idx)



if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
