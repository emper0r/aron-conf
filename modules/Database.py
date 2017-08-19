import os
import configparser
from PyQt5.Qt import *
from modules.dialogDatabase import Ui_DialogDatabase

conf = configparser.RawConfigParser()


class DialogDatabase(QDialog, Ui_DialogDatabase):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.btSave.setFocus()
        save_hw_img = QPixmap("QtUI/save.png")
        self.btSave.setIcon(QIcon(save_hw_img))
        self.btSave.setToolTip('Salva impostazione')
        self.btSave.setToolTipDuration(10000)
        self.btSave.clicked.connect(self._save)
        self.setWindowTitle('Impostazione Database')
        self.load_data()

    def load_data(self):
        conf.read(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../db.conf'))
        try:
            self.EditDialogHostname.setText(conf['Settings']['hostname'])
            self.EditDialogDatabase.setText(conf['Settings']['database'])
            self.EditDialogUsername.setText(conf['Settings']['user'])
            self.EditDialogPwd.setText(conf['Settings']['password'])
        except:
            self.config(hostname='localhost', database='aron_conf', user='ac', password='!')
            self.load_data()

    def _save(self):
        self.config(hostname=self.EditDialogHostname.text(),
                    database=self.EditDialogDatabase.text(),
                    user=self.EditDialogUsername.text(),
                    password=self.EditDialogPwd.text())
        self.accept()

    def config(self, hostname=False, database=False, user=False, password=False):
        config_file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../db.conf'), 'w')
        conf.clear()
        conf.add_section('Settings')
        conf.set('Settings', 'hostname', hostname)
        conf.set('Settings', 'database', database)
        conf.set('Settings', 'user', user)
        conf.set('Settings', 'password', password)
        conf.write(config_file)
        config_file.close()

    def accept(self):
        self.hide()

    def close(self):
        self.hide()
