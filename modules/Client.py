from PyQt5.Qt import *
from modules.dialogNewClient import Ui_DialogClient
from modules import sql_query


class DialogNewClient(QDialog, Ui_DialogClient):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.EditDialog.setFocus(True)
        self.setWindowTitle('Insere Cliente')

    def accept(self):
        if self.EditDialog.text() == '':
            QMessageBox.about(self, 'Attenzione', 'Deve scrivere un nome cliente')
        else:
            check_client = sql_query.Q(action='check_client', kwargs=[self.EditDialog.text()])
            if str(check_client) == '()':
                sql_query.Q(action='new_client', kwargs=[self.EditDialog.text()])
                self.hide()
            else:
                QMessageBox.about(self, 'Attenzione', 'Cliente esistente')

    def getValues(self):
        return self.EditDialog.text()

    def close(self):
        self.hide()
