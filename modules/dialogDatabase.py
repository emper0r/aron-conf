# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtUI/dialogDatabase.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogImpostazione(object):
    def setupUi(self, DialogImpostazione):
        DialogImpostazione.setObjectName("DialogImpostazione")
        DialogImpostazione.resize(325, 430)
        DialogImpostazione.setMinimumSize(QtCore.QSize(325, 430))
        DialogImpostazione.setMaximumSize(QtCore.QSize(325, 430))
        DialogImpostazione.setSizeIncrement(QtCore.QSize(325, 430))
        DialogImpostazione.setBaseSize(QtCore.QSize(325, 430))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(9)
        DialogImpostazione.setFont(font)
        DialogImpostazione.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.EditDialogHostname = QtWidgets.QLineEdit(DialogImpostazione)
        self.EditDialogHostname.setEnabled(True)
        self.EditDialogHostname.setGeometry(QtCore.QRect(95, 215, 170, 25))
        self.EditDialogHostname.setMinimumSize(QtCore.QSize(170, 25))
        self.EditDialogHostname.setMaximumSize(QtCore.QSize(170, 25))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.EditDialogHostname.setFont(font)
        self.EditDialogHostname.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.EditDialogHostname.setReadOnly(False)
        self.EditDialogHostname.setObjectName("EditDialogHostname")
        self.labelHost = QtWidgets.QLabel(DialogImpostazione)
        self.labelHost.setGeometry(QtCore.QRect(34, 218, 60, 20))
        self.labelHost.setMinimumSize(QtCore.QSize(50, 20))
        self.labelHost.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.labelHost.setFont(font)
        self.labelHost.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.labelHost.setObjectName("labelHost")
        self.btSave = QtWidgets.QPushButton(DialogImpostazione)
        self.btSave.setGeometry(QtCore.QRect(130, 396, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.btSave.setFont(font)
        self.btSave.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btSave.setText("")
        self.btSave.setFlat(True)
        self.btSave.setObjectName("btSave")
        self.EditDialogPwd = QtWidgets.QLineEdit(DialogImpostazione)
        self.EditDialogPwd.setEnabled(True)
        self.EditDialogPwd.setGeometry(QtCore.QRect(95, 301, 170, 25))
        self.EditDialogPwd.setMinimumSize(QtCore.QSize(170, 25))
        self.EditDialogPwd.setMaximumSize(QtCore.QSize(170, 25))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.EditDialogPwd.setFont(font)
        self.EditDialogPwd.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.EditDialogPwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.EditDialogPwd.setReadOnly(False)
        self.EditDialogPwd.setObjectName("EditDialogPwd")
        self.labelPassword = QtWidgets.QLabel(DialogImpostazione)
        self.labelPassword.setGeometry(QtCore.QRect(31, 304, 65, 20))
        self.labelPassword.setMinimumSize(QtCore.QSize(65, 20))
        self.labelPassword.setMaximumSize(QtCore.QSize(65, 20))
        self.labelPassword.setBaseSize(QtCore.QSize(65, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.labelPassword.setFont(font)
        self.labelPassword.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.labelPassword.setObjectName("labelPassword")
        self.EditDialogDatabase = QtWidgets.QLineEdit(DialogImpostazione)
        self.EditDialogDatabase.setEnabled(True)
        self.EditDialogDatabase.setGeometry(QtCore.QRect(95, 242, 170, 25))
        self.EditDialogDatabase.setMinimumSize(QtCore.QSize(170, 25))
        self.EditDialogDatabase.setMaximumSize(QtCore.QSize(170, 25))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.EditDialogDatabase.setFont(font)
        self.EditDialogDatabase.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.EditDialogDatabase.setReadOnly(False)
        self.EditDialogDatabase.setObjectName("EditDialogDatabase")
        self.labelDatabase = QtWidgets.QLabel(DialogImpostazione)
        self.labelDatabase.setGeometry(QtCore.QRect(33, 245, 60, 20))
        self.labelDatabase.setMinimumSize(QtCore.QSize(50, 20))
        self.labelDatabase.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.labelDatabase.setFont(font)
        self.labelDatabase.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.labelDatabase.setObjectName("labelDatabase")
        self.EditDialogUsername = QtWidgets.QLineEdit(DialogImpostazione)
        self.EditDialogUsername.setEnabled(True)
        self.EditDialogUsername.setGeometry(QtCore.QRect(95, 272, 170, 25))
        self.EditDialogUsername.setMinimumSize(QtCore.QSize(170, 25))
        self.EditDialogUsername.setMaximumSize(QtCore.QSize(170, 25))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.EditDialogUsername.setFont(font)
        self.EditDialogUsername.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.EditDialogUsername.setReadOnly(False)
        self.EditDialogUsername.setObjectName("EditDialogUsername")
        self.labelUsername = QtWidgets.QLabel(DialogImpostazione)
        self.labelUsername.setGeometry(QtCore.QRect(47, 275, 60, 20))
        self.labelUsername.setMinimumSize(QtCore.QSize(50, 20))
        self.labelUsername.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.labelUsername.setFont(font)
        self.labelUsername.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.labelUsername.setObjectName("labelUsername")
        self.labelSmtpPassword = QtWidgets.QLabel(DialogImpostazione)
        self.labelSmtpPassword.setGeometry(QtCore.QRect(10, 123, 80, 20))
        self.labelSmtpPassword.setMinimumSize(QtCore.QSize(80, 20))
        self.labelSmtpPassword.setMaximumSize(QtCore.QSize(80, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.labelSmtpPassword.setFont(font)
        self.labelSmtpPassword.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.labelSmtpPassword.setObjectName("labelSmtpPassword")
        self.EditDialogSmtpUser = QtWidgets.QLineEdit(DialogImpostazione)
        self.EditDialogSmtpUser.setEnabled(True)
        self.EditDialogSmtpUser.setGeometry(QtCore.QRect(95, 90, 170, 25))
        self.EditDialogSmtpUser.setMinimumSize(QtCore.QSize(170, 25))
        self.EditDialogSmtpUser.setMaximumSize(QtCore.QSize(170, 25))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.EditDialogSmtpUser.setFont(font)
        self.EditDialogSmtpUser.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.EditDialogSmtpUser.setReadOnly(False)
        self.EditDialogSmtpUser.setObjectName("EditDialogSmtpUser")
        self.labelSmtpServer = QtWidgets.QLabel(DialogImpostazione)
        self.labelSmtpServer.setGeometry(QtCore.QRect(16, 37, 80, 20))
        self.labelSmtpServer.setMinimumSize(QtCore.QSize(80, 20))
        self.labelSmtpServer.setMaximumSize(QtCore.QSize(80, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.labelSmtpServer.setFont(font)
        self.labelSmtpServer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.labelSmtpServer.setObjectName("labelSmtpServer")
        self.EditDialogSmtpPassword = QtWidgets.QLineEdit(DialogImpostazione)
        self.EditDialogSmtpPassword.setEnabled(True)
        self.EditDialogSmtpPassword.setGeometry(QtCore.QRect(95, 120, 170, 25))
        self.EditDialogSmtpPassword.setMinimumSize(QtCore.QSize(170, 25))
        self.EditDialogSmtpPassword.setMaximumSize(QtCore.QSize(170, 25))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.EditDialogSmtpPassword.setFont(font)
        self.EditDialogSmtpPassword.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.EditDialogSmtpPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.EditDialogSmtpPassword.setReadOnly(False)
        self.EditDialogSmtpPassword.setObjectName("EditDialogSmtpPassword")
        self.labelSmtpUser = QtWidgets.QLabel(DialogImpostazione)
        self.labelSmtpUser.setGeometry(QtCore.QRect(24, 93, 70, 20))
        self.labelSmtpUser.setMinimumSize(QtCore.QSize(70, 20))
        self.labelSmtpUser.setMaximumSize(QtCore.QSize(70, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.labelSmtpUser.setFont(font)
        self.labelSmtpUser.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.labelSmtpUser.setObjectName("labelSmtpUser")
        self.EditDialogSmtpServer = QtWidgets.QLineEdit(DialogImpostazione)
        self.EditDialogSmtpServer.setEnabled(True)
        self.EditDialogSmtpServer.setGeometry(QtCore.QRect(95, 34, 170, 25))
        self.EditDialogSmtpServer.setMinimumSize(QtCore.QSize(170, 25))
        self.EditDialogSmtpServer.setMaximumSize(QtCore.QSize(170, 25))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.EditDialogSmtpServer.setFont(font)
        self.EditDialogSmtpServer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.EditDialogSmtpServer.setReadOnly(False)
        self.EditDialogSmtpServer.setObjectName("EditDialogSmtpServer")
        self.line = QtWidgets.QFrame(DialogImpostazione)
        self.line.setGeometry(QtCore.QRect(9, 150, 311, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.line.setFont(font)
        self.line.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.labelImpostazioneMail = QtWidgets.QLabel(DialogImpostazione)
        self.labelImpostazioneMail.setGeometry(QtCore.QRect(10, 10, 131, 18))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelImpostazioneMail.setFont(font)
        self.labelImpostazioneMail.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.labelImpostazioneMail.setObjectName("labelImpostazioneMail")
        self.labelImpostazioneDB = QtWidgets.QLabel(DialogImpostazione)
        self.labelImpostazioneDB.setGeometry(QtCore.QRect(10, 175, 161, 18))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelImpostazioneDB.setFont(font)
        self.labelImpostazioneDB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.labelImpostazioneDB.setObjectName("labelImpostazioneDB")
        self.labelImpostazioneSave = QtWidgets.QLabel(DialogImpostazione)
        self.labelImpostazioneSave.setGeometry(QtCore.QRect(160, 399, 51, 18))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelImpostazioneSave.setFont(font)
        self.labelImpostazioneSave.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.labelImpostazioneSave.setObjectName("labelImpostazioneSave")
        self.labelSmtpSender = QtWidgets.QLabel(DialogImpostazione)
        self.labelSmtpSender.setGeometry(QtCore.QRect(11, 66, 80, 20))
        self.labelSmtpSender.setMinimumSize(QtCore.QSize(80, 20))
        self.labelSmtpSender.setMaximumSize(QtCore.QSize(80, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.labelSmtpSender.setFont(font)
        self.labelSmtpSender.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.labelSmtpSender.setObjectName("labelSmtpSender")
        self.EditDialogSmtpSender = QtWidgets.QLineEdit(DialogImpostazione)
        self.EditDialogSmtpSender.setEnabled(True)
        self.EditDialogSmtpSender.setGeometry(QtCore.QRect(95, 63, 170, 25))
        self.EditDialogSmtpSender.setMinimumSize(QtCore.QSize(170, 25))
        self.EditDialogSmtpSender.setMaximumSize(QtCore.QSize(170, 25))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.EditDialogSmtpSender.setFont(font)
        self.EditDialogSmtpSender.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.EditDialogSmtpSender.setReadOnly(False)
        self.EditDialogSmtpSender.setObjectName("EditDialogSmtpSender")
        self.labelImpostazioneDaemonPort = QtWidgets.QLabel(DialogImpostazione)
        self.labelImpostazioneDaemonPort.setGeometry(QtCore.QRect(10, 340, 161, 18))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelImpostazioneDaemonPort.setFont(font)
        self.labelImpostazioneDaemonPort.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.labelImpostazioneDaemonPort.setObjectName("labelImpostazioneDaemonPort")
        self.line_2 = QtWidgets.QFrame(DialogImpostazione)
        self.line_2.setGeometry(QtCore.QRect(0, 330, 311, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.line_2.setFont(font)
        self.line_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.labelDaemonPort = QtWidgets.QLabel(DialogImpostazione)
        self.labelDaemonPort.setGeometry(QtCore.QRect(48, 363, 50, 20))
        self.labelDaemonPort.setMinimumSize(QtCore.QSize(50, 20))
        self.labelDaemonPort.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.labelDaemonPort.setFont(font)
        self.labelDaemonPort.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.labelDaemonPort.setObjectName("labelDaemonPort")
        self.spinBoxDaemonPort = QtWidgets.QSpinBox(DialogImpostazione)
        self.spinBoxDaemonPort.setGeometry(QtCore.QRect(95, 360, 70, 25))
        self.spinBoxDaemonPort.setMinimumSize(QtCore.QSize(70, 25))
        self.spinBoxDaemonPort.setMaximumSize(QtCore.QSize(70, 25))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.spinBoxDaemonPort.setFont(font)
        self.spinBoxDaemonPort.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.spinBoxDaemonPort.setMinimum(1)
        self.spinBoxDaemonPort.setMaximum(65535)
        self.spinBoxDaemonPort.setProperty("value", 9999)
        self.spinBoxDaemonPort.setObjectName("spinBoxDaemonPort")

        self.retranslateUi(DialogImpostazione)
        QtCore.QMetaObject.connectSlotsByName(DialogImpostazione)
        DialogImpostazione.setTabOrder(self.EditDialogSmtpServer, self.EditDialogSmtpSender)
        DialogImpostazione.setTabOrder(self.EditDialogSmtpSender, self.EditDialogSmtpUser)
        DialogImpostazione.setTabOrder(self.EditDialogSmtpUser, self.EditDialogSmtpPassword)
        DialogImpostazione.setTabOrder(self.EditDialogSmtpPassword, self.EditDialogHostname)
        DialogImpostazione.setTabOrder(self.EditDialogHostname, self.EditDialogDatabase)
        DialogImpostazione.setTabOrder(self.EditDialogDatabase, self.EditDialogUsername)
        DialogImpostazione.setTabOrder(self.EditDialogUsername, self.EditDialogPwd)
        DialogImpostazione.setTabOrder(self.EditDialogPwd, self.btSave)

    def retranslateUi(self, DialogImpostazione):
        _translate = QtCore.QCoreApplication.translate
        DialogImpostazione.setWindowTitle(_translate("DialogImpostazione", "Dialog"))
        self.labelHost.setText(_translate("DialogImpostazione", "Hostname"))
        self.labelPassword.setText(_translate("DialogImpostazione", "Password"))
        self.labelDatabase.setText(_translate("DialogImpostazione", "Database"))
        self.labelUsername.setText(_translate("DialogImpostazione", "Utente"))
        self.labelSmtpPassword.setText(_translate("DialogImpostazione", "SMTP Passwd"))
        self.labelSmtpServer.setText(_translate("DialogImpostazione", "SMTP Server"))
        self.labelSmtpUser.setText(_translate("DialogImpostazione", "SMTP User"))
        self.labelImpostazioneMail.setText(_translate("DialogImpostazione", "Impostazione Mail"))
        self.labelImpostazioneDB.setText(_translate("DialogImpostazione", "Impostazione Database"))
        self.labelImpostazioneSave.setText(_translate("DialogImpostazione", "Salva"))
        self.labelSmtpSender.setText(_translate("DialogImpostazione", "SMTP Sender"))
        self.labelImpostazioneDaemonPort.setText(_translate("DialogImpostazione", "Impostazione Servizio"))
        self.labelDaemonPort.setText(_translate("DialogImpostazione", "Port"))

