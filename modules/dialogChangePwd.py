# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtUI/dialogChangePasswd.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogChangePwd(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(260, 178)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(9)
        Dialog.setFont(font)
        self.EditNew = QtWidgets.QLineEdit(Dialog)
        self.EditNew.setGeometry(QtCore.QRect(70, 91, 181, 25))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(9)
        self.EditNew.setFont(font)
        self.EditNew.setEchoMode(QtWidgets.QLineEdit.Password)
        self.EditNew.setObjectName("EditNew")
        self.labelNew = QtWidgets.QLabel(Dialog)
        self.labelNew.setGeometry(QtCore.QRect(20, 94, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelNew.setFont(font)
        self.labelNew.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.labelNew.setObjectName("labelNew")
        self.EditConferm = QtWidgets.QLineEdit(Dialog)
        self.EditConferm.setGeometry(QtCore.QRect(70, 117, 181, 25))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(9)
        self.EditConferm.setFont(font)
        self.EditConferm.setEchoMode(QtWidgets.QLineEdit.Password)
        self.EditConferm.setObjectName("EditConferm")
        self.labelConferm = QtWidgets.QLabel(Dialog)
        self.labelConferm.setGeometry(QtCore.QRect(10, 120, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelConferm.setFont(font)
        self.labelConferm.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.labelConferm.setObjectName("labelConferm")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(100, 143, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(9)
        self.buttonBox.setFont(font)
        self.buttonBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.labelLogo = QtWidgets.QLabel(Dialog)
        self.labelLogo.setGeometry(QtCore.QRect(90, 10, 121, 71))
        self.labelLogo.setText("")
        self.labelLogo.setObjectName("labelLogo")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Modifica Password"))
        self.labelNew.setText(_translate("Dialog", "Nuova"))
        self.labelConferm.setText(_translate("Dialog", "Conferma"))

