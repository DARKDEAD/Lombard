__author__ = 'dead'
import sys,sqlite3
from PyQt4 import QtCore, QtGui, uic

"""заполнение списка пользователей, пароль хранится в роле"""
def AddListUser():
        for n in range(0,arr.__len__()):
            edtInputUser = window.edtInputUser.addItem(arr[n][1], arr[n][2])

def initBD():
    con = sqlite3.connect("lombard1.db")

    cur = con.cursor()
    cur.execute("SELECT * FROM user")
    arr = cur.fetchall()

    AddListUser()
    cur.close()
    con.close()

class start(object):
    initBD()

    app = QtGui.QApplication(sys.argv)
    window = uic.loadUi("MyForm.ui")
    window.show()