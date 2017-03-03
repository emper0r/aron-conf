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
import base64
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch
from reportlab.platypus import TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Image
from reportlab.platypus.tables import Table
from PyQt5.Qt import *
from modules import sql_query
from modules import mainwindow_ui
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

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = mainwindow_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
        self.ui.tableWidget.setColumnWidth(2, 345)
        self.ui.cbClient.clear()
        self.ui.cbClient.addItem('Seleziona')
        self.ui.cbClient.currentTextChanged['QString'].connect(self._table_view)
        self.ui.cbClient.currentTextChanged['QString'].connect(self.update_hardware)
        self.ui.cbClient.currentTextChanged['QString'].connect(self._table_foto)
        self.ui.tableWidgetImg.clicked.connect(self.img)
        plus_img = QPixmap("QtUI/plus.png")
        self.ui.btPlus.setIcon(QIcon(plus_img))
        self.ui.btPlus.setToolTip('Aggiungi configurazione')
        self.ui.btPlus.setToolTipDuration(10000)
        plus_hw_img = QPixmap("QtUI/plus.png")
        self.ui.btHwPlus.setIcon(QIcon(plus_hw_img))
        self.ui.btHwPlus.setToolTip('Aggiungi Hardware')
        self.ui.btHwPlus.setToolTipDuration(10000)
        plus_item_img = QPixmap("QtUI/plus.png")
        self.ui.btItemPlus.setIcon(QIcon(plus_item_img))
        self.ui.btItemPlus.setToolTip('Aggiungi Campo per il Hardware')
        self.ui.btItemPlus.setToolTipDuration(10000)
        plus_client_img = QPixmap("QtUI/plus.png")
        self.ui.btClientPlus.setIcon(QIcon(plus_client_img))
        self.ui.btClientPlus.setToolTip('Aggiungi Nuovo Cliente')
        self.ui.btClientPlus.setToolTipDuration(10000)
        plus_foto_img = QPixmap("QtUI/add_photo.png")
        self.ui.btPlus_foto.setIcon(QIcon(plus_foto_img))
        self.ui.btPlus_foto.setToolTip('Aggiungi nuova foto')
        self.ui.btPlus_foto.setToolTipDuration(10000)
        minus_img = QPixmap("QtUI/minus.png")
        self.ui.btMinus.setIcon(QIcon(minus_img))
        self.ui.btMinus.setToolTip('Cancella configurazione')
        self.ui.btMinus.setToolTipDuration(10000)
        minus_hw_img = QPixmap("QtUI/minus.png")
        self.ui.btHwMinus.setIcon(QIcon(minus_hw_img))
        self.ui.btHwMinus.setToolTip('Cancella Hardware selezzionato')
        self.ui.btHwMinus.setToolTipDuration(10000)
        minus_item_img = QPixmap("QtUI/minus.png")
        self.ui.btItemMinus.setIcon(QIcon(minus_item_img))
        self.ui.btItemMinus.setToolTip('Cancella Campo selezzionato')
        self.ui.btItemMinus.setToolTipDuration(10000)
        minus_client_img = QPixmap("QtUI/minus.png")
        self.ui.btClientMinus.setIcon(QIcon(minus_client_img))
        self.ui.btClientMinus.setToolTip('Cancella Cliente con tutti i suoi dati')
        self.ui.btClientMinus.setToolTipDuration(10000)
        minus_foto_img = QPixmap("QtUI/delete_photo.png")
        self.ui.btMinus_foto.setIcon(QIcon(minus_foto_img))
        self.ui.btMinus_foto.setToolTip('Cancella foto della galleria')
        self.ui.btMinus_foto.setToolTipDuration(10000)
        pass_img = QPixmap("QtUI/password.png")
        self.ui.btPassword.setIcon(QIcon(pass_img))
        self.ui.btPassword.setToolTip('Cambio password attuale')
        self.ui.btPassword.setToolTipDuration(10000)
        login_img = QPixmap("QtUI/login.png")
        self.ui.btLogin.setIcon(QIcon(login_img))
        self.ui.btLogin.setToolTip('Login')
        self.ui.btLogin.setToolTipDuration(10000)
        logout_img = QPixmap("QtUI/logout.png")
        self.ui.btLogout.setIcon(QIcon(logout_img))
        self.ui.btLogout.setToolTip('Uscire del programa')
        self.ui.btLogout.setToolTipDuration(10000)
        users_img = QPixmap("QtUI/users.png")
        self.ui.btUsers.setIcon(QIcon(users_img))
        self.ui.btUsers.setToolTip('Lista utenti per l\'accesso al sistema')
        self.ui.btUsers.setToolTipDuration(10000)
        logs = QPixmap("QtUI/log.png")
        self.ui.btLogs.setIcon(QIcon(logs))
        self.ui.btLogs.setToolTip('Logs del sistema')
        self.ui.btLogs.setToolTipDuration(10000)
        pdf = QPixmap("QtUI/pdf.png")
        self.ui.btPDF.setIcon(QIcon(pdf))
        self.ui.btPDF.setToolTip('Salva in formato PDF')
        self.ui.btPDF.setToolTipDuration(10000)
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
        self.ui.labelFoto.mousePressEvent = self.img_normal_size
        self._want_to_close = False
        logo = QPixmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../QtUI', 'ctime_logo.png'))
        self.ui.labelLogo.setPixmap(logo)
        self._ready()

    def _ready(self):
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
                self.ui.btLogin.setDisabled(True)
                if login._login == 'admin':
                    self.ui.btUsers.setHidden(False)
                    self.ui.btPDF.setHidden(False)
                    self.ui.btLogs.setHidden(False)
                else:
                    self.ui.btUsers.setHidden(True)
                    self.ui.btPDF.setHidden(True)
                    self.ui.btLogs.setHidden(True)
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
            hardware = self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 0).text()
            item = self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 1).text()
            value = self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 2).text()
            reply = QMessageBox.question(self, 'Attenzione!', codes.msg(code=201), QMessageBox.Yes, QMessageBox.No)
            if reply == QMessageBox.Yes:
                sql_query.Q(action='deleteRow', kwargs=[hardware, item, value])
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
        for i in reversed(range(self.ui.tableWidget.rowCount())):
            self.ui.tableWidget.removeRow(i)
        tmp_values = sql_query.Q(action='tableView', kwargs=[self.ui.cbClient.currentText()])
        db_table = sorted(tmp_values)
        for row in range(0, len(db_table)):
            self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())
            for colum in range(0, 3):
                value = QTableWidgetItem(str(db_table[row][colum]), 0)
                self.ui.tableWidget.setItem(row, colum, value)
                colum += 1
            row += 1

    def _change_pwd(self):
        changePasswd = ChangePasswd.DialogChangePwd()
        changePasswd.data(str=self.ui.labelUserName.text())
        changePasswd.exec_()
        if int(changePasswd.Accepted) is 1:
            sql_query.Q(action='log', kwargs=[self.ui.labelUserName.text(), codes.msg(code=104)])
            self.statusBar().showMessage(codes.msg(code=104), 2000)

    def quit(self):
        sql_query.Q(action='log', kwargs=[self.ui.labelUserName.text(), codes.msg(code=402)])
        qApp.exit(0)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            sql_query.Q(action='log', kwargs=[self.ui.labelUserName.text(), codes.msg(code=402)])
            qApp.exit(0)

    def _add_foto(self):
        if self.ui.cbClient.currentText() == 'Seleziona':
            self.statusBar().showMessage(codes.msg(code=302), 4000)
        else:
            dlg = QFileDialog()
            dlg.setFileMode(QFileDialog.AnyFile)
            dlg.selectNameFilter(codes.msg(code=101))
            fname = dlg.getOpenFileName(self, 'Seleziona imagine', codes.msg(code=101))
            if str(fname[0])[-3:] == 'png' or str(fname[0])[-3:] == 'bmp' or str(fname[0])[-3:] == 'jpg':
                self.ui.labelFoto.setPixmap(QPixmap(fname[0]))
                self.ui.labelFoto.setScaledContents(True)
                sql_query.Q('save_foto', kwargs=[self.ui.cbClient.currentText(), fname[0]])
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
        img.setPixmap(QPixmap(pix).scaled(380, 370))
        self.ui.labelFoto.setScaledContents(True)
        self.ui.labelFoto.setPixmap(QPixmap(pix))

    def img_normal_size(self, event):
        if self._fs == 1:
            self.ui.labelFoto.setGeometry(633, 147, 380, 411)
            self._fs = 0
        else:
            self.ui.labelFoto.setGeometry(0, 0, 1030, 700)
            self._fs = 1

    def _del_foto(self):
        if self.ui.cbClient.currentText() == 'Seleziona':
            self.statusBar().showMessage(codes.msg(code=302), 4000)
        else:
            if self.ui.tableWidgetImg.currentRow() == -1:
                self.statusBar().showMessage(codes.msg(code=306), 2000)
            else:
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

            data = [[Paragraph(cell, s) for cell in row]
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
