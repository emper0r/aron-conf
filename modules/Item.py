from PyQt5.Qt import *
from modules.dialogNewItem import Ui_DialogItem
from modules import sql_query
from modules import codes


class DialogNewItem(QDialog, Ui_DialogItem):
    _hardware = ''
    _client = ''

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.EditDialog.hasFocus()
        plus_hw_img = QPixmap("QtUI/plus.png")
        self.btItAdd.setIcon(QIcon(plus_hw_img))
        self.btItAdd.setToolTip('Aggiungi altro campo alla lista di Opzioni')
        self.btItAdd.setToolTipDuration(10000)
        minus_hw_img = QPixmap("QtUI/minus.png")
        self.btItDel.setIcon(QIcon(minus_hw_img))
        self.btItDel.setToolTip('Cancella campo selezzionato della lista di Opzioni')
        self.btItDel.setToolTipDuration(10000)
        save_hw_img = QPixmap("QtUI/save.png")
        self.btItSave.setIcon(QIcon(save_hw_img))
        self.btItSave.setToolTip('Salva campo nella lista Opzioni')
        self.btItSave.setToolTipDuration(10000)
        self.btItAdd.clicked.connect(self._new_it)
        self.btItDel.clicked.connect(self._delete_it)
        self.btItSave.clicked.connect(self._save)
        self.setWindowTitle('Insere Campo')
        self.tableWidget.itemSelectionChanged.connect(self._load_data)
        self.load_table()
        self.btItSave.setDisabled(True)

    def load_table(self):
        db_table = sql_query.Q(action='load_item')
        for i in reversed(range(self.tableWidget.rowCount())):
            self.tableWidget.removeRow(i)
        for row in range(0, len(db_table)):
            self.tableWidget.insertRow(self.tableWidget.rowCount())
            value = QTableWidgetItem(str(db_table[row][0]), 0)
            self.tableWidget.setItem(row, 0, value)
            row += 1

    def _new_it(self):
        self.EditDialog.setReadOnly(False)
        self.EditDialog.setText('')
        self.EditDialog.setFocus(True)
        self.btItSave.setEnabled(True)
        self.buttonBox.setDisabled(True)

    def _save(self):
        try:
            sql_query.Q(action='save_it_new', kwargs=[self.EditDialog.text()])
            self.EditDialog.setReadOnly(True)
            self.btItSave.setDisabled(True)
            self.EditDialog.setText('')
            self.buttonBox.setDisabled(False)
            self.load_table()
        except:
            QMessageBox.about(self, 'Attenzione', codes.msg(code=307))

    def _delete_it(self):
        sql_query.Q(action='delete_it_item', kwargs=[self.tableWidget.item(self.tableWidget.currentRow(), 0).text()])
        self.EditDialog.setText('')
        self.load_table()

    def _load_data(self):
        try:
            self.EditDialog.setText(self.tableWidget.selectedItems()[0].text())
        except:
            pass

    def data(self, str_hw=None, str_client=None):
        self._hardware = str_hw
        self._client = str_client

    def accept(self):
        if self.EditDialog.text() == '':
            QMessageBox.about(self, 'Attenzione', codes.msg(code=308))
        else:
            if self.EditDialog.isReadOnly() is False:
                self._save()
            sql_query.Q(action='new_Item', kwargs=[self.EditDialog.text(), self._hardware, self._client])
            self.hide()

    def getValues(self):
        return self.EditDialog.text()

    def close(self):
        self.hide()
