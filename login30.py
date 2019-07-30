# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login30.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os

class Ui_Dialog(object):
    def __init__(self, u_name_label=None, pass_label=None):
        self.lineEdit = u_name_label
        self.lineEdit_2 = pass_label
    def id(self):
        return self.lineEdit
    def pas(self):
        return self.lineEdit_2

    def logincheck(self, u_name_label="admin" , pass_label= "1234"):
        self.u_name_label = u_name_label
        self.pass_label = pass_label
        os.system("python test1.py")
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(552, 549)
        Dialog.setStyleSheet("")
        self.u_name_label = QtWidgets.QLabel(Dialog)
        self.u_name_label.setGeometry(QtCore.QRect(150, 260, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.u_name_label.setFont(font)
        self.u_name_label.setObjectName("u_name_label")
        self.pass_label = QtWidgets.QLabel(Dialog)
        self.pass_label.setGeometry(QtCore.QRect(150, 300, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pass_label.setFont(font)
        self.pass_label.setObjectName("pass_label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(270, 260, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 300, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(270, 330, 111, 71))
        self.pushButton.setStyleSheet("position:relative;\n"
"font: 9pt \"HY헤드라인M\";\n"
"  width: auto;\n"
"  display:inline-block;\n"
"  color:#ecf0f1;\n"
"  text-decoration:none;\n"
"  border-radius:5px;\n"
"  border:solid 1px #f39c12;\n"
"  background:#e67e22;\n"
"  text-align:center;\n"
"  padding:16px 18px 14px;\n"
"  margin: 12px;")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 10, 351, 241))
        self.label_2.setStyleSheet("background-image:url(:/그림/심장.png)")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.u_name_label.raise_()
        self.pass_label.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.pushButton.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton.clicked.connect(self.logincheck)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.u_name_label.setText(_translate("Dialog", "USERNAME"))
        self.pass_label.setText(_translate("Dialog", "PASSWORD"))
        self.pushButton.setText(_translate("Dialog", "Login"))

import source_rc

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

