from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from Form_ui import Ui_MainWindow  # импорт сгенерированного файла UI
import sys
import re
import subprocess
import win32clipboard
import datetime

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        address=''
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        now = QDateTime.currentDateTime()
        self.ui.dateTimeEdit.setDateTime(now)
        self.ui.dateTimeEdit_2.setDateTime(now)
        f = open('address.txt', 'r')
        line = f.readline()
        while line:
            address += line
            address +='\n'
            line = f.readline()                 # чтение следующей строки
        f.close()
        self.ui.textEdit_5.setText(address)
        self.ui.radioButton.clicked.connect(self.datetime2Off)
        self.ui.radioButton_2.clicked.connect(self.datetime2Off)
        self.ui.radioButton_7.clicked.connect(self.datetime2Off)
        self.ui.radioButton_6.clicked.connect(self.datetime2On)
        self.ui.radioButton_8.clicked.connect(self.datetime2On)
        self.ui.pushButton.clicked.connect(self.btnClicked)
        self.ui.pushButton_2.clicked.connect(self.btnClicked_2)
        self.ui.pushButton_3.clicked.connect(self.btnClicked_3)
        self.ui.pushButton_4.clicked.connect(self.btnClicked_4)
        self.ui.pushButton_5.clicked.connect(self.btnClicked_5)
    def btnClicked(self):
        main_result = ''
        fault_tematic = ''
        if self.ui.lineEdit.text():
            main_result += 'СИ:'
            main_result += self.ui.lineEdit.text()
            main_result += '\n'
        if self.ui.lineEdit_2.text():
            main_result += 'ГП:'
            main_result += self.ui.lineEdit_2.text()
            main_result += '\n'
        if self.ui.lineEdit_3.text():
            main_result += 'ТТ:'
            main_result += self.ui.lineEdit_3.text()
            main_result += '\n'
        if self.ui.radioButton_3.isChecked():
            main_result += 'ФЛ\n'
        if self.ui.radioButton_4.isChecked():
            main_result += 'ЮЛ\n'
        if self.ui.radioButton_5.isChecked():
            main_result += 'ФЛ + ЮЛ\n'
        if self.ui.radioButton_6.isChecked() or self.ui.radioButton_8.isChecked():
            ddMMyyyy_1 = self.ui.dateTimeEdit.dateTime().toString("dd.MM.yyyy")
            ddMMyyyy_2 = self.ui.dateTimeEdit_2.dateTime().toString("dd.MM.yyyy")
            if ddMMyyyy_1 == ddMMyyyy_2:
                main_result += self.ui.dateTimeEdit.dateTime().toString("dd.MM.yyyyг hh:mm")
                main_result += ' - '
                main_result += self.ui.dateTimeEdit_2.dateTime().toString("hh:mmмск ")
            else:
                main_result += self.ui.dateTimeEdit.dateTime().toString("dd.MM.yyyyг hh:mmмск")
                main_result += ' - '
                main_result += self.ui.dateTimeEdit_2.dateTime().toString("dd.MM.yyyyг hh:mmмск ")
        else:
           main_result += self.ui.dateTimeEdit.dateTime().toString("dd.MM.yyyyг hh:mmмск ") 
        if self.ui.textEdit.toPlainText():
            main_result += self.ui.textEdit.toPlainText()
        if self.ui.checkBox_3.isChecked():
            main_result += " Проблемы с авторизацией"
            f = open('fault_bras_servises.txt', 'r')
            line = f.readline()
            while line:
                fault_tematic += line
                fault_tematic +='\n'
                line = f.readline()                 # чтение следующей строки
            f.close()
        if self.ui.checkBox_4.isChecked() or self.ui.checkBox_5.isChecked() or self.ui.checkBox_6.isChecked():
            main_result += " 100% отсутствие"
            if self.ui.checkBox_4.isChecked():
                main_result += " мг/мн"
                f = open('fault_unavail_tel.txt', 'r')
                line = f.readline()
                while line:
                    fault_tematic += line
                    fault_tematic +='\n'
                    line = f.readline()                 # чтение следующей строки
                f.close()
            if self.ui.checkBox_5.isChecked():
                main_result += " СПД"
                f = open('fault_unavail_spd.txt', 'r')
                line = f.readline()
                while line:
                    fault_tematic += line
                    fault_tematic +='\n'
                    line = f.readline()                 # чтение следующей строки
                f.close()                
            if self.ui.checkBox_6.isChecked():
                main_result += " IpTV"
                f = open('fault_unavail_iptv.txt', 'r')
                line = f.readline()
                while line:
                    fault_tematic += line
                    fault_tematic +='\n'
                    line = f.readline()                 # чтение следующей строки
                f.close()
        if self.ui.checkBox_7.isChecked() or self.ui.checkBox_8.isChecked() or self.ui.checkBox_9.isChecked():
            main_result += " Ухудшение качества"
            if self.ui.checkBox_7.isChecked():
                main_result += " МГ/МН"
                f = open('fault_degrad_tel.txt', 'r')
                line = f.readline()
                while line:
                    fault_tematic += line
                    fault_tematic +='\n'
                    line = f.readline()                 # чтение следующей строки
                f.close()
            if self.ui.checkBox_8.isChecked():
                main_result += " СПД"
                f = open('fault_degrad_spd.txt', 'r')
                line = f.readline()
                while line:
                    fault_tematic += line
                    fault_tematic +='\n'
                    line = f.readline()                 # чтение следующей строки
                f.close()
            if self.ui.checkBox_9.isChecked():
                main_result += " IpTV"
                f = open('fault_degrad_iptv.txt', 'r')
                line = f.readline()
                while line:
                    fault_tematic += line
                    fault_tematic +='\n'
                    line = f.readline()                 # чтение следующей строки
                f.close()
        if self.ui.textEdit_2.toPlainText() or self.ui.radioButton.isChecked() or self.ui.radioButton_2.isChecked() or self.ui.radioButton_6.isChecked() or self.ui.radioButton_7.isChecked() or self.ui.radioButton_8.isChecked():
            main_result += ' Причина: '
            if self.ui.radioButton.isChecked():
                main_result += 'Сбой в работе оборудования ПАО Ростелеком'
            if self.ui.radioButton_2.isChecked():
                main_result += 'Линейное повреждение'
            if self.ui.radioButton_6.isChecked():
                main_result += 'Ремонтно-настроечные работы на сети филиала'
            if self.ui.radioButton_7.isChecked():
                main_result += 'Аварийное отключение Э/Э'
            if self.ui.radioButton_8.isChecked():
                main_result += 'Плановое отключение Э/Э'
            if self.ui.textEdit_2.toPlainText():
                main_result += ' '
                main_result += self.ui.textEdit_2.toPlainText()
#        print('--' + main_result)
#        print('t-' + fault_tematic)
        self.ui.textEdit_3.setText(main_result)
        self.ui.textEdit_4.setText(fault_tematic)      
    def btnClicked_2(self):
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(self.ui.textEdit_3.toPlainText())
        win32clipboard.CloseClipboard()
    def btnClicked_3(self):
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(self.ui.textEdit_5.toPlainText())
        win32clipboard.CloseClipboard()
    def btnClicked_4(self):
        text = ''
        text = self.ui.textEdit_3.toPlainText()
        text = text.replace("\n", " ")
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(text)
        win32clipboard.CloseClipboard()
    def btnClicked_5(self):
        self.ui.textEdit.setText("")
        self.ui.textEdit_2.setText("")
        self.ui.textEdit_3.setText("")
        self.ui.textEdit_4.setText("")
        self.ui.lineEdit.setText("")
        self.ui.lineEdit_2.setText("")
        self.ui.lineEdit_3.setText("")
        now = QDateTime.currentDateTime()
        self.ui.dateTimeEdit.setDateTime(now)
        self.ui.dateTimeEdit_2.setDateTime(now)
        self.ui.checkBox_3.setChecked(False)
        self.ui.checkBox_4.setChecked(False)
        self.ui.checkBox_5.setChecked(False)
        self.ui.checkBox_6.setChecked(False)
        self.ui.checkBox_7.setChecked(False)
        self.ui.checkBox_8.setChecked(False)
        self.ui.checkBox_9.setChecked(False)
        # Отключение эксклюзива радиокнопок
        self.ui.radioButton.setAutoExclusive(False)
        self.ui.radioButton_2.setAutoExclusive(False)
        self.ui.radioButton_3.setAutoExclusive(False)
        self.ui.radioButton_4.setAutoExclusive(False)
        self.ui.radioButton_5.setAutoExclusive(False)
        self.ui.radioButton_6.setAutoExclusive(False)
        self.ui.radioButton_7.setAutoExclusive(False)
        self.ui.radioButton_8.setAutoExclusive(False)
        # убираем выделение радиоточек
        self.ui.radioButton.setChecked(False)
        self.ui.radioButton_2.setChecked(False)
        self.ui.radioButton_3.setChecked(False)
        self.ui.radioButton_4.setChecked(False)
        self.ui.radioButton_5.setChecked(False)
        self.ui.radioButton_6.setChecked(False)
        self.ui.radioButton_7.setChecked(False)
        self.ui.radioButton_8.setChecked(False)
        # Включение эксклюзива радиокнопок
        self.ui.radioButton.setAutoExclusive(True)
        self.ui.radioButton_2.setAutoExclusive(True)
        self.ui.radioButton_3.setAutoExclusive(True)
        self.ui.radioButton_4.setAutoExclusive(True)
        self.ui.radioButton_5.setAutoExclusive(True)
        self.ui.radioButton_6.setAutoExclusive(True)
        self.ui.radioButton_7.setAutoExclusive(True)
        self.ui.radioButton_8.setAutoExclusive(True)
        self.ui.dateTimeEdit_2.setEnabled(False)
    def datetime2On(self):
        self.ui.dateTimeEdit_2.setEnabled(True)
    def datetime2Off(self):
        self.ui.dateTimeEdit_2.setEnabled(False)
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
 
sys.exit(app.exec())
