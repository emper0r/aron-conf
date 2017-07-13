from PyQt5.Qt import *
from modules.dialogAddLine import Ui_DialogAdd
from modules import sql_query
from modules import codes
import iptools


class DialogAddLine(QDialog, Ui_DialogAdd):
    _hardware = ''
    _item = ''
    _client = ''

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.EditDialog.hasFocus()
        self.setWindowTitle('Insere Riga')

    def data(self, str_hw=None, str_item=None, str_client=None):
        self._hardware = str_hw
        self._item = str_item
        self._client = str_client
        self.labelDialog.setText(str(self._hardware + ' ' + self._item))

    def accept(self):
        if self.EditDialog.text() == '':
            QMessageBox.about(self, 'Attenzione', codes.msg(code=308))
        else:
            if self._item == 'LAN' or self._item == 'WAN':
                if iptools.ipv4.validate_ip(self.EditDialog.text()) is True:
                    sql_query.Q(action='new_line',
                                kwargs=[self._hardware,
                                        self._item,
                                        self.EditDialog.text(),
                                        self._client])
                    self.hide()
                    return
                else:
                    QMessageBox.about(self, 'Attenzione', codes.msg(code=311))
                    return
            sql_query.Q(action='new_line', kwargs=[self._hardware, self._item, self.EditDialog.text(), self._client])
            self.hide()

    def getValues(self):
        return self.EditDialog.text(), self._client

    def close(self):
        self.hide()
