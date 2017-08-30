import os
from PyQt5.Qt import *
from modules.dialogLic import Ui_DialogLic
from modules import sql_query


class DialogLic(QDialog, Ui_DialogLic):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
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
        self.hide()
