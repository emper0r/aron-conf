# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtUI/dialogNewClient.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogClient(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(343, 66)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(250, 10, 81, 50))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(9)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.EditDialog = QtWidgets.QLineEdit(Dialog)
        self.EditDialog.setGeometry(QtCore.QRect(63, 21, 181, 25))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(9)
        self.EditDialog.setFont(font)
        self.EditDialog.setObjectName("EditDialog")
        self.labelDialog = QtWidgets.QLabel(Dialog)
        self.labelDialog.setGeometry(QtCore.QRect(10, 24, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(9)
        self.labelDialog.setFont(font)
        self.labelDialog.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.labelDialog.setObjectName("labelDialog")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelDialog.setText(_translate("Dialog", "Cliente"))

