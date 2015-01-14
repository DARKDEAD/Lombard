# -*- coding:utf-8 -*-

# noinspection PyUnresolvedReferences,PyUnresolvedReferences
from PyQt4 import QtCore, QtGui, uic
from Tools.Scripts.serve import app
import sys, sqlite3


"""проверка пароля """
def InputUser():
    curIndex = window.edtInputUser.currentIndex()
    currentPassw = window.edtInputUser.itemData(curIndex)

    if currentPassw == window.InputPassw.text():
        print("/INPUT")
        QtGui.qApp.quit
    else:
        QtGui.QMessageBox.critical(window, "Ошибка", "Проверьте правильность ввода Пароля", QtGui.QMessageBox.Close)
        window.InputPassw.setText("")

"""заполнение списка пользователей, пароль хранится в роле"""
def AddListUser():
    for n in range(0,arr.__len__()):
        edtInputUser = window.edtInputUser.addItem(arr[n][1], arr[n][2])

# noinspection PyRedeclaration
app = QtGui.QApplication(sys.argv)
window = uic.loadUi("MyForm.ui")

con = sqlite3.connect("lombard1.db")
cur = con.cursor()
cur.execute("SELECT * FROM user")
arr = cur.fetchall()

AddListUser()
cur.close()
con.close()


QtCore.QObject.connect(window.btnQuit, QtCore.SIGNAL("clicked()"), QtGui.qApp.quit)
QtCore.QObject.connect(window.btnOK, QtCore.SIGNAL("clicked()"), InputUser)

window.setWindowFlags(QtCore.Qt.Window |
                       QtCore.Qt.CustomizeWindowHint |
                       QtCore.Qt.WindowTitleHint |
                       QtCore.Qt.WindowCloseButtonHint |
                       QtCore.Qt.MSWindowsFixedSizeDialogHint)

window.show()
# noinspection PyUnresolvedReferences
sys.exit(app.exec_())