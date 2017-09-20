from PyQt5.Qt import *
from modules.dialogNewHardware import Ui_DialogHw
from modules import sql_query
from modules import codes


class DialogNewHardware(QDialog, Ui_DialogHw):
    _client = ''

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.EditDialog.hasFocus()
        plus_hw_img = QPixmap("images/plus.png")
        self.btHwAdd.setIcon(QIcon(plus_hw_img))
        self.btHwAdd.setToolTip('Aggiungi altro hardware alla lista di Opzioni')
        self.btHwAdd.setToolTipDuration(10000)
        minus_hw_img = QPixmap("images/minus.png")
        self.btHwDel.setIcon(QIcon(minus_hw_img))
        self.btHwDel.setToolTip('Cancella Hardware selezzionato della lista di Opzioni')
        self.btHwDel.setToolTipDuration(10000)
        save_hw_img = QPixmap("images/save.png")
        self.btSave.setIcon(QIcon(save_hw_img))
        self.btSave.setToolTip('Salva campo nella lista Opzioni')
        self.btSave.setToolTipDuration(10000)
        self.btHwAdd.clicked.connect(self._new_hw)
        self.btHwDel.clicked.connect(self._delete_hw)
        self.btSave.clicked.connect(self._save)
        self.setWindowTitle('Insere Hardware')
        self.tableWidget.itemSelectionChanged.connect(self._load_data)
        self.load_table()
        self.btSave.setDisabled(True)

    def load_table(self):
        db_table = sql_query.Q(action='load_hw')
        for i in reversed(range(self.tableWidget.rowCount())):
            self.tableWidget.removeRow(i)
        for row in range(0, len(db_table)):
            self.tableWidget.insertRow(self.tableWidget.rowCount())
            value = QTableWidgetItem(str(db_table[row][0]), 0)
            self.tableWidget.setItem(row, 0, value)
            row += 1

    def _new_hw(self):
        self.EditDialog.setReadOnly(False)
        self.EditDialog.setText('')
        self.EditDialog.setFocus(True)
        self.btSave.setEnabled(True)
        self.buttonBox.setDisabled(True)

    def _save(self):
        try:
            sql_query.Q(action='save_hw_new', kwargs=[self.EditDialog.text()])
            self.EditDialog.setReadOnly(True)
            self.btSave.setDisabled(True)
            self.EditDialog.setText('')
            self.buttonBox.setDisabled(False)
            self.load_table()
        except:
            QMessageBox.about(self, 'Attenzione', codes.msg(code=307))

    def _delete_hw(self):
        sql_query.Q(action='delete_hw_item', kwargs=[self.tableWidget.item(self.tableWidget.currentRow(), 0).text()])
        self.EditDialog.setText('')
        self.load_table()

    def _load_data(self):
        try:
            self.EditDialog.setText(self.tableWidget.selectedItems()[0].text())
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
            sql_query.Q(action='new_hw', kwargs=[self.EditDialog.text(), self._client])
            self.hide()

    def getValues(self):
        return self.EditDialog.text()

    def close(self):
        self.hide()
