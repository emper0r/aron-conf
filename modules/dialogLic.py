# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtUI/dialogLic.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogLic(object):
    def setupUi(self, DialogLic):
        DialogLic.setObjectName("DialogLic")
        DialogLic.resize(770, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogLic.sizePolicy().hasHeightForWidth())
        DialogLic.setSizePolicy(sizePolicy)
        DialogLic.setMinimumSize(QtCore.QSize(770, 500))
        DialogLic.setMaximumSize(QtCore.QSize(770, 500))
        DialogLic.setSizeIncrement(QtCore.QSize(770, 500))
        DialogLic.setBaseSize(QtCore.QSize(770, 500))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(9)
        DialogLic.setFont(font)
        DialogLic.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tableWidget = QtWidgets.QTableWidget(DialogLic)
        self.tableWidget.setGeometry(QtCore.QRect(4, 120, 760, 320))
        self.tableWidget.setMinimumSize(QtCore.QSize(760, 320))
        self.tableWidget.setMaximumSize(QtCore.QSize(760, 320))
        self.tableWidget.setSizeIncrement(QtCore.QSize(760, 320))
        self.tableWidget.setBaseSize(QtCore.QSize(760, 420))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tableWidget.setFont(font)
        self.tableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget.setGridStyle(QtCore.Qt.DotLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(11)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(10, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(69)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(330)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(25)
        self.tableWidget.verticalHeader().setMinimumSectionSize(25)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.labelClient = QtWidgets.QLabel(DialogLic)
        self.labelClient.setGeometry(QtCore.QRect(10, 10, 60, 20))
        self.labelClient.setMinimumSize(QtCore.QSize(60, 20))
        self.labelClient.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelClient.setFont(font)
        self.labelClient.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.labelClient.setObjectName("labelClient")
        self.lineEditClient = QtWidgets.QLineEdit(DialogLic)
        self.lineEditClient.setGeometry(QtCore.QRect(76, 10, 140, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEditClient.setFont(font)
        self.lineEditClient.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lineEditClient.setObjectName("lineEditClient")
        self.labelName = QtWidgets.QLabel(DialogLic)
        self.labelName.setGeometry(QtCore.QRect(30, 37, 60, 20))
        self.labelName.setMinimumSize(QtCore.QSize(60, 20))
        self.labelName.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelName.setFont(font)
        self.labelName.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.labelName.setObjectName("labelName")
        self.lineEditName = QtWidgets.QLineEdit(DialogLic)
        self.lineEditName.setGeometry(QtCore.QRect(76, 37, 140, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEditName.setFont(font)
        self.lineEditName.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lineEditName.setObjectName("lineEditName")
        self.labelEmail = QtWidgets.QLabel(DialogLic)
        self.labelEmail.setGeometry(QtCore.QRect(23, 63, 60, 20))
        self.labelEmail.setMinimumSize(QtCore.QSize(60, 20))
        self.labelEmail.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelEmail.setFont(font)
        self.labelEmail.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.labelEmail.setObjectName("labelEmail")
        self.lineEditEmail = QtWidgets.QLineEdit(DialogLic)
        self.lineEditEmail.setGeometry(QtCore.QRect(76, 63, 140, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEditEmail.setFont(font)
        self.lineEditEmail.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.labelQty = QtWidgets.QLabel(DialogLic)
        self.labelQty.setGeometry(QtCore.QRect(49, 90, 30, 20))
        self.labelQty.setMinimumSize(QtCore.QSize(30, 20))
        self.labelQty.setMaximumSize(QtCore.QSize(30, 20))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelQty.setFont(font)
        self.labelQty.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.labelQty.setObjectName("labelQty")
        self.dateEditActive = QtWidgets.QDateEdit(DialogLic)
        self.dateEditActive.setGeometry(QtCore.QRect(263, 10, 110, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.dateEditActive.setFont(font)
        self.dateEditActive.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dateEditActive.setCalendarPopup(True)
        self.dateEditActive.setObjectName("dateEditActive")
        self.labelActive = QtWidgets.QLabel(DialogLic)
        self.labelActive.setGeometry(QtCore.QRect(234, 12, 30, 20))
        self.labelActive.setMinimumSize(QtCore.QSize(30, 20))
        self.labelActive.setMaximumSize(QtCore.QSize(30, 20))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelActive.setFont(font)
        self.labelActive.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.labelActive.setObjectName("labelActive")
        self.labelExpire = QtWidgets.QLabel(DialogLic)
        self.labelExpire.setGeometry(QtCore.QRect(227, 40, 30, 20))
        self.labelExpire.setMinimumSize(QtCore.QSize(30, 20))
        self.labelExpire.setMaximumSize(QtCore.QSize(30, 20))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelExpire.setFont(font)
        self.labelExpire.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.labelExpire.setObjectName("labelExpire")
        self.dateEditExpire = QtWidgets.QDateEdit(DialogLic)
        self.dateEditExpire.setGeometry(QtCore.QRect(263, 38, 110, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.dateEditExpire.setFont(font)
        self.dateEditExpire.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dateEditExpire.setCalendarPopup(True)
        self.dateEditExpire.setObjectName("dateEditExpire")
        self.btGenerate = QtWidgets.QPushButton(DialogLic)
        self.btGenerate.setGeometry(QtCore.QRect(464, 70, 30, 26))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.btGenerate.setFont(font)
        self.btGenerate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btGenerate.setText("")
        self.btGenerate.setObjectName("btGenerate")
        self.btSave = QtWidgets.QPushButton(DialogLic)
        self.btSave.setGeometry(QtCore.QRect(590, 70, 30, 26))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.btSave.setFont(font)
        self.btSave.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btSave.setText("")
        self.btSave.setObjectName("btSave")
        self.lineEditReq = QtWidgets.QLineEdit(DialogLic)
        self.lineEditReq.setGeometry(QtCore.QRect(414, 10, 351, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEditReq.setFont(font)
        self.lineEditReq.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lineEditReq.setReadOnly(True)
        self.lineEditReq.setObjectName("lineEditReq")
        self.labelReq = QtWidgets.QLabel(DialogLic)
        self.labelReq.setGeometry(QtCore.QRect(390, 10, 30, 20))
        self.labelReq.setMinimumSize(QtCore.QSize(30, 20))
        self.labelReq.setMaximumSize(QtCore.QSize(30, 20))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelReq.setFont(font)
        self.labelReq.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.labelReq.setObjectName("labelReq")
        self.lineEditLic = QtWidgets.QLineEdit(DialogLic)
        self.lineEditLic.setGeometry(QtCore.QRect(414, 37, 351, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEditLic.setFont(font)
        self.lineEditLic.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lineEditLic.setReadOnly(True)
        self.lineEditLic.setObjectName("lineEditLic")
        self.labelLic = QtWidgets.QLabel(DialogLic)
        self.labelLic.setGeometry(QtCore.QRect(390, 37, 30, 20))
        self.labelLic.setMinimumSize(QtCore.QSize(30, 20))
        self.labelLic.setMaximumSize(QtCore.QSize(30, 20))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelLic.setFont(font)
        self.labelLic.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.labelLic.setObjectName("labelLic")
        self.btDelete = QtWidgets.QPushButton(DialogLic)
        self.btDelete.setGeometry(QtCore.QRect(10, 450, 31, 26))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.btDelete.setFont(font)
        self.btDelete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btDelete.setText("")
        self.btDelete.setObjectName("btDelete")
        self.labelGenerate = QtWidgets.QLabel(DialogLic)
        self.labelGenerate.setGeometry(QtCore.QRect(500, 73, 60, 20))
        self.labelGenerate.setMinimumSize(QtCore.QSize(60, 20))
        self.labelGenerate.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelGenerate.setFont(font)
        self.labelGenerate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.labelGenerate.setObjectName("labelGenerate")
        self.labelSave = QtWidgets.QLabel(DialogLic)
        self.labelSave.setGeometry(QtCore.QRect(627, 73, 60, 20))
        self.labelSave.setMinimumSize(QtCore.QSize(60, 20))
        self.labelSave.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelSave.setFont(font)
        self.labelSave.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.labelSave.setObjectName("labelSave")
        self.labelDelete = QtWidgets.QLabel(DialogLic)
        self.labelDelete.setGeometry(QtCore.QRect(45, 453, 60, 20))
        self.labelDelete.setMinimumSize(QtCore.QSize(60, 20))
        self.labelDelete.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelDelete.setFont(font)
        self.labelDelete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.labelDelete.setObjectName("labelDelete")
        self.spinBoxQty = QtWidgets.QSpinBox(DialogLic)
        self.spinBoxQty.setGeometry(QtCore.QRect(77, 90, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBoxQty.setFont(font)
        self.spinBoxQty.setMaximum(1000)
        self.spinBoxQty.setObjectName("spinBoxQty")
        self.labelUnlimited = QtWidgets.QLabel(DialogLic)
        self.labelUnlimited.setGeometry(QtCore.QRect(150, 90, 100, 20))
        self.labelUnlimited.setMinimumSize(QtCore.QSize(100, 20))
        self.labelUnlimited.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.labelUnlimited.setFont(font)
        self.labelUnlimited.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.labelUnlimited.setObjectName("labelUnlimited")

        self.retranslateUi(DialogLic)
        QtCore.QMetaObject.connectSlotsByName(DialogLic)
        DialogLic.setTabOrder(self.lineEditClient, self.lineEditName)
        DialogLic.setTabOrder(self.lineEditName, self.lineEditEmail)
        DialogLic.setTabOrder(self.lineEditEmail, self.spinBoxQty)
        DialogLic.setTabOrder(self.spinBoxQty, self.dateEditActive)
        DialogLic.setTabOrder(self.dateEditActive, self.dateEditExpire)
        DialogLic.setTabOrder(self.dateEditExpire, self.btGenerate)
        DialogLic.setTabOrder(self.btGenerate, self.btSave)
        DialogLic.setTabOrder(self.btSave, self.tableWidget)
        DialogLic.setTabOrder(self.tableWidget, self.btDelete)
        DialogLic.setTabOrder(self.btDelete, self.lineEditReq)
        DialogLic.setTabOrder(self.lineEditReq, self.lineEditLic)

    def retranslateUi(self, DialogLic):
        _translate = QtCore.QCoreApplication.translate
        DialogLic.setWindowTitle(_translate("DialogLic", "Aron Proxy License"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("DialogLic", "Client"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("DialogLic", "Nome"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("DialogLic", "Email"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("DialogLic", "Qtà"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("DialogLic", "Attivo"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("DialogLic", "Scade"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("DialogLic", "Req"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("DialogLic", "Lic"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("DialogLic", "Server-ID"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("DialogLic", "Active"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("DialogLic", "Password"))
        self.labelClient.setText(_translate("DialogLic", "Cliente"))
        self.labelName.setText(_translate("DialogLic", "Nome"))
        self.labelEmail.setText(_translate("DialogLic", "Email"))
        self.labelQty.setText(_translate("DialogLic", "Qtà"))
        self.dateEditActive.setDisplayFormat(_translate("DialogLic", "dd/MM/yyyy"))
        self.labelActive.setText(_translate("DialogLic", "Dal"))
        self.labelExpire.setText(_translate("DialogLic", "Fino"))
        self.dateEditExpire.setDisplayFormat(_translate("DialogLic", "dd/MM/yyyy"))
        self.labelReq.setText(_translate("DialogLic", "Req"))
        self.labelLic.setText(_translate("DialogLic", "Lic"))
        self.labelGenerate.setText(_translate("DialogLic", "Genera"))
        self.labelSave.setText(_translate("DialogLic", "Salva"))
        self.labelDelete.setText(_translate("DialogLic", "Elimina"))
        self.labelUnlimited.setText(_translate("DialogLic", "0 = Ilimitato"))

