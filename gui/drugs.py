from PyQt5 import QtCore, QtGui, QtWidgets
from styleSheets import *

class Ui_InstinctSolutions(object):
    drug = ""
    dose = 0
    def setupUi(self, InstinctSolutions):
        InstinctSolutions.setObjectName("InstinctSolutions")
        InstinctSolutions.resize(1081, 482)
        InstinctSolutions.setStyleSheet(getStyle())
        self.centralwidget = QtWidgets.QWidget(InstinctSolutions)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_go = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_go.setGeometry(QtCore.QRect(330, 320, 421, 101))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.pushButton_go.setFont(font)
        self.pushButton_go.setObjectName("pushButton_go")
        self.comboBox_drugs = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_drugs.setGeometry(QtCore.QRect(40, 140, 671, 141))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.comboBox_drugs.setFont(font)
        self.comboBox_drugs.setObjectName("comboBox_drugs")
        self.comboBox_drugs.addItem("")
        self.comboBox_drugs.addItem("")
        self.comboBox_drugs.addItem("")
        self.comboBox_drugs.addItem("")
        self.comboBox_drugs.addItem("")
        self.line_amount = QtWidgets.QLineEdit(self.centralwidget)
        self.line_amount.setGeometry(QtCore.QRect(770, 140, 261, 141))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.line_amount.setFont(font)
        self.line_amount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.line_amount.setObjectName("line_amount")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(10, 20, 1001, 81))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.label_title.setFont(font)
        self.label_title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_title.setStyleSheet("")
        self.label_title.setObjectName("label_title")
        InstinctSolutions.setCentralWidget(self.centralwidget)

        self.retranslateUi(InstinctSolutions)
        QtCore.QMetaObject.connectSlotsByName(InstinctSolutions)

    def retranslateUi(self, InstinctSolutions):
        _translate = QtCore.QCoreApplication.translate
        InstinctSolutions.setWindowTitle(_translate("InstinctSolutions", "Instinct Solutions"))
        self.pushButton_go.setText(_translate("InstinctSolutions", "GO"))
        self.pushButton_go.clicked.connect(self.prescribe)
        self.comboBox_drugs.setItemText(0, _translate("InstinctSolutions", "AMOXICILLIN"))
        self.comboBox_drugs.setItemText(1, _translate("InstinctSolutions", "AZITHROMYCIN"))
        self.comboBox_drugs.setItemText(2, _translate("InstinctSolutions", "HYDROCHLOROTHIAZIDE"))
        self.comboBox_drugs.setItemText(3, _translate("InstinctSolutions", "HYDROCODONE"))
        self.comboBox_drugs.setItemText(4, _translate("InstinctSolutions", "LISINOPRIL"))
        self.line_amount.setText(_translate("InstinctSolutions", "0"))
        self.label_title.setText(_translate("InstinctSolutions", "INSTINCT SOLUTIONS"))

    def prescribe(self):
        drugs = self.comboBox_drugs.currentText()
        dose = self.line_amount.text()
        
        print(drugs+dose)
        
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InstinctSolutions = QtWidgets.QMainWindow()
    ui = Ui_InstinctSolutions()
    ui.setupUi(InstinctSolutions)
    InstinctSolutions.show()
    sys.exit(app.exec_())
