__author__ = 'dead'

#!/usr/bin/env python
import sys,sqlite3
from PyQt4 import QtCore, QtGui, uic
from windowMain import startMainWindow

# """заполнение списка пользователей, пароль хранится в роле"""
# def AddListUser():
#         for n in range(0,arr.__len__()):
#             edtInputUser = window.edtInputUser.addItem(arr[n][1], arr[n][2])
#
def initBD():
    con = sqlite3.connect("lombard1.db")

    cur = con.cursor()
    cur.execute("SELECT * FROM user")
    arr = cur.fetchall()

    for n in range(0,arr.__len__()):
        edtInputUser = window.edtInputUser.addItem(arr[n][1], arr[n][2])

    cur.close()
    con.close()

"""проверка пароля """
def InputUser():
    curIndex = window.edtInputUser.currentIndex()
    currentPassw = window.edtInputUser.itemData(curIndex)
    #MainWindow()
    if currentPassw == window.InputPassw.text():

        #window
        # print("/INPUT")
        QtGui.QWidget.close(window)
        startMainWindow(MainWindow)
        #QtGui.QWidget.show(MainWindow)
        #QtGui.qApp.quit

        #QtGui.QWidget.close

    else:
        QtGui.QMessageBox.critical(window, "Ошибка", "Проверьте правильность ввода Пароля", QtGui.QMessageBox.Close)
        window.InputPassw.setText("")

def showWndSprKlients():
   wndSprKlients.setParent(MainWindow)
   #MainWindow.setParent(wndSprKlients)
   QtGui.QWidget.show(wndSprKlients)

   #wndSprKlients.setWindowState(QtCore.Qt.WindowMaximized)

def initialWindows():

    #Входное окно, где пароль
    QtCore.QObject.connect(window.btnQuit, QtCore.SIGNAL("clicked()"), QtGui.qApp.quit) # нажатие кнопки ОТМЕНА
    QtCore.QObject.connect(window.btnOK, QtCore.SIGNAL("clicked()"), InputUser) #Нажата Кннопка ВХОД

    window.setWindowFlags(QtCore.Qt.Window |
                       QtCore.Qt.CustomizeWindowHint |
                       QtCore.Qt.WindowTitleHint |
                       QtCore.Qt.WindowCloseButtonHint |
                       QtCore.Qt.MSWindowsFixedSizeDialogHint)

    #окно СПРАВОЧНИК КЛИНТЫ
    #QtGui.QWidget.parent()

    QtCore.QObject.connect(MainWindow.sprKlients, QtCore.SIGNAL("triggered()"), showWndSprKlients)


class startApp():
    global window,MainWindow,wndSprKlients

    app = QtGui.QApplication(sys.argv)

    window = uic.loadUi("MyForm.ui")
    MainWindow = uic.loadUi("MainWindow.ui")
    wndSprKlients = uic.loadUi("WindowSprKlients.ui")

    initialWindows()
    initBD()

    window.show()
    app.exec()  # запускает приложение

    #sys.exit(app.exec_())

