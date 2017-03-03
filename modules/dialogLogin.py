# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtUI/dialogLogin.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogLogin(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(275, 183)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(9)
        Dialog.setFont(font)
        Dialog.setModal(False)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(100, 144, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(9)
        self.buttonBox.setFont(font)
        self.buttonBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.EditLogin = QtWidgets.QLineEdit(Dialog)
        self.EditLogin.setGeometry(QtCore.QRect(70, 91, 181, 25))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(9)
        self.EditLogin.setFont(font)
        self.EditLogin.setObjectName("EditLogin")
        self.labelLogin = QtWidgets.QLabel(Dialog)
        self.labelLogin.setGeometry(QtCore.QRect(20, 94, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(9)
        self.labelLogin.setFont(font)
        self.labelLogin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.labelLogin.setObjectName("labelLogin")
        self.EditPass = QtWidgets.QLineEdit(Dialog)
        self.EditPass.setGeometry(QtCore.QRect(70, 117, 181, 25))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(9)
        self.EditPass.setFont(font)
        self.EditPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.EditPass.setObjectName("EditPass")
        self.labelPass = QtWidgets.QLabel(Dialog)
        self.labelPass.setGeometry(QtCore.QRect(10, 120, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(9)
        self.labelPass.setFont(font)
        self.labelPass.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.labelPass.setObjectName("labelPass")
        self.labelLogo = QtWidgets.QLabel(Dialog)
        self.labelLogo.setGeometry(QtCore.QRect(90, 10, 121, 71))
        self.labelLogo.setText("")
        self.labelLogo.setObjectName("labelLogo")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.EditLogin, self.EditPass)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Aron Config - Login"))
        self.labelLogin.setText(_translate("Dialog", "Login"))
        self.labelPass.setText(_translate("Dialog", "Password"))

