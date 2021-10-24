import sys
from PyQt5.QtWidgets import *  # imports section
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.resize(400, 200)

        self.create_widgets()

        self.setup_layout()

    # Create UI
    def create_widgets(self):
        self.lwg_programming_topics = QListWidget()
        self.lwg_programming_topics.addItems(['Python', 'Java', 'JavaScript', 'TypeScript', 'HTML', 'CSS',
                                              'Django', 'Flask', 'Data Science', 'Machine Learning', 'Node.js',
                                              'Android Dev', 'iOS Dev', 'Bootstrap', 'Angular', 'React', 'Vue'])
        self.lwg_programming_topics.sortItems()
        self.lwg_programming_topics.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.lwg_programming_topics.itemSelectionChanged.connect(self.evt_prog_top_selection)

        self.lwg_programming_topics_selected = QListWidget()
        self.lwg_programming_topics_selected.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.lwg_programming_topics_selected.itemSelectionChanged.connect(self.evt_prog_top_selected_selection)

        self.btn_add = QPushButton('-->')
        self.btn_add.clicked.connect(self.evt_btn_add_clicked)

        self.btn_remove = QPushButton('<--')
        self.btn_remove.clicked.connect(self.evt_btn_remove_clicked)

        self.btn_enroll = QPushButton('Записаться на крусы')
        self.btn_enroll.clicked.connect(self.evt_btn_enroll_clicked)

    def setup_layout(self):
        self.lyt_main = QVBoxLayout()
        self.lyt_lists = QHBoxLayout()
        self.lyt_buttons = QVBoxLayout()

        self.add_widgets_to_lyt_lists()

        self.add_widgets_to_lyt_main()

        self.add_widgets_to_lyt_buttons()

        self.setLayout(self.lyt_main)

    def add_widgets_to_lyt_lists(self):
        self.lyt_lists.addWidget(self.lwg_programming_topics)
        self.lyt_lists.addLayout(self.lyt_buttons)
        self.lyt_lists.addWidget(self.lwg_programming_topics_selected)

    def add_widgets_to_lyt_main(self):
        self.lyt_main.addLayout(self.lyt_lists)
        self.lyt_main.addWidget(self.btn_enroll)

    def add_widgets_to_lyt_buttons(self):
        self.lyt_buttons.addStretch()
        self.lyt_buttons.addWidget(self.btn_add)
        self.lyt_buttons.addWidget(self.btn_remove)
        self.lyt_buttons.addStretch()

    # Event Handlers (slots)
    def evt_btn_add_clicked(self):
        lst_items = self.lwg_programming_topics.selectedItems()
        for item in lst_items:
            qlwi = self.lwg_programming_topics.takeItem(self.lwg_programming_topics.row(item))
            self.lwg_programming_topics_selected.addItem(qlwi)
            # self.lwg_programming_topics_selected.addItem(item.text())
        self.btn_enroll.setDefault(True)

    def evt_btn_remove_clicked(self):
        lst_items = self.lwg_programming_topics_selected.selectedItems()
        for item in lst_items:
            qlwi = self.lwg_programming_topics_selected.takeItem(self.lwg_programming_topics_selected.row(item))
            self.lwg_programming_topics.addItem(qlwi)
            self.lwg_programming_topics.sortItems()

    def evt_prog_top_selection(self):
        self.btn_add.setDefault(True)

    def evt_prog_top_selected_selection(self):
        self.btn_remove.setDefault(True)

    def evt_btn_enroll_clicked(self):
        if self.lwg_programming_topics_selected.count() == 0:
            QMessageBox.information(self, 'Topics', 'You have not selected any topics.')
        else:
            items = [self.lwg_programming_topics_selected.item(index).text()
                     for index in range(self.lwg_programming_topics_selected.count())]

            res = QMessageBox.question(self,
                                       'Сообщение',
                                       f'Вы записались на курсы: '
                                       f'"{", ".join(items)}"'
                                       f', согласны?')
            if res == QMessageBox.Yes:
                QMessageBox.information(self, 'Удачи', 'Удачного обучения')
                


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
