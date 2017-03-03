from PyQt5.Qt import *
from modules.dialogLogs import Ui_DialogLogs
from modules import sql_query


class DialogLogs(QDialog, Ui_DialogLogs):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.comboBox.setFocus()
        self._want_to_close = False
        users_list = sql_query.Q(action='load_users')
        self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 360)
        self.comboBox.clear()
        logs = QPixmap("QtUI/log.png")
        self.btFind.setIcon(QIcon(logs))
        self.btFind.setToolTip('Logs del sistema')
        self.btFind.setToolTipDuration(10000)
        self.comboBox.addItem('Tutti')
        for item in range(0, len(users_list)):
            self.comboBox.addItem(users_list[item][0])
        self.logs()
        self.btFind.clicked.connect(self.logs)

    def logs(self):
        if self.comboBox.currentText() == 'Tutti':
            db_table = sql_query.Q(action='allLogs',
                                   kwargs=[str(self.calendarFrom.selectedDate().year()) + '-' +
                                           str(self.calendarFrom.selectedDate().month()) + '-' +
                                           str(self.calendarFrom.selectedDate().day()) + ' 00:00:00',
                                           str(self.calendarTo.selectedDate().year()) + '-' +
                                           str(self.calendarTo.selectedDate().month()) + '-' +
                                           str(self.calendarTo.selectedDate().day()) + ' 23:59:59'])
        else:
            db_table = sql_query.Q(action='logs_by',
                                   kwargs=[str(self.calendarFrom.selectedDate().year()) + '-' +
                                           str(self.calendarFrom.selectedDate().month()) + '-' +
                                           str(self.calendarFrom.selectedDate().day()) + ' 00:00:00',
                                           str(self.calendarTo.selectedDate().year()) + '-' +
                                           str(self.calendarTo.selectedDate().month()) + '-' +
                                           str(self.calendarTo.selectedDate().day()) + ' 23:59:59',
                                           str(self.comboBox.currentText())])
        for i in reversed(range(self.tableWidget.rowCount())):
            self.tableWidget.removeRow(i)
        for row in range(0, len(db_table)):
            self.tableWidget.insertRow(self.tableWidget.rowCount())
            for colum in range(0, 3):
                value = QTableWidgetItem(str(db_table[row][colum]), 0)
                self.tableWidget.setItem(row, colum, value)
                colum += 1
            row += 1

    def closeEvent(self, event):
        if self._want_to_close:
            super(DialogLogs, self).closeEvent()
        else:
            self.hide()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter:
            self.accept()
        if event.key() == Qt.Key_Escape:
            self.hide()
