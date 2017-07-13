from PyQt5.Qt import *
from modules.dialogUsers import Ui_DialogUsers
from modules import sql_query
from modules import codes


class DialogUsers(QDialog, Ui_DialogUsers):
    _client = ''

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.EditDialog.hasFocus()
        self.tableWidget.setColumnWidth(0, 250)
        self.tableWidget.setColumnWidth(1, 50)
        plus_users_img = QPixmap("QtUI/plus.png")
        self.btUsersAdd.setIcon(QIcon(plus_users_img))
        self.btUsersAdd.setToolTip('Aggiungi utente alla lista')
        self.btUsersAdd.setToolTipDuration(10000)
        minus_users_img = QPixmap("QtUI/minus.png")
        self.btUsersDel.setIcon(QIcon(minus_users_img))
        self.btUsersDel.setToolTip('Cancella Utente')
        self.btUsersDel.setToolTipDuration(10000)
        save_hw_img = QPixmap("QtUI/save.png")
        self.btSave.setIcon(QIcon(save_hw_img))
        self.btSave.setToolTip('Salva lista')
        self.btSave.setToolTipDuration(10000)
        self.btUsersAdd.clicked.connect(self._new_user)
        self.btUsersDel.clicked.connect(self._delete_user)
        self.btSave.clicked.connect(self._save)
        self.setWindowTitle('Lista Utenti')
        self.tableWidget.itemSelectionChanged.connect(self._modify)
        self.load_table()
        self.btSave.setDisabled(True)
        self.modify = 'False'

    def load_table(self):
        db_table = sql_query.Q(action='load_users')
        for i in reversed(range(self.tableWidget.rowCount())):
            self.tableWidget.removeRow(i)
        for row in range(0, len(db_table)):
            self.tableWidget.insertRow(self.tableWidget.rowCount())
            user = QTableWidgetItem(str(db_table[row][0]), 0)
            self.tableWidget.setItem(row, 0, user)
            if db_table[row][2] == 2:
                pix = QPixmap("QtUI/enable.png")
            else:
                pix = QPixmap("QtUI/disable.png")
            img = QLabel(self)
            img.setPixmap(QPixmap(pix).scaled(16, 16))
            self.tableWidget.setCellWidget(row, 1, img)
            row += 1

    def _new_user(self):
        self.EditDialog.setReadOnly(False)
        self.EditDialogPwd.setReadOnly(False)
        self.EditDialog.setText('')
        self.EditDialogPwd.setText('')
        self.EditDialog.setFocus(True)
        self.btSave.setEnabled(True)
        self.modify = 'False'

    def _save(self):
        try:
            if self.modify == 'False':
                sql_query.Q(action='save_new_user', kwargs=[self.EditDialog.text(), self.EditDialogPwd.text(), self.checkBox.checkState()])
            else:
                sql_query.Q(action='update_user', kwargs=[self.EditDialog.text(), self.checkBox.checkState()])
                self.modify = 'False'
            self.EditDialog.setText('')
            self.EditDialogPwd.setText('')
            self.EditDialog.setReadOnly(True)
            self.EditDialogPwd.setReadOnly(True)
            self.load_table()
            self.btSave.setDisabled(True)
        except:
            QMessageBox.about(self, 'Attenzione', codes.msg(code=307))

    def _delete_user(self):
        sql_query.Q(action='delete_user', kwargs=[self.tableWidget.item(self.tableWidget.currentRow(), 0).text()])
        self.load_table()

    def _modify(self):
        try:
            self.btSave.setEnabled(True)
            self.EditDialog.setText(self.tableWidget.selectedItems()[0].text())
            db_table = sql_query.Q(action='load_user', kwargs=[self.tableWidget.selectedItems()[0].text()])
            self.EditDialogPwd.setText(db_table[0][1])
            self.checkBox.setCheckState(db_table[0][2])
            self.modify = 'True'
        except:
            pass

    def data(self, str=None):
        self._client = str

    def accept(self):
        if self.EditDialog.text() == '':
            QMessageBox.about(self, 'Attenzione', codes.msg(code=308))
        else:
            if self.EditDialog.isReadOnly() is False:
                self._save()
            sql_query.Q(action='new_user', kwargs=[self.EditDialog.text(), self._client])
            self.hide()

    def getValues(self):
        return self.EditDialog.text()

    def close(self):
        self.hide()
