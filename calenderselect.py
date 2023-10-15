from PyQt5.QtWidgets import QMainWindow,QApplication, QCalendarWidget,QLabel
from PyQt5 import uic
import sys 
import forminput3


class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()
        uic.loadUi("forminput.ui",self)
        self.calendar=self.findChild(QCalendarWidget, "calendarWidget")
        self.label=self.findChild(QLabel,"label_9")
        self.calendar2=self.findChild(QCalendarWidget, "calendarWidget_2")
        self.label=self.findChild(QLabel,"label_10")
        
        self.calendar.selectionChanged.connect(self.grab_date)
        self.calendar2.selectionChanged.connect(self.grab_date2)
        self.show()
        
    def grab_date(self):
        dateselected=self.calendar.selectedDate()
        self.label_9.setText(str(dateselected.toPyDate()))
        
    def grab_date2(self):
        dateselected2=self.calendar2.selectedDate()
        self.label_10.setText(str(dateselected2.toPyDate()))
        
    
def setupUi(self, forminput):
        self.koneksi()
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
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 30, 161, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(160, 90, 104, 26))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 60, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(160, 130, 104, 26))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(445, 30, 211, 141))
        self.graphicsView.setObjectName("graphicsView")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 200, 121, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(520, 180, 71, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 340, 60, 16))
        self.label_7.setObjectName("label_7")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(160, 340, 221, 71))
        self.textEdit.setObjectName("textEdit")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 260, 101, 21))
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.save())
        self.pushButton.setGeometry(QtCore.QRect(90, 540, 113, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(620, 540, 113, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(160, 190, 110, 24))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_2.setGeometry(QtCore.QRect(160, 260, 110, 24))
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setObjectName("dateEdit_2")
        forminput.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(forminput)
        self.statusbar.setObjectName("statusbar")
        forminput.setStatusBar(self.statusbar)

        self.retranslateUi(forminput)
        QtCore.QMetaObject.connectSlotsByName(forminput)

app=QApplication(sys.argv)
UIWindow=UI()
app.exec_()       
        