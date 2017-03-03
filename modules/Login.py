import os
import bcrypt
from PyQt5.Qt import *
from modules.dialogLogin import Ui_DialogLogin
from modules import sql_query
from modules import codes


class DialogLogin(QDialog, Ui_DialogLogin):
    _access = False
    _login = ''

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.EditLogin.setFocus()
        self._want_to_close = False
        logo = QPixmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../QtUI', 'ctime_logo.png'))
        self.labelLogo.setPixmap(logo)

    def accept(self):
        if self.EditLogin.text() == '' or self.EditPass.text() == '':
            QMessageBox.about(self, 'Attenzione', codes.msg(code=114))
        else:
            try:
                access = sql_query.Q(action='login', kwargs=[self.EditLogin.text()])
                if len(access) is 0:
                    self.EditLogin.clear()
                    self.EditPass.clear()
                    self.EditLogin.setFocus()
                elif bcrypt.hashpw(str(self.EditPass.text()).encode('utf-8'), str(access[0][1]).encode('utf-8')) == str(access[0][2]).encode('utf-8'):
                    self._login = self.EditLogin.text()
                    sql_query.Q(action='log', kwargs=[self.EditLogin.text(), codes.msg(code=115)])
                    self._access = self.hide()
                else:
                    self.EditLogin.clear()
                    self.EditPass.clear()
                    self.EditLogin.setFocus()
                    sql_query.Q(action='log', kwargs=[self.EditLogin.text(), codes.msg(code=404 + self.EditLogin.text())])
            except:
                QMessageBox.about(self, 'Attenzione', codes.msg(code=401))

    def getValues(self):
        return self._access

    def closeEvent(self, event):
        if self._want_to_close:
            super(DialogLogin, self).closeEvent()
        else:
            event.ignore()
            sql_query.Q(action='log', kwargs=[self.EditLogin.text(), codes.msg(code=404) + self.EditLogin.text()])
            qApp.exit(0)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter:
            self.accept()
        if event.key() == Qt.Key_Escape:
            sql_query.Q(action='log', kwargs=[self.EditLogin.text(), codes.msg(code=404) + self.EditLogin.text()])
            qApp.exit(0)