# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/hsierra/OneDrive/myproject/project-payroll/forminput.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_forminput(object):
    def setupUi(self, forminput):
        forminput.setObjectName("forminput")
        forminput.resize(846, 677)
        self.centralwidget = QtWidgets.QWidget(forminput)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 41, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 60, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 130, 60, 16))
        self.label_4.setObjectName("label_4")
        self.lineEditnama = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditnama.setGeometry(QtCore.QRect(150, 30, 211, 21))
        self.lineEditnama.setObjectName("lineEditnama")
        self.comboBoxdivisi = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxdivisi.setGeometry(QtCore.QRect(150, 90, 211, 26))
        self.comboBoxdivisi.setObjectName("comboBoxdivisi")
        self.comboBoxdivisi.addItem("")
        self.comboBoxdivisi.addItem("")
        self.comboBoxdivisi.addItem("")
        self.comboBoxdivisi.addItem("")
        self.comboBoxdivisi.addItem("")
        self.lineEditnip = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditnip.setGeometry(QtCore.QRect(150, 60, 211, 21))
        self.lineEditnip.setObjectName("lineEditnip")
        self.comboBoxgrade = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxgrade.setGeometry(QtCore.QRect(150, 130, 211, 26))
        self.comboBoxgrade.setObjectName("comboBoxgrade")
        self.comboBoxgrade.addItem("")
        self.comboBoxgrade.addItem("")
        self.comboBoxgrade.addItem("")
        self.comboBoxgrade.addItem("")
        self.comboBoxgrade.addItem("")
        self.comboBoxgrade.addItem("")
        self.comboBoxgrade.addItem("")
        self.comboBoxgrade.addItem("")
        self.comboBoxgrade.addItem("")
        self.comboBoxgrade.addItem("")
        self.comboBoxgrade.addItem("")
        self.comboBoxgrade.addItem("")
        self.comboBoxgrade.addItem("")
        self.comboBoxgrade.addItem("")
        self.comboBoxgrade.addItem("")
        self.comboBoxgrade.addItem("")
        self.comboBoxgrade.addItem("")
        self.comboBoxgrade.addItem("")
        self.comboBoxgrade.addItem("")
        self.comboBoxgrade.addItem("")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 200, 121, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 430, 71, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 330, 60, 16))
        self.label_7.setObjectName("label_7")
        self.textEditalamat = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditalamat.setGeometry(QtCore.QRect(150, 330, 221, 71))
        self.textEditalamat.setObjectName("textEditalamat")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 270, 111, 21))
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 570, 113, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(600, 570, 113, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.dateEditmasuk = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEditmasuk.setGeometry(QtCore.QRect(150, 200, 221, 24))
        self.dateEditmasuk.setObjectName("dateEditmasuk")
        self.dateEditlahir = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEditlahir.setGeometry(QtCore.QRect(150, 270, 221, 24))
        self.dateEditlahir.setObjectName("dateEditlahir")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(495, 30, 321, 192))
        self.graphicsView.setObjectName("graphicsView")
        self.textEditfoto = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditfoto.setGeometry(QtCore.QRect(150, 430, 221, 41))
        self.textEditfoto.setObjectName("textEditfoto")
        forminput.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(forminput)
        self.statusbar.setObjectName("statusbar")
        forminput.setStatusBar(self.statusbar)

        self.retranslateUi(forminput)
        QtCore.QMetaObject.connectSlotsByName(forminput)

    def retranslateUi(self, forminput):
        _translate = QtCore.QCoreApplication.translate
        forminput.setWindowTitle(_translate("forminput", "MainWindow"))
        self.label.setText(_translate("forminput", "NAMA"))
        self.label_2.setText(_translate("forminput", "NIP"))
        self.label_3.setText(_translate("forminput", "DIVISI"))
        self.label_4.setText(_translate("forminput", "GRADE"))
        self.comboBoxdivisi.setItemText(0, _translate("forminput", "IT"))
        self.comboBoxdivisi.setItemText(1, _translate("forminput", "TEKNIK"))
        self.comboBoxdivisi.setItemText(2, _translate("forminput", "KEUANGAN"))
        self.comboBoxdivisi.setItemText(3, _translate("forminput", "UMUM"))
        self.comboBoxdivisi.setItemText(4, _translate("forminput", "OPERASI"))
        self.comboBoxgrade.setItemText(0, _translate("forminput", "1"))
        self.comboBoxgrade.setItemText(1, _translate("forminput", "2"))
        self.comboBoxgrade.setItemText(2, _translate("forminput", "3"))
        self.comboBoxgrade.setItemText(3, _translate("forminput", "4"))
        self.comboBoxgrade.setItemText(4, _translate("forminput", "5"))
        self.comboBoxgrade.setItemText(5, _translate("forminput", "6"))
        self.comboBoxgrade.setItemText(6, _translate("forminput", "7"))
        self.comboBoxgrade.setItemText(7, _translate("forminput", "8"))
        self.comboBoxgrade.setItemText(8, _translate("forminput", "9"))
        self.comboBoxgrade.setItemText(9, _translate("forminput", "10"))
        self.comboBoxgrade.setItemText(10, _translate("forminput", "11"))
        self.comboBoxgrade.setItemText(11, _translate("forminput", "12"))
        self.comboBoxgrade.setItemText(12, _translate("forminput", "13"))
        self.comboBoxgrade.setItemText(13, _translate("forminput", "14"))
        self.comboBoxgrade.setItemText(14, _translate("forminput", "15"))
        self.comboBoxgrade.setItemText(15, _translate("forminput", "16"))
        self.comboBoxgrade.setItemText(16, _translate("forminput", "17"))
        self.comboBoxgrade.setItemText(17, _translate("forminput", "18"))
        self.comboBoxgrade.setItemText(18, _translate("forminput", "19"))
        self.comboBoxgrade.setItemText(19, _translate("forminput", "20"))
        self.label_5.setText(_translate("forminput", "TANGGAL MASUK"))
        self.label_6.setText(_translate("forminput", "FOTO"))
        self.label_7.setText(_translate("forminput", "ALAMAT"))
        self.label_8.setText(_translate("forminput", "TANGGAL LAHIR"))
        self.pushButton.setText(_translate("forminput", "SAVE"))
        self.pushButton_3.setText(_translate("forminput", "CLEAR"))