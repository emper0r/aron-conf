import os
import re
import smtplib
import base64
import configparser
import socket
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt5.Qt import *
from modules.dialogLic import Ui_DialogLic
from modules import sql_query
from modules import codes


class DialogLic(QDialog, Ui_DialogLic):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self._want_to_close = False
        self.dateEditActive.setDate(QDate.currentDate())
        self.dateEditExpire.setDate(QDate.currentDate().addYears(1))
        save_img = QPixmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../images', 'save.png'))
        trash_img = QPixmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../images', 'trash.png'))
        generate_img = QPixmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../images', 'generate.png'))

        self.tableWidget.setColumnWidth(0, 90)
        self.tableWidget.setColumnWidth(1, 90)
        self.tableWidget.setColumnWidth(2, 120)
        self.tableWidget.setColumnWidth(3, 70)
        self.tableWidget.setColumnWidth(4, 80)
        self.tableWidget.setColumnWidth(5, 80)
        self.tableWidget.setColumnWidth(6, 240)
        self.tableWidget.setColumnWidth(7, 240)
        self.tableWidget.setColumnWidth(8, 240)
        self.tableWidget.setColumnWidth(9, 60)
        self.tableWidget.setColumnWidth(10, 240)
        self.btSave.setIcon(QIcon(save_img))
        self.btSave.setToolTip('Salve Licenza')
        self.btSave.setToolTipDuration(10000)
        self.btGenerate.setIcon(QIcon(generate_img))
        self.btGenerate.setToolTip('Genera Licenza')
        self.btGenerate.setToolTipDuration(10000)
        self.btDelete.setIcon(QIcon(trash_img))
        self.btDelete.setToolTip('Cancella Licenza')
        self.btDelete.setToolTipDuration(10000)

        self.btSave.clicked.connect(self._save)
        self.btGenerate.clicked.connect(self._generate)
        self.btDelete.clicked.connect(self._delete)
        
        self._loadtable()
        
    def _loadtable(self):
        for i in reversed(range(self.tableWidget.rowCount())):
            self.tableWidget.removeRow(i)
        db_table = sql_query.Q(action='license')
        for row in range(0, len(db_table)):
            self.tableWidget.insertRow(self.tableWidget.rowCount())
            for column in range(0, 11):
                if column == 9 and db_table[row][9] == 1:
                    pix = QPixmap("images/enable.png")
                    img = QLabel(self)
                    img.setPixmap(QPixmap(pix).scaled(16, 16))
                    self.tableWidget.setCellWidget(row, 9, img)
                elif column == 9 and db_table[row][9] is None:
                    pix = QPixmap("images/disable.png")
                    img = QLabel(self)
                    img.setPixmap(QPixmap(pix).scaled(16, 16))
                    self.tableWidget.setCellWidget(row, 9, img)
                else:
                    if column == 3 and db_table[row][3] is 0:
                        value = QTableWidgetItem(str('Ilimitati'), 0)
                    else:
                        value = QTableWidgetItem(str(db_table[row][column]), 0)
                    value.setTextAlignment(Qt.AlignHCenter)
                    value.setTextAlignment(Qt.AlignVCenter)
                    self.tableWidget.setItem(row, column, value)
                    column += 1
            row += 1

    def closeEvent(self, event):
        if self._want_to_close:
            super(DialogLic, self).closeEvent()
        else:
            self.hide()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter:
            self.accept()
        if event.key() == Qt.Key_Escape:
            self.hide()
    
    def _save(self):
        conf = configparser.RawConfigParser()
        conf.read(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../db.conf'))
        email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
        if self.lineEditClient.text() == '' or self.lineEditName.text() == '' or self.lineEditEmail.text() == '' or self.lineEditReq.text() == '' or self.lineEditLic.text() == '' or not email_regex.match(self.lineEditEmail.text()):
            QMessageBox.about(self, 'Attenzione', codes.msg(code=413))
        else:
            sql_query.Q(action='insert_lic', kwargs=[self.lineEditClient.text(), self.lineEditName.text(),
                                                     self.lineEditEmail.text(), self.dateEditActive.text(),
                                                     self.dateEditExpire.text(), self.lineEditReq.text(),
                                                     self.lineEditLic.text(), self.spinBoxQty.value()])

            if self.spinBoxQty.value() is 0:
                qty = 'Ilimitati'
            else:
                qty = str(self.spinBoxQty.value())
            
            sender = base64.b64decode(conf['Mail']['sender'][2:-1]).decode('utf-8')
            recipient = self.lineEditEmail.text()
            
            ctx = 'Gentile Cliente,<br><br>Grazie per aver scelto il nostro prodotto Aron Proxy,<br>'
            ctx += 'nel seguito inviamo i dati per l\'attivazione della licenza.<br><br>'
            ctx += 'Cliente: %s<br>Nome: %s<br>Codice: %s<br>Licenza: %s<br>Quantita\' devices: %s<br><br>' \
                   'Cordiali Saluti,<br><br>' \
                   'Computer Time s.r.l' % \
                   (self.lineEditClient.text(), self.lineEditName.text(), self.lineEditReq.text(), self.lineEditLic.text(), qty)

            msg = MIMEMultipart('alternative')
            msg['Subject'] = u'Computer Time :: Licenza per Aron Proxy'
            msg['From'] = sender
            msg['To'] = recipient
            message = MIMEText(ctx, 'html')
            msg.attach(message)
            s = smtplib.SMTP(base64.b64decode(conf['Mail']['server'][2:-1]).decode('utf-8'), 25)
            s.login(base64.b64decode(conf['Mail']['user'][2:-1]).decode('utf-8'),
                    base64.b64decode(conf['Mail']['password'][2:-1]).decode('utf-8'))
            s.sendmail(sender, recipient, msg.as_string())
            s.quit()

            self._loadtable()
    
    def _delete(self):
        client = self.tableWidget.item(self.tableWidget.currentRow(), 0).text()
        lic = self.tableWidget.item(self.tableWidget.currentRow(), 7).text()
        sql_query.Q(action='delete_lic', kwargs=[client, lic])
        self._loadtable()
    
    def _generate(self):
        conf = configparser.RawConfigParser()
        conf.read(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../db.conf'))
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((base64.b64decode(conf['Settings']['hostname'][2:-1]).decode('utf-8'),
                          int(conf['Daemon']['port'])))
            sock.sendall(bytes('genlic' + "\n", "utf-8"))
            received = str(sock.recv(1024), "utf-8")
            self.lineEditReq.setText(received[:48])
            self.lineEditLic.setText(received[49:])
