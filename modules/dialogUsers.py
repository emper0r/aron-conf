# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtUI/dialogUsers.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogUsers(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(340, 290)
        Dialog.setMinimumSize(QtCore.QSize(340, 290))
        Dialog.setMaximumSize(QtCore.QSize(340, 290))
        Dialog.setSizeIncrement(QtCore.QSize(340, 290))
        Dialog.setBaseSize(QtCore.QSize(340, 290))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(9)
        Dialog.setFont(font)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.EditDialog = QtWidgets.QLineEdit(Dialog)
        self.EditDialog.setGeometry(QtCore.QRect(73, 10, 170, 25))
        self.EditDialog.setMinimumSize(QtCore.QSize(170, 25))
        self.EditDialog.setMaximumSize(QtCore.QSize(170, 25))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.EditDialog.setFont(font)
        self.EditDialog.setReadOnly(True)
        self.EditDialog.setObjectName("EditDialog")
        self.labelDialog = QtWidgets.QLabel(Dialog)
        self.labelDialog.setGeometry(QtCore.QRect(20, 13, 50, 20))
        self.labelDialog.setMinimumSize(QtCore.QSize(50, 20))
        self.labelDialog.setMaximumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelDialog.setFont(font)
        self.labelDialog.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.labelDialog.setObjectName("labelDialog")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 70, 320, 210))
        self.tableWidget.setMinimumSize(QtCore.QSize(320, 210))
        self.tableWidget.setMaximumSize(QtCore.QSize(320, 210))
        self.tableWidget.setSizeIncrement(QtCore.QSize(320, 210))
        self.tableWidget.setBaseSize(QtCore.QSize(320, 210))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(159)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.btUsersAdd = QtWidgets.QPushButton(Dialog)
        self.btUsersAdd.setGeometry(QtCore.QRect(250, 10, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.btUsersAdd.setFont(font)
        self.btUsersAdd.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btUsersAdd.setText("")
        self.btUsersAdd.setFlat(True)
        self.btUsersAdd.setObjectName("btUsersAdd")
        self.btUsersDel = QtWidgets.QPushButton(Dialog)
        self.btUsersDel.setGeometry(QtCore.QRect(275, 10, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.btUsersDel.setFont(font)
        self.btUsersDel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btUsersDel.setText("")
        self.btUsersDel.setFlat(True)
        self.btUsersDel.setObjectName("btUsersDel")
        self.btSave = QtWidgets.QPushButton(Dialog)
        self.btSave.setGeometry(QtCore.QRect(300, 10, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.btSave.setFont(font)
        self.btSave.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btSave.setText("")
        self.btSave.setFlat(True)
        self.btSave.setObjectName("btSave")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(250, 40, 81, 22))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox.setChecked(False)
        self.checkBox.setObjectName("checkBox")
        self.EditDialogPwd = QtWidgets.QLineEdit(Dialog)
        self.EditDialogPwd.setGeometry(QtCore.QRect(73, 37, 170, 25))
        self.EditDialogPwd.setMinimumSize(QtCore.QSize(170, 25))
        self.EditDialogPwd.setMaximumSize(QtCore.QSize(170, 25))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.EditDialogPwd.setFont(font)
        self.EditDialogPwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.EditDialogPwd.setReadOnly(True)
        self.EditDialogPwd.setObjectName("EditDialogPwd")
        self.labelPassword = QtWidgets.QLabel(Dialog)
        self.labelPassword.setGeometry(QtCore.QRect(10, 40, 65, 20))
        self.labelPassword.setMinimumSize(QtCore.QSize(65, 20))
        self.labelPassword.setMaximumSize(QtCore.QSize(65, 20))
        self.labelPassword.setBaseSize(QtCore.QSize(65, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelPassword.setFont(font)
        self.labelPassword.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.labelPassword.setObjectName("labelPassword")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.EditDialog, self.EditDialogPwd)
        Dialog.setTabOrder(self.EditDialogPwd, self.checkBox)
        Dialog.setTabOrder(self.checkBox, self.btUsersAdd)
        Dialog.setTabOrder(self.btUsersAdd, self.btUsersDel)
        Dialog.setTabOrder(self.btUsersDel, self.btSave)
        Dialog.setTabOrder(self.btSave, self.tableWidget)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelDialog.setText(_translate("Dialog", "Utenti"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Utenti"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Attivi"))
        self.checkBox.setText(_translate("Dialog", "Attivo"))
        self.labelPassword.setText(_translate("Dialog", "Password"))

