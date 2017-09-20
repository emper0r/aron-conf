import os
import base64
import configparser
from PyQt5.Qt import *
from modules.dialogDatabase import Ui_DialogImpostazione

conf = configparser.RawConfigParser()


class DialogDatabase(QDialog, Ui_DialogImpostazione):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.btSave.setFocus()
        save_hw_img = QPixmap("images/save.png")
        self.btSave.setIcon(QIcon(save_hw_img))
        self.btSave.setToolTip('Salva impostazione')
        self.btSave.setToolTipDuration(10000)
        self.btSave.clicked.connect(self._save)
        self.setWindowTitle('Impostazione Database')
        self.load_data()

    def load_data(self):
        conf.read(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../db.conf'))
        try:
            self.EditDialogSmtpServer.setText(base64.b64decode(conf['Mail']['server'][2:-1]).decode('utf-8'))
            self.EditDialogSmtpSender.setText(base64.b64decode(conf['Mail']['sender'][2:-1]).decode('utf-8'))
            self.EditDialogSmtpUser.setText(base64.b64decode(conf['Mail']['user'][2:-1]).decode('utf-8'))
            self.EditDialogSmtpPassword.setText(base64.b64decode(conf['Mail']['password'][2:-1]).decode('utf-8'))
            self.EditDialogHostname.setText(base64.b64decode(conf['Settings']['hostname'][2:-1]).decode('utf-8'))
            self.EditDialogDatabase.setText(base64.b64decode(conf['Settings']['database'][2:-1]).decode('utf-8'))
            self.EditDialogUsername.setText(base64.b64decode(conf['Settings']['user'][2:-1]).decode('utf-8'))
            self.EditDialogPwd.setText(base64.b64decode(conf['Settings']['password'][2:-1]).decode('utf-8'))
            self.spinBoxDaemonPort.value()
        except:
            self.config(smtp_server='localhost', smtp_sender='foo@domain.com', smtp_user='foo', smtp_password='pass',
                        hostname='localhost', database='aron_conf', user='ac', password='!', daemon_port=9999)
            self.load_data()

    def _save(self):
        self.config(smtp_server=self.EditDialogSmtpServer.text(),
                    smtp_sender=self.EditDialogSmtpSender.text(),
                    smtp_user=self.EditDialogSmtpUser.text(),
                    smtp_password=self.EditDialogSmtpPassword.text(),
                    hostname=self.EditDialogHostname.text(),
                    database=self.EditDialogDatabase.text(),
                    user=self.EditDialogUsername.text(),
                    password=self.EditDialogPwd.text(),
                    daemon_port=self.spinBoxDaemonPort.value())
        self.accept()

    def config(self, smtp_server=False, smtp_sender=False, smtp_user=False, smtp_password=False, hostname=False, database=False, user=False, password=False, daemon_port=False):
        config_file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../db.conf'), 'w')
        conf.clear()
        conf.add_section('Settings')
        conf.set('Settings', 'hostname', base64.b64encode(hostname.encode('utf-8')))
        conf.set('Settings', 'database', base64.b64encode(database.encode('utf-8')))
        conf.set('Settings', 'user', base64.b64encode(user.encode('utf-8')))
        conf.set('Settings', 'password', base64.b64encode(password.encode('utf-8')))
        conf.add_section('Mail')
        conf.set('Mail', 'server', base64.b64encode(smtp_server.encode('utf-8')))
        conf.set('Mail', 'sender', base64.b64encode(smtp_sender.encode('utf-8')))
        conf.set('Mail', 'user', base64.b64encode(smtp_user.encode('utf-8')))
        conf.set('Mail', 'password', base64.b64encode(smtp_password.encode('utf-8')))
        conf.add_section('Daemon')
        conf.set('Daemon', 'port', 9999)
        conf.write(config_file)
        config_file.close()

    def accept(self):
        self.hide()

    def close(self):
        self.hide()
