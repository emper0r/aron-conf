import os
import re
from PyQt5.Qt import *
from modules.dialogLic import Ui_DialogLic
from modules import sql_query
from modules import codes
from modules import key


class DialogLic(QDialog, Ui_DialogLic):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self._want_to_close = False
        self.dateEditActive.setDate(QDate.currentDate())
        self.dateEditExpire.setDate(QDate.currentDate().addYears(1))
        save_img = QPixmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../QtUI', 'save.png'))
        trash_img = QPixmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../QtUI', 'trash.png'))
        generate_img = QPixmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../QtUI', 'generate.png'))

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
            for colum in range(0, 10):
                value = QTableWidgetItem(str(db_table[row][colum]), 0)
                self.tableWidget.setItem(row, colum, value)
                colum += 1
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
        email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
        if self.lineEditClient.text() == '' or self.lineEditName.text() == '' or self.lineEditEmail.text() == '' or self.lineEditReq.text() == '' or self.lineEditLic.text() == '' or not email_regex.match(self.lineEditEmail.text()):
            QMessageBox.about(self, 'Attenzione', codes.msg(code=413))
        else:
            sql_query.Q(action='insert_lic', kwargs=[self.lineEditClient.text(), self.lineEditName.text(),
                                                     self.lineEditEmail.text(), self.dateEditActive.text(),
                                                     self.dateEditExpire.text(), self.lineEditReq.text(),
                                                     self.lineEditLic.text(), self.spinBoxQty.value()])
            self._loadtable()
    
    def _delete(self):
        client = self.tableWidget.item(self.tableWidget.currentRow(), 0).text()
        lic = self.tableWidget.item(self.tableWidget.currentRow(), 7).text()
        sql_query.Q(action='delete_lic', kwargs=[client, lic])
        self._loadtable()
    
    def _generate(self):
        pk, sk = key.generate_keypair()
        self.lineEditReq.setText(key.key_to_string(pk))
        self.lineEditLic.setText(key.secret_to_string(sk))

