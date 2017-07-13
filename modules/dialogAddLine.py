# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtUI/dialogAddLine.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogAdd(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(213, 97)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(9)
        Dialog.setFont(font)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(46, 60, 120, 31))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(9)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.EditDialog = QtWidgets.QLineEdit(Dialog)
        self.EditDialog.setGeometry(QtCore.QRect(10, 30, 190, 25))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(9)
        self.EditDialog.setFont(font)
        self.EditDialog.setObjectName("EditDialog")
        self.labelDialog = QtWidgets.QLabel(Dialog)
        self.labelDialog.setGeometry(QtCore.QRect(10, 8, 190, 20))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(9)
        self.labelDialog.setFont(font)
        self.labelDialog.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.labelDialog.setText("")
        self.labelDialog.setObjectName("labelDialog")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

