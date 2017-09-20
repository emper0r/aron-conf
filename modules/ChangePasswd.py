import os
from PyQt5.Qt import *
from modules.dialogChangePwd import Ui_DialogChangePwd
from modules import sql_query
from modules import codes


class DialogChangePwd(QDialog, Ui_DialogChangePwd):
    _client = ''

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.EditNew.hasFocus()
        self.setWindowTitle('Cambio Password')
        logo = QPixmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../images', 'ctime_logo.png'))
        self.labelLogo.setPixmap(logo)
        self.buttonBox.clicked.connect(self.accept)

    def accept(self):
        if self.EditNew.text() == '' or self.EditConferm.text() == '':
            QMessageBox.about(self, 'Attenzione', codes.msg(code=309))
        if self.EditNew.text() == self.EditConferm.text():
            sql_query.Q(action='update_pwd', kwargs=[self.EditNew.text(), self._client])
            self.hide()
        else:
            self.EditNew.clear()
            self.EditConferm.clear()
            QMessageBox.about(self, 'Attenzione', codes.msg(code=310))

    def data(self, str=None):
        self._client = str

    def close(self):
        self.hide()
