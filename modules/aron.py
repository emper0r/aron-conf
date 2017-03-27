# -*- coding: utf-8 -*-
# Copyright (c) 2016 by Antonio Peña Diaz <antonio@ctime.it>
#
# GNU General Public Licence (GPL)
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 59 Temple
# Place, Suite 330, Boston, MA  02111-1307  USA
#
# Aron Config :: License GPLv3+

import os
import platform
import base64
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch
from reportlab.platypus import TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Image
from reportlab.platypus.tables import Table
from PyQt5.Qt import *
from modules import sql_query
from modules import mainwindow_ui_l
from modules import mainwindow_ui_w
from modules import Client
from modules import Login
from modules import Hardware
from modules import Item
from modules import AddLine
from modules import ChangePasswd
from modules import codes
from modules import Users
from modules import Logs


__version__ = '1.0'


class Main(QMainWindow):
    id_image = []
    _fs = 0
    _data = ''
    _hw = ''
    _field = ''
    _value = ''
    
    def __init__(self):
        QMainWindow.__init__(self)
        if platform.system() == 'Linux':
            self.ui = mainwindow_ui_l.Ui_MainWindow()
        else:
            self.ui = mainwindow_ui_w.Ui_MainWindow()
        self.ui.setupUi(self)
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
        logo = QPixmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../QtUI', 'ctime_logo.png'))
        self.ui.labelLogo.setPixmap(logo)
        
        # Images
        plus_img = QPixmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../QtUI', 'plus.png'))
        upload_img = QPixmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../QtUI', 'upload.png'))
        download_img = QPixmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../QtUI', 'download.png'))
        plus_hw_img = QPixmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../QtUI', 'plus.png'))
        plus_item_img = QPixmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../QtUI', 'plus.png'))
        plus_client_img = QPixmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../QtUI', 'plus.png'))
        plus_foto_img = QPixmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../QtUI', 'add_photo.png'))
        minus_img = QPixmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../QtUI', 'minus.png'))
        trash_img = QPixmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../QtUI', 'trash.png'))
        minus_hw_img = QPixmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../QtUI', 'minus.png'))
        minus_item_img = QPixmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../QtUI', 'minus.png'))
        minus_client_img = QPixmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../QtUI', 'minus.png'))
        minus_foto_img = QPixmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../QtUI', 'delete_photo.png'))
        pass_img = QPixmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../QtUI', 'password.png'))
        login_img = QPixmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../QtUI', 'login.png'))
        logout_img = QPixmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../QtUI', 'logout.png'))
        users_img = QPixmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../QtUI', '../QtUI/users.png'))
        logs = QPixmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../QtUI', 'log.png'))
        pdf = QPixmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../QtUI', 'pdf.png'))
        save = QPixmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../QtUI', 'save.png'))
        modify = QPixmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../QtUI', 'modify.png'))

        # GUI
        self.ui.tableWidget.setColumnWidth(3, 562)
        self.ui.tableWidgetImg.clicked.connect(self.img)
        self.ui.tableWidget_attachments.clicked.connect(self._readFile)
        
        self.ui.cbClient.clear()
        self.ui.cbClient.addItem('Seleziona')
        self.ui.cbClient.currentTextChanged['QString'].connect(self._table_view)
        self.ui.cbClient.currentTextChanged['QString'].connect(self.update_hardware)
        self.ui.cbClient.currentTextChanged['QString'].connect(self._table_foto)
        
        self.ui.btPlus.setIcon(QIcon(plus_img))
        self.ui.btPlus.setToolTip('Aggiungi configurazione')
        self.ui.btPlus.setToolTipDuration(10000)
        
        self.ui.btUpload.setIcon(QIcon(upload_img))
        self.ui.btUpload.setToolTip('Aggiungi file')
        self.ui.btUpload.setToolTipDuration(10000)
        
        self.ui.btDownload.setIcon(QIcon(download_img))
        self.ui.btDownload.setToolTip('Scarica file')
        self.ui.btDownload.setToolTipDuration(10000)
        
        self.ui.btHwPlus.setIcon(QIcon(plus_hw_img))
        self.ui.btHwPlus.setToolTip('Aggiungi Hardware')
        self.ui.btHwPlus.setToolTipDuration(10000)
        
        self.ui.btItemPlus.setIcon(QIcon(plus_item_img))
        self.ui.btItemPlus.setToolTip('Aggiungi Campo per il Hardware')
        self.ui.btItemPlus.setToolTipDuration(10000)
        
        self.ui.btClientPlus.setIcon(QIcon(plus_client_img))
        self.ui.btClientPlus.setToolTip('Aggiungi Nuovo Cliente')
        self.ui.btClientPlus.setToolTipDuration(10000)
        
        self.ui.btPlus_foto.setIcon(QIcon(plus_foto_img))
        self.ui.btPlus_foto.setText('Aggiungi')
        self.ui.btPlus_foto.setToolTipDuration(10000)
        
        self.ui.btMinus.setIcon(QIcon(minus_img))
        self.ui.btMinus.setToolTip('Cancella configurazione')
        self.ui.btMinus.setToolTipDuration(10000)
        
        self.ui.btTrash.setIcon(QIcon(trash_img))
        self.ui.btTrash.setToolTip('Cancella file')
        self.ui.btTrash.setToolTipDuration(10000)
        
        self.ui.btHwMinus.setIcon(QIcon(minus_hw_img))
        self.ui.btHwMinus.setToolTip('Cancella Hardware selezzionato')
        self.ui.btHwMinus.setToolTipDuration(10000)
        
        self.ui.btItemMinus.setIcon(QIcon(minus_item_img))
        self.ui.btItemMinus.setToolTip('Cancella Campo selezzionato')
        self.ui.btItemMinus.setToolTipDuration(10000)
        
        self.ui.btClientMinus.setIcon(QIcon(minus_client_img))
        self.ui.btClientMinus.setToolTip('Cancella Cliente con tutti i suoi dati')
        
        self.ui.btMinus_foto.setIcon(QIcon(minus_foto_img))
        self.ui.btMinus_foto.setText('Cancella')

        self.ui.btSaveModify.setIcon(QIcon(save))
        self.ui.btSaveModify.setText('Modifica')
        
        self.ui.btPassword.setIcon(QIcon(pass_img))
        self.ui.btPassword.setToolTip('Cambio password attuale')
        self.ui.btPassword.setToolTipDuration(10000)
        
        self.ui.btLogin.setIcon(QIcon(login_img))
        self.ui.btLogin.setToolTip('Login')
        self.ui.btLogin.setToolTipDuration(10000)
        
        self.ui.btLogout.setIcon(QIcon(logout_img))
        self.ui.btLogout.setToolTip('Uscire del programa')
        self.ui.btLogout.setToolTipDuration(10000)
        
        self.ui.btUsers.setIcon(QIcon(users_img))
        self.ui.btUsers.setToolTip('Lista utenti per l\'accesso al sistema')
        self.ui.btUsers.setToolTipDuration(10000)
        
        self.ui.btLogs.setIcon(QIcon(logs))
        self.ui.btLogs.setToolTip('Logs del sistema')
        self.ui.btLogs.setToolTipDuration(10000)
        
        self.ui.btPDF.setIcon(QIcon(pdf))
        self.ui.btPDF.setToolTip('Salva in formato PDF')
        self.ui.btPDF.setToolTipDuration(10000)
        
        self.ui.btSave.setIcon(QIcon(save))
        self.ui.btSave.setToolTip('Salva cambiamenti')
        self.ui.btSave.setToolTipDuration(10000)
        
        self.ui.btModify.setIcon(QIcon(modify))
        self.ui.btModify.setToolTip('Abilita modifica')
        self.ui.btModify.setToolTipDuration(10000)
        
        # Button events
        self.ui.btClientPlus.clicked.connect(self._new_client)
        self.ui.btClientMinus.clicked.connect(self._delete_client)
        
        self.ui.btHwPlus.clicked.connect(self._new_hardware)
        self.ui.btHwMinus.clicked.connect(self._delete_hardware)
        
        self.ui.btItemPlus.clicked.connect(self._new_item)
        self.ui.btItemMinus.clicked.connect(self._delete_item)
        
        self.ui.btPlus.clicked.connect(self._add_line)
        self.ui.btMinus.clicked.connect(self._delete_line)

        self.ui.btPlus_foto.clicked.connect(self._add_foto)
        self.ui.btMinus_foto.clicked.connect(self._del_foto)
        
        self.ui.btPassword.clicked.connect(self._change_pwd)
        
        self.ui.btLogin.clicked.connect(self._login)
        
        self.ui.btLogout.clicked.connect(self._ready)
        
        self.ui.btUsers.clicked.connect(self.utenti)
        
        self.ui.btLogs.clicked.connect(self.logs)
        
        self.ui.btPDF.clicked.connect(self._pdf)
        
        self.ui.btUpload.clicked.connect(self._uploadFile)
        
        self.ui.btDownload.clicked.connect(self._downloadFile)
        
        self.ui.btTrash.clicked.connect(self._deleteFile)
        
        self.ui.btSave.clicked.connect(self._save_text)
        
        self.ui.btModify.clicked.connect(self._modify_enabled)
        
        self.ui.labelFoto.mousePressEvent = self.img_normal_size
        
        self.ui.tableWidget.doubleClicked.connect(self._freeze_table)
        self.ui.btSaveModify.clicked.connect(self._unfreeze_table)
        
        self._want_to_close = False
        
        self._ready()

    def _ready(self):
        for i in reversed(range(self.ui.tableWidget.rowCount())):
            self.ui.tableWidget.removeRow(i)
        for i in reversed(range(self.ui.tableWidgetImg.rowCount())):
            self.ui.tableWidgetImg.removeRow(i)
        for i in reversed(range(self.ui.tableWidget_attachments.rowCount())):
            self.ui.tableWidget_attachments.removeRow(i)
        self.ui.plainTextEdit.clear()
        self.ui.cbClient.clear()
        self.ui.cbHardware.clear()
        self.ui.cbItem.clear()
        self.ui.cbClient.setDisabled(True)
        self.ui.cbHardware.setDisabled(True)
        self.ui.cbItem.setDisabled(True)
        self.ui.btClientMinus.setDisabled(True)
        self.ui.btClientPlus.setDisabled(True)
        self.ui.btHwMinus.setDisabled(True)
        self.ui.btHwPlus.setDisabled(True)
        self.ui.btItemMinus.setDisabled(True)
        self.ui.btItemPlus.setDisabled(True)
        self.ui.btPlus.setDisabled(True)
        self.ui.btMinus.setDisabled(True)
        self.ui.btPlus_foto.setDisabled(True)
        self.ui.btMinus_foto.setDisabled(True)
        self.ui.labelLogo.setDisabled(True)
        self.ui.tableWidget.setDisabled(True)
        self.ui.tableWidgetImg.setDisabled(True)
        self.ui.labelFoto.setDisabled(True)
        self.ui.btPDF.setHidden(True)
        self.ui.btPassword.setDisabled(True)
        self.ui.btLogin.setEnabled(True)
        self.ui.btUsers.setHidden(True)
        self.ui.btLogs.setHidden(True)
        self.ui.btLogin.setFocus(True)
        self.ui.plainTextEdit.setDisabled(True)
        self.ui.plainTextEdit.setReadOnly(True)
        self.ui.tab_attachments.setDisabled(True)
        self.ui.btSave.setDisabled(True)
        self.ui.labelupdate.setDisabled(True)
        self.ui.labelallowmodify.setDisabled(True)
        self.ui.btModify.setDisabled(True)
        self.ui.btUpload.setDisabled(True)
        self.ui.btDownload.setDisabled(True)
        self.ui.btTrash.setDisabled(True)
        self.ui.btSaveModify.setDisabled(True)
        self.no_image()
        sql_query.Q(action='log', kwargs=[self.ui.labelUserName.text(), codes.msg(code=402)])

    def _login(self):
        login = Login.DialogLogin()
        login.exec_()
        try:
            if int(login.Accepted) is 1:
                self.ui.labelUserName.setText(login._login)
                self.ui.cbClient.setDisabled(False)
                self.ui.cbHardware.setDisabled(False)
                self.ui.cbItem.setDisabled(False)
                self.ui.btClientMinus.setDisabled(False)
                self.ui.btClientPlus.setDisabled(False)
                self.ui.btHwMinus.setDisabled(False)
                self.ui.btHwPlus.setDisabled(False)
                self.ui.btItemMinus.setDisabled(False)
                self.ui.btItemPlus.setDisabled(False)
                self.ui.btPlus.setDisabled(False)
                self.ui.btMinus.setDisabled(False)
                self.ui.btPlus_foto.setDisabled(False)
                self.ui.btMinus_foto.setDisabled(False)
                self.ui.labelLogo.setDisabled(False)
                self.ui.btPassword.setDisabled(False)
                self.ui.tableWidget.setDisabled(False)
                self.ui.tableWidgetImg.setDisabled(False)
                self.ui.labelFoto.setDisabled(False)
                self.ui.tab_attachments.setDisabled(False)
                self.ui.plainTextEdit.setDisabled(True)
                self.ui.plainTextEdit.setReadOnly(True)
                self.ui.btSave.setDisabled(True)
                self.ui.labelupdate.setDisabled(True)
                self.ui.labelallowmodify.setDisabled(True)
                self.ui.btModify.setDisabled(True)
                self.ui.btLogin.setDisabled(True)
                self.ui.btSaveModify.setDisabled(True)
                self.ui.btUpload.setDisabled(False)
                self.ui.btDownload.setDisabled(False)
                self.ui.btTrash.setDisabled(True)
                if login._login == 'admin':
                    self.ui.btUsers.setHidden(False)
                    self.ui.btPDF.setHidden(False)
                    self.ui.btLogs.setHidden(False)
                    self.ui.btMinus_foto.setDisabled(False)
                    self.ui.btTrash.setDisabled(False)
                    sql_query.Q(action='log', kwargs=[self.ui.labelUserName.text(), codes.msg(code=405) + 'admin'])
                else:
                    self.ui.btMinus_foto.setDisabled(True)
                    self.ui.btTrash.setDisabled(True)
                    self.ui.btUsers.setHidden(True)
                    self.ui.btPDF.setHidden(True)
                    self.ui.btLogs.setHidden(True)
                    sql_query.Q(action='log', kwargs=[self.ui.labelUserName.text(), codes.msg(code=405) + self.ui.labelUserName.text()])
                self.ui.cbClient.setFocus(True)
                self.list_clients()
        except:
            QMessageBox.about(self, 'Attenzione', codes.msg(code=401))

    def list_clients(self):
        self.ui.cbClient.clear()
        self.ui.cbClient.addItem('Seleziona')
        client = sql_query.Q(action="AllClients")
        for item in range(0, len(client)):
            self.ui.cbClient.addItem(client[item][0])
        self.no_image()

    def no_image(self):
        self.ui.labelFoto.setPixmap(QPixmap("QtUI/no_image.png"))
        self.ui.labelFoto.setScaledContents(True)

    def update_client(self):
        self.ui.cbClient.clear()
        client = sql_query.Q(action="AllClients")
        self.ui.cbHardware.addItem('Seleziona')
        if len(client) > 0:
            for item in range(0, len(client)):
                self.ui.cbClient.addItem(client[item][0])
        self.no_image()
        self.update_hardware()

    def utenti(self):
        dialog = Users.DialogUsers()
        dialog.exec_()

    def update_hardware(self):
        self.ui.cbHardware.clear()
        self.ui.cbHardware.addItem('Seleziona')
        hardware = sql_query.Q(action="AllHw", kwargs=[self.ui.cbClient.currentText()])
        if self.ui.cbClient.currentText() == 'Seleziona':
            self.ui.cbItem.clear()
            self.ui.cbItem.addItem('Seleziona')
        else:
            for item in range(0, len(hardware)):
                self.ui.cbHardware.addItem(hardware[item][0])
            self.ui.cbHardware.itemText(0)
            self.update_items()

    def update_items(self):
        self.ui.cbItem.clear()
        self.ui.cbItem.addItem('Seleziona')
        items = sql_query.Q(action="AllItems", kwargs=[self.ui.cbClient.currentText()])
        for item in range(0, len(items)):
            self.ui.cbItem.addItem(items[item][0])
        self.ui.cbItem.itemText(0)

    def _new_client(self):
        dialog = Client.DialogNewClient()
        dialog.exec_()
        if int(dialog.Accepted) is 1:
            value = dialog.getValues()
            msg = codes.msg(code=105) + '%s' % value
            sql_query.Q(action='log', kwargs=[self.ui.labelUserName.text(), codes.msg(code=105) + '%s' % value])
            self.statusBar().showMessage(msg, 4000)
            self.update_client()
            self.no_image()

    def _new_hardware(self):
        if self.ui.cbClient.currentIndex() == 'Seleziona':
            self.statusBar().showMessage(codes.msg(code=301), 4000)
        else:
            dialog = Hardware.DialogNewHardware()
            dialog.data(str=self.ui.cbClient.currentText())
            dialog.exec_()
            if int(dialog.Accepted) is 1:
                value = dialog.getValues()
                self.statusBar().showMessage(codes.msg(code=103), 4000)
                sql_query.Q(action='log', kwargs=[self.ui.labelUserName.text(), codes.msg(code=103) + value + ' cliente ' + self.ui.cbClient.currentText()])
                self.update_hardware()

    def _new_item(self):
        if self.ui.cbClient.currentText() == 'Seleziona':
            self.statusBar().showMessage(codes.msg(code=301), 4000)
        elif self.ui.cbHardware.currentText() == 'Seleziona':
            self.statusBar().showMessage(codes.msg(code=301), 4000)
        else:
            dialog = Item.DialogNewItem()
            dialog.data(str_hw=self.ui.cbHardware.currentText(), str_client=self.ui.cbClient.currentText())
            dialog.exec_()
            if int(dialog.Accepted) is 1:
                value = dialog.getValues()
                self.statusBar().showMessage(codes.msg(code=102), 4000)
                sql_query.Q(action='log', kwargs=[self.ui.labelUserName.text(), codes.msg(code=102) + value + ' cliente' + self.ui.cbClient.currentText()])
                self.update_items()

    def _add_line(self):
        if self.ui.cbClient.currentText() == 'Seleziona' \
            or self.ui.cbHardware.currentText() == 'Seleziona' \
                or self.ui.cbItem.currentText() == 'Seleziona':
            self.statusBar().showMessage(codes.msg(code=302), 4000)
        else:
            plus = AddLine.DialogAddLine()
            plus.data(str_hw=self.ui.cbHardware.currentText(),
                      str_item=self.ui.cbItem.currentText(),
                      str_client=self.ui.cbClient.currentText())
            plus.exec_()
            if int(plus.Accepted) is 1:
                value = plus.getValues()
                self.statusBar().showMessage(codes.msg(code=100), 4000)
                sql_query.Q(action='log', kwargs=[self.ui.labelUserName.text(), str(codes.msg(code=106)) + ' ' + str(value[0]) + ' cliente ' + str(self.ui.cbClient.currentText())])
                self._table_view()

    def _delete_line(self):
        try:
            data = self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 0).text()
            hardware = self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 1).text()
            item = self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 2).text()
            value = self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 3).text()
            reply = QMessageBox.question(self, 'Attenzione!', codes.msg(code=201), QMessageBox.Yes, QMessageBox.No)
            if reply == QMessageBox.Yes:
                sql_query.Q(action='deleteRow', kwargs=[data, hardware, item, value])
                sql_query.Q(action='log', kwargs=[self.ui.labelUserName.text(), codes.msg(code=107) + self.ui.cbClient.currentText()])
                self.statusBar().showMessage(codes.msg(code=100), 4000)
                self._table_view()
        except:
            self.statusBar().showMessage(codes.msg(code=303), 4000)

    def _delete_client(self):
        if self.ui.cbClient.currentText() != 'Seleziona':
            reply = QMessageBox.question(self, 'Attenzione!', codes.msg(code=202) + '%s ?' % self.ui.cbClient.currentText(), QMessageBox.Yes, QMessageBox.No)
            if reply == QMessageBox.Yes:
                sql_query.Q(action='deleteClient', kwargs=[self.ui.cbClient.currentText()])
                sql_query.Q(action='log', kwargs=[self.ui.labelUserName.text(), codes.msg(code=108) + self.ui.cbClient.currentText()])
                self.statusBar().showMessage(codes.msg(code=100), 4000)
                self.update_client()
                self._table_view()
                self._table_foto()
        else:
            self.statusBar().showMessage(codes.msg(code=301), 4000)

    def _delete_item(self):
        if self.ui.cbHardware.currentText() == 'Seleziona':
            QMessageBox.about(self, 'Attenzione', codes.msg(code=305))
        else:
            if self.ui.cbItem.currentText() != 'Seleziona':
                reply = QMessageBox.question(self, 'Attenzione!', codes.msg(code=201) + '%s ?' % self.ui.cbItem.currentText(), QMessageBox.Yes, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    sql_query.Q(action='deleteItem', kwargs=[self.ui.cbClient.currentText(), self.ui.cbHardware.currentText(), self.ui.cbItem.currentText()])
                    sql_query.Q(action='log', kwargs=[self.ui.labelUserName.text(), codes.msg(code=109) + self.ui.cbItem.currentText() + 'cliente ' + self.ui.cbClient.currentText()])
                    self.statusBar().showMessage(codes.msg(code=100), 4000)
                    self.update_items()
                    self._table_view()
            else:
                QMessageBox.about(self, 'Attenzione', codes.msg(code=304))

    def _delete_hardware(self):
        if self.ui.cbHardware.currentText() != 'Seleziona':
            reply = QMessageBox.question(self, 'Attenzione!', codes.msg(code=201) + '%s ?' % self.ui.cbHardware.currentText(), QMessageBox.Yes, QMessageBox.No)
            if reply == QMessageBox.Yes:
                sql_query.Q(action='deleteHardware', kwargs=[self.ui.cbHardware.currentText()])
                sql_query.Q(action='log', kwargs=[self.ui.labelUserName.text(), codes.msg(
                    code=110) + self.ui.cbHardware.currentText() + 'cliente ' + self.ui.cbClient.currentText()])
                self.statusBar().showMessage(codes.msg(code=100), 4000)
                self.update_hardware()
                self._table_view()
        else:
            self.statusBar().showMessage(codes.msg(code=305), 4000)

    def _table_view(self):
        self.ui.plainTextEdit.clear()
        self.ui.btSave.setDisabled(True)
        self.ui.labelupdate.setDisabled(True)
        self.ui.plainTextEdit.setDisabled(True)
        self.ui.plainTextEdit.setReadOnly(True)
        for i in reversed(range(self.ui.tableWidget.rowCount())):
            self.ui.tableWidget.removeRow(i)
        tmp_values = sql_query.Q(action='tableView', kwargs=[self.ui.cbClient.currentText()])
        db_table = sorted(tmp_values)
        for row in range(0, len(db_table)):
            self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())
            for colum in range(0, 4):
                value = QTableWidgetItem(str(db_table[row][colum]), 0)
                self.ui.tableWidget.setItem(row, colum, value)
                colum += 1
            row += 1
        if self.ui.cbClient.currentText() == '' or self.ui.cbClient.currentText() == 'Seleziona':
            return
        else:
            self._table_files()

    def _change_pwd(self):
        changePasswd = ChangePasswd.DialogChangePwd()
        changePasswd.data(str=self.ui.labelUserName.text())
        changePasswd.exec_()
        if int(changePasswd.Accepted) is 1:
            sql_query.Q(action='log', kwargs=[self.ui.labelUserName.text(), codes.msg(code=104)])
            #self.statusBar().showMessage(codes.msg(code=104), 2000)

    def quit(self):
        sql_query.Q(action='log', kwargs=[self.ui.labelUserName.text(), codes.msg(code=402)])
        qApp.exit(0)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            sql_query.Q(action='log', kwargs=[self.ui.labelUserName.text(), codes.msg(code=402)])
            qApp.exit(0)

    def _uploadFile(self):
        if self.ui.cbClient.currentText() == 'Seleziona':
            self.statusBar().showMessage(codes.msg(code=301), 4000)
        else:
            dlg = QFileDialog()
            dlg.setFileMode(QFileDialog.AnyFile)
            fname = dlg.getOpenFileNames()
            try:
                for item in range(0, len(fname)):
                    if str(fname[0][item])[-3:] == 'txt' or \
                            str(fname[0][item])[-3:] == 'rtf' or \
                            str(fname[0][item])[-3:] == 'xls' or \
                            str(fname[0][item])[-3:] == 'lsx' or \
                            str(fname[0][item])[-3:] == 'onf' or \
                            str(fname[0][item])[-3:] == 'sql' or \
                            str(fname[0][item])[-3:] == 'doc' or \
                            str(fname[0][item])[-3:] == 'ocx' or \
                            str(fname[0][item])[-3:] == 'pdf' or \
                            str(fname[0][item])[-3:] == 'xml' or \
                            str(fname[0][item])[-3:] == 'dat':
                        sql_query.Q('upload', kwargs=[self.ui.cbClient.currentText(), fname[0][item]])
                        self._table_files()
                        self.statusBar().showMessage(codes.msg(code=101), 4000)
                        sql_query.Q(action='log', kwargs=[self.ui.labelUserName.text(), codes.msg(code=406) + str(fname[0][item]) + ' per il cliente ' + self.ui.cbClient.currentText()])
                    else:
                        pass
            except:
                pass

    def _readFile(self):
        if str(self.ui.tableWidget_attachments.item(self.ui.tableWidget_attachments.currentRow(), self.ui.tableWidget_attachments.currentColumn()).text())[-3:] == 'txt':
            file = sql_query.Q(action='load_file', kwargs=[self.ui.cbClient.currentText(), str(self.ui.tableWidget_attachments.item(self.ui.tableWidget_attachments.currentRow(), self.ui.tableWidget_attachments.currentColumn()).text())])
            sql_query.Q(action='log', kwargs=[self.ui.labelUserName.text(), codes.msg(code=407) + 'cliente ' + self.ui.cbClient.currentText()])
            self.ui.plainTextEdit.setPlainText(file[0][0])
            self.ui.labelallowmodify.setDisabled(False)
            self.ui.btModify.setDisabled(False)
            self.ui.plainTextEdit.setDisabled(False)
            self.ui.plainTextEdit.setReadOnly(True)
        else:
            self.ui.plainTextEdit.clear()
            self.ui.labelallowmodify.setDisabled(True)
            self.ui.labelupdate.setDisabled(True)
            self.ui.btModify.setDisabled(True)
            self.ui.plainTextEdit.setDisabled(True)
            self.ui.plainTextEdit.setReadOnly(False)
            self.ui.btSave.setDisabled(True)

    def _deleteFile(self):
        if self.ui.cbClient.currentText() == 'Seleziona':
            self.statusBar().showMessage(codes.msg(code=301), 4000)
        else:
            if self.ui.tableWidget_attachments.rowCount() is 0:
                self.statusBar().showMessage(codes.msg(code=303), 4000)
            else:
                reply = QMessageBox.question(self, 'Attenzione!', codes.msg(code=203) + '%s ?' % self.ui.cbClient.currentText(), QMessageBox.Yes, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    sql_query.Q(action='log', kwargs=[self.ui.labelUserName.text(),
                                                      codes.msg(code=408) +
                                                      self.ui.tableWidget_attachments.item(self.ui.tableWidget_attachments.currentRow(), self.ui.tableWidget_attachments.currentColumn()).text() +
                                                      ' dal cliente ' + self.ui.cbClient.currentText()])
                    sql_query.Q(action='delete_file', kwargs=[self.ui.cbClient.currentText(),
                                                              self.ui.tableWidget_attachments.item(self.ui.tableWidget_attachments.currentRow(), self.ui.tableWidget_attachments.currentColumn()).text()])
                    self._table_files()
                    self._table_view()
                    
                    self.statusBar().showMessage(codes.msg(code=100), 4000)
                else:
                    pass
    
    def _downloadFile(self):
        buffer = sql_query.Q(action='load_file', kwargs=[self.ui.cbClient.currentText(),
                                                       str(self.ui.tableWidget_attachments.item(self.ui.tableWidget_attachments.currentRow(), self.ui.tableWidget_attachments.currentColumn()).text())])
        filename = QFileDialog.getSaveFileName(self, 'Save File', os.path.expanduser("~"))
        f = open(filename[0] + str(self.ui.tableWidget_attachments.item(self.ui.tableWidget_attachments.currentRow(), self.ui.tableWidget_attachments.currentColumn()).text()), 'w')
        filedata = str(buffer[0][0])
        f.write(filedata)
        f.close()
        sql_query.Q(action='log', kwargs=[self.ui.labelUserName.text(),
                                          codes.msg(code=409) +
                                          self.ui.tableWidget_attachments.item(self.ui.tableWidget_attachments.currentRow(), self.ui.tableWidget_attachments.currentColumn()).text() +
                                          ' dal cliente ' + self.ui.cbClient.currentText()])
        
    def _modifyFile(self):
        self.ui.btSave.setDisabled(False)
        self.ui.labelupdate.setDisabled(False)
        self.ui.plainTextEdit.setDisabled(False)
        self.ui.plainTextEdit.setReadOnly(False)
        self.ui.labelallowmodify.setDisabled(True)
        self.ui.btModify.setDisabled(False)
    
    def _modify_enabled(self):
        self.ui.plainTextEdit.setReadOnly(False)
        self.ui.btModify.setDisabled(True)
        self.ui.labelallowmodify.setDisabled(True)
        self.ui.btSave.setDisabled(False)
        self.ui.labelupdate.setDisabled(False)
    
    def _save_text(self):
        self.ui.btSave.setDisabled(True)
        self.ui.labelupdate.setDisabled(True)
        self.ui.plainTextEdit.setReadOnly(True)
        self.ui.btModify.setDisabled(False)
        self.ui.labelallowmodify.setDisabled(False)
        txt = self.ui.plainTextEdit.toPlainText()
        sql_query.Q(action='update_text', kwargs=[self.ui.cbClient.currentText(),
                                                  self.ui.tableWidget_attachments.item(self.ui.tableWidget_attachments.currentRow(), self.ui.tableWidget_attachments.currentColumn()).text(),
                                                  txt])
        self.statusBar().showMessage(codes.msg(code=100), 4000)
        sql_query.Q(action='log', kwargs=[self.ui.labelUserName.text(),
                                          codes.msg(code=410) +
                                          self.ui.tableWidget_attachments.item(self.ui.tableWidget_attachments.currentRow(), self.ui.tableWidget_attachments.currentColumn()).text() +
                                          ' dal cliente ' + self.ui.cbClient.currentText()])

    def _table_files(self):
        files = sql_query.Q(action='files', kwargs=[self.ui.cbClient.currentText()])
        for i in reversed(range(self.ui.tableWidget_attachments.rowCount())):
            self.ui.tableWidget_attachments.removeRow(i)
        for row in range(0, len(files)):
            self.ui.tableWidget_attachments.insertRow(self.ui.tableWidget_attachments.rowCount())
            value = QTableWidgetItem(str(files[row][0]), 0)
            self.ui.tableWidget_attachments.setItem(row, 0, value)
    
    def _add_foto(self):
        if self.ui.cbClient.currentText() == 'Seleziona':
            self.statusBar().showMessage(codes.msg(code=302), 4000)
        else:
            dlg = QFileDialog()
            dlg.setFileMode(QFileDialog.AnyFile)
            fname = dlg.getOpenFileNames()
            for item in range(0, len(fname[0])):
                if str(fname[0][item])[-3:] == 'png' or str(fname[0][item])[-3:] == 'bmp' or str(fname[0])[-3:] == 'jpg':
                    self.ui.labelFoto.setPixmap(QPixmap(fname[0][item]))
                    self.ui.labelFoto.setScaledContents(True)
                    self._table_foto()
                    sql_query.Q('save_foto', kwargs=[self.ui.cbClient.currentText(), fname[0][item]])
                    sql_query.Q(action='log', kwargs=[self.ui.labelUserName.text(), codes.msg(code=112) + 'cliente ' + self.ui.cbClient.currentText()])
                    self._table_foto()
                else:
                    self.statusBar().showMessage(codes.msg(code=101), 4000)

    def _table_foto(self):
        _img = []
        if self.ui.cbClient.currentText() == 'Seleziona' or self.ui.cbClient.currentText() == '':
            self.statusBar().showMessage(codes.msg(code=302), 4000)
            self.no_image()
        else:
            try:
                image = sql_query.Q(action='load_foto', kwargs=[self.ui.cbClient.currentText()])
                for i in reversed(range(self.ui.tableWidgetImg.rowCount())):
                    self.ui.tableWidgetImg.removeRow(i)
                for row in range(0, len(image)):
                    self.ui.tableWidgetImg.insertRow(self.ui.tableWidgetImg.rowCount())
                    pix = QPixmap()
                    pix.loadFromData(base64.b64decode(image[row][0]))
                    img = QLabel(self)
                    img.setPixmap(QPixmap(pix).scaled(64, 64, Qt.KeepAspectRatio))
                    img.setScaledContents(False)
                    self.ui.tableWidgetImg.setCellWidget(row, 0, img)
                    _img.append(image[row][1])
                self.id_image = _img
                self.no_image()
            except:
                self.no_image()
    
    def img(self):
        img_idx = self.ui.tableWidgetImg.currentRow()
        photo = sql_query.Q(action='tableView_Img', kwargs=[self.id_image[img_idx]])
        sql_query.Q(action='log', kwargs=[self.ui.labelUserName.text(),
                                          codes.msg(code=111) + 'cliente ' + self.ui.cbClient.currentText()])
        pix = QPixmap()
        pix.loadFromData(base64.b64decode(photo[0][0]))
        img = QLabel(self)
        img.setPixmap(QPixmap(pix).scaled(1031, 591))
        self.ui.labelFoto.setScaledContents(True)
        self.ui.labelFoto.setPixmap(QPixmap(pix))

    def img_normal_size(self, event):
        if self._fs == 1:
            self.ui.labelFoto.setGeometry(260, 9, 1031, 591)
            self._fs = 0
        else:
            self.ui.labelFoto.setGeometry(260, 9, 1031, 591)
            #self.ui.labelFoto.setGeometry(0, 0, 1030, 700)
            self._fs = 1

    def _del_foto(self):
        if self.ui.cbClient.currentText() == 'Seleziona':
            self.statusBar().showMessage(codes.msg(code=302), 4000)
        else:
            if self.ui.tableWidgetImg.currentRow() == -1:
                self.statusBar().showMessage(codes.msg(code=306), 2000)
            else:
                reply = QMessageBox.question(self, 'Attenzione!', codes.msg(code=203) + '%s ?' % self.ui.cbClient.currentText(), QMessageBox.Yes, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    sql_query.Q(action='delete_Img', kwargs=[int(self.id_image[self.ui.tableWidgetImg.currentRow()])])
                    sql_query.Q(action='log', kwargs=[self.ui.labelUserName.text(),
                                                      codes.msg(code=113) + 'cliente ' + self.ui.cbClient.currentText()])
                    self._table_foto()
                    self.statusBar().showMessage(codes.msg(code=100), 4000)

    def logs(self):
        dialog = Logs.DialogLogs()
        dialog.exec_()

    def _pdf(self):
        if self.ui.cbClient.currentText() != 'Seleziona':
            values = sql_query.Q(action='tableView', kwargs=[self.ui.cbClient.currentText()])
            items = sorted(values)

            elements = []

            logo = Image("QtUI/ctime_logo.png", inch, inch)
            elements.append(logo)

            doc = SimpleDocTemplate("ctime_" + self.ui.cbClient.currentText() + ".pdf",
                                    pagesize=A4, rightMargin=30, leftMargin=30, topMargin=30,
                                    bottomMargin=18)

            style = TableStyle([('ALIGN', (1, 1), (-2, -2), 'RIGHT'),
                                ('TEXTCOLOR', (1, 1), (-2, -2), colors.red),
                                ('VALIGN', (0, 0), (0, -1), 'TOP'),
                                ('TEXTCOLOR', (0, 0), (0, -1), colors.blue),
                                ('ALIGN', (0, -1), (-1, -1), 'CENTER'),
                                ('VALIGN', (0, -1), (-1, -1), 'MIDDLE'),
                                ('TEXTCOLOR', (0, -1), (-1, -1), colors.green),
                                ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                                ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                                ])

            s = getSampleStyleSheet()
            s = s["Normal"]
            s.wordWrap = 'CJK'

            elements.append(Paragraph('', s))
            elements.append(Spacer(1, 12))
            elements.append(Paragraph('Configurazione Cliente: ' + self.ui.cbClient.currentText(), s))
            elements.append(Spacer(1, 12))
            elements.append(Paragraph('', s))

            data = [[Paragraph(str(cell), s) for cell in row]
                    for row in items]
            t = Table(data)
            t.setStyle(style)

            elements.append(t)
            doc.build(elements)
            sql_query.Q(action='log', kwargs=[self.ui.labelUserName.text(),
                                              codes.msg(code=500) + 'cliente ' + self.ui.cbClient.currentText()])
            self.statusBar().showMessage(codes.msg(code=500), 4000)
        else:
            QMessageBox.about(self, 'Attenzione', codes.msg(code=301))

    def _freeze_table(self):
        self._data = self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 0).text()
        self._hw = self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 1).text()
        self._field = self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 2).text()
        self._value = self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 3).text()
        self.ui.cbClient.setDisabled(True)
        self.ui.cbHardware.setDisabled(True)
        self.ui.cbItem.setDisabled(True)
        self.ui.btClientMinus.setDisabled(True)
        self.ui.btClientPlus.setDisabled(True)
        self.ui.btHwMinus.setDisabled(True)
        self.ui.btHwPlus.setDisabled(True)
        self.ui.btItemMinus.setDisabled(True)
        self.ui.btItemPlus.setDisabled(True)
        self.ui.btPlus.setDisabled(True)
        self.ui.btMinus.setDisabled(True)
        self.ui.btPlus_foto.setDisabled(True)
        self.ui.btMinus_foto.setDisabled(True)
        self.ui.btSaveModify.setDisabled(False)
    
    def _unfreeze_table(self):
        self.ui.btSaveModify.setDisabled(True)
        self.ui.cbClient.setDisabled(False)
        self.ui.cbHardware.setDisabled(False)
        self.ui.cbItem.setDisabled(False)
        self.ui.btClientMinus.setDisabled(False)
        self.ui.btClientPlus.setDisabled(False)
        self.ui.btHwMinus.setDisabled(False)
        self.ui.btHwPlus.setDisabled(False)
        self.ui.btItemMinus.setDisabled(False)
        self.ui.btItemPlus.setDisabled(False)
        self.ui.btPlus.setDisabled(False)
        self.ui.btMinus.setDisabled(False)
        self.ui.btPlus_foto.setDisabled(False)
        self.ui.btMinus_foto.setDisabled(False)
        client = self.ui.cbClient.currentText()
        data = self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 0).text()
        hardware = self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 1).text()
        field = self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 2).text()
        value = self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 3).text()
        sql_query.Q(action='update_conf', kwargs=[data, hardware, field, value,
                    self._data, self._hw, self._field, self._value, client])
        self._table_view()
        self.statusBar().showMessage(codes.msg(code=100), 4000)
