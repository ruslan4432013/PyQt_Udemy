# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'example.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dlg_main(object):
    def setupUi(self, dlg_main):
        dlg_main.setObjectName("dlg_main")
        dlg_main.resize(514, 638)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        dlg_main.setFont(font)
        self.grb_dialog = QtWidgets.QGroupBox(dlg_main)
        self.grb_dialog.setGeometry(QtCore.QRect(0, 0, 511, 371))
        self.grb_dialog.setAlignment(QtCore.Qt.AlignCenter)
        self.grb_dialog.setFlat(False)
        self.grb_dialog.setCheckable(True)
        self.grb_dialog.setChecked(True)
        self.grb_dialog.setObjectName("grb_dialog")
        self.lbl_1 = QtWidgets.QLabel(self.grb_dialog)
        self.lbl_1.setGeometry(QtCore.QRect(10, 30, 91, 31))
        self.lbl_1.setObjectName("lbl_1")
        self.horizontalSlider = QtWidgets.QSlider(self.grb_dialog)
        self.horizontalSlider.setGeometry(QtCore.QRect(30, 230, 160, 16))
        self.horizontalSlider.setProperty("value", 50)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.grb_dialog)
        self.dateTimeEdit.setGeometry(QtCore.QRect(0, 130, 194, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.tableWidget = QtWidgets.QTableWidget(self.grb_dialog)
        self.tableWidget.setGeometry(QtCore.QRect(230, 60, 256, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.lcdNumber = QtWidgets.QLCDNumber(self.grb_dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(20, 270, 191, 81))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lineEdit = QtWidgets.QLineEdit(dlg_main)
        self.lineEdit.setGeometry(QtCore.QRect(0, 380, 511, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(dlg_main)
        self.label.setGeometry(QtCore.QRect(0, 415, 511, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(dlg_main)
        self.horizontalSlider.valueChanged['int'].connect(self.lcdNumber.display)
        self.lineEdit.textChanged['QString'].connect(self.label.setText)
        QtCore.QMetaObject.connectSlotsByName(dlg_main)
        dlg_main.setTabOrder(self.horizontalSlider, self.tableWidget)
        dlg_main.setTabOrder(self.tableWidget, self.dateTimeEdit)
        dlg_main.setTabOrder(self.dateTimeEdit, self.grb_dialog)

    def retranslateUi(self, dlg_main):
        _translate = QtCore.QCoreApplication.translate
        dlg_main.setWindowTitle(_translate("dlg_main", "My GUI"))
        self.grb_dialog.setTitle(_translate("dlg_main", "My GUI Widgets"))
        self.lbl_1.setText(_translate("dlg_main", "First Widget"))
        self.lineEdit.setPlaceholderText(_translate("dlg_main", "input something here"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dlg_main = QtWidgets.QDialog()
    ui = Ui_dlg_main()
    ui.setupUi(dlg_main)
    dlg_main.show()
    sys.exit(app.exec_())
