from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(470, 282)
        mainWindow.setWindowOpacity(1.0)
        
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.groupBox_items = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_items.setGeometry(QtCore.QRect(20, 10, 131, 221))
        
        font = QtGui.QFont()
        font.setPointSize(16)
        
        self.groupBox_items.setFont(font)
        self.groupBox_items.setObjectName("groupBox_items")
        
        self.pushButton_250 = QtWidgets.QPushButton(self.groupBox_items)
        self.pushButton_250.setGeometry(QtCore.QRect(30, 90, 75, 23))
        
        font = QtGui.QFont()
        font.setPointSize(12)
        
        self.pushButton_250.setFont(font)
        self.pushButton_250.setObjectName("pushButton_250")
        
        self.pushButton_150 = QtWidgets.QPushButton(self.groupBox_items)
        self.pushButton_150.setGeometry(QtCore.QRect(30, 40, 75, 23))
        
        font = QtGui.QFont()
        font.setPointSize(12)
        
        self.pushButton_150.setFont(font)
        self.pushButton_150.setObjectName("pushButton150")
        
        self.pushButton_500 = QtWidgets.QPushButton(self.groupBox_items)
        self.pushButton_500.setGeometry(QtCore.QRect(30, 140, 75, 23))
        
        font = QtGui.QFont()
        font.setPointSize(12)
        
        self.pushButton_500.setFont(font)
        self.pushButton_500.setObjectName("pushButton_500")
        
        self.label_change = QtWidgets.QLabel(self.centralwidget)
        self.label_change.setGeometry(QtCore.QRect(170, 130, 81, 31))
        
        font = QtGui.QFont()
        font.setPointSize(16)
        
        self.label_change.setFont(font)
        self.label_change.setObjectName("label_change")
        
        self.line_amount_value = QtWidgets.QLineEdit(self.centralwidget)
        self.line_amount_value.setGeometry(QtCore.QRect(270, 60, 151, 31))
        
        font = QtGui.QFont()
        font.setPointSize(12)
        
        self.line_amount_value.setFont(font)
        self.line_amount_value.setObjectName("line_amount_value")
        
        self.label_amount = QtWidgets.QLabel(self.centralwidget)
        self.label_amount.setGeometry(QtCore.QRect(270, 30, 141, 21))
        
        font = QtGui.QFont()
        font.setPointSize(16)
        
        self.label_amount.setFont(font)
        self.label_amount.setObjectName("label_amount")
        
        self.label_change_value = QtWidgets.QLabel(self.centralwidget)
        self.label_change_value.setGeometry(QtCore.QRect(170, 170, 61, 21))
        
        font = QtGui.QFont()
        font.setPointSize(12)
        
        self.label_change_value.setFont(font)
        self.label_change_value.setAutoFillBackground(False)
        self.label_change_value.setObjectName("label_change_value")
        
        self.label_cost = QtWidgets.QLabel(self.centralwidget)
        self.label_cost.setGeometry(QtCore.QRect(170, 30, 81, 31))
        
        font = QtGui.QFont()
        font.setPointSize(16)
        
        self.label_cost.setFont(font)
        self.label_cost.setObjectName("label_cost")
        
        self.label_cost_value = QtWidgets.QLabel(self.centralwidget)
        self.label_cost_value.setGeometry(QtCore.QRect(170, 70, 61, 21))
        
        font = QtGui.QFont()
        font.setPointSize(12)
        
        self.label_cost_value.setFont(font)
        self.label_cost_value.setAutoFillBackground(False)
        self.label_cost_value.setObjectName("label_cost_value")
        
        self.pushButton_convert = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_convert.setGeometry(QtCore.QRect(170, 200, 75, 23))
        
        font = QtGui.QFont()
        font.setPointSize(12)
        
        self.pushButton_convert.setFont(font)
        self.pushButton_convert.setObjectName("pushButton_convert")
        self.pushButton_pay = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_pay.setGeometry(QtCore.QRect(310, 100, 75, 23))
        
        font = QtGui.QFont()
        font.setPointSize(12)
        
        self.pushButton_pay.setFont(font)
        self.pushButton_pay.setObjectName("pushButton_pay")
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Vending Machine Simulation"))
        self.groupBox_items.setTitle(_translate("mainWindow", "Items"))
        
        # Items
        self.pushButton_150.setText(_translate("mainWindow", "RM 1.50"))
        self.pushButton_150.clicked.connect(lambda: self.addValue(1))
        
        self.pushButton_250.setText(_translate("mainWindow", "RM 2.50"))
        self.pushButton_250.clicked.connect(lambda: self.addValue(2))
        
        self.pushButton_500.setText(_translate("mainWindow", "RM 5.00"))
        self.pushButton_500.clicked.connect(lambda: self.addValue(3))
        
        # Change
        self.label_change.setText(_translate("mainWindow", "Change"))
        
        # Change Value
        self.label_change_value.setText(_translate("mainWindow", "0.00"))
        
        # Amount Value
        self.line_amount_value.setText(_translate("mainWindow", "0.00"))
        
        self.label_amount.setText(_translate("mainWindow", "Enter amount"))
        
        
        self.label_cost.setText(_translate("mainWindow", "Cost"))
        self.label_cost_value.setText(_translate("mainWindow", "0.00"))
        
        self.pushButton_convert.setText(_translate("mainWindow", "Convert"))
        
        self.pushButton_pay.setText(_translate("mainWindow", "Pay"))
        self.pushButton_pay.clicked.connect(self.payAmount)
    
    def payAmount(self):
        amountValue = float(self.line_amount_value.text())
        costValue = float(self.label_cost_value.text())
        
        if amountValue >= costValue:
            changeValue = amountValue - costValue
        else:
            print('NOT ENOUGH MONEY BODOH')
            changeValue = 0.00
        self.label_change_value.setText(str(changeValue)+str(0))
        
        print(amountValue)
    
    def addValue(self, value):
        if value == 1:
            costValue = 1.50
            
        elif value == 2:
            costValue = 2.50
         
        elif value == 3:
            costValue = 5.00   
            
        print(costValue)
        self.label_cost_value.setText(str(costValue)+str(0))
        
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
