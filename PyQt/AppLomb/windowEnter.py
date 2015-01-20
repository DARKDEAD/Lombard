__author__ = 'dead'

#!/usr/bin/env python
import sys,sqlite3
from PyQt4 import QtCore, QtGui, uic
from windowMain import startMainWindow

class MainWnd(QtGui.QMainWindow):
    def __init__(self, prent=None):
        QtGui.QMainWindow.__init__(self, parent=None)
        uic.loadUi("MainWindow.ui",self)
        self.connect(self.sprKlients, QtCore.SIGNAL("triggered()"), self.showWnd)
    def showWnd(self):
        window = showWndSprKlients()
        window.show()

"""проверка пароля """
def InputUser_():
    curIndex = window.edtInputUser.currentIndex()
    currentPassw = window.edtInputUser.itemData(curIndex)
    #MainWindow()
    if currentPassw == window.InputPassw.text():

        #window
        # print("/INPUT")
        QtGui.QWidget.close(window)
        window = MainWnd()
        window.show()

        #startMainWindow(MainWindow)
        #QtGui.QWidget.show(MainWindow)
        #QtGui.qApp.quit

        #QtGui.QWidget.close

    else:
        QtGui.QMessageBox.critical(window, "Ошибка", "Проверьте правильность ввода Пароля", QtGui.QMessageBox.Close)
        window.InputPassw.setText("")

class showWndSprKlients(QtGui.QMainWindow):
    def __init__(self, prent=None):
        QtGui.QWidget.__init__(self, parent=None)
        uic.loadUi("WindowSprKlients.ui",self)


   #wndSprKlients.setParent(MainWindow)
   #MainWindow.setParent(wndSprKlients)
    # def __init__(self, paren=None):
    #    self.wndSprKlients = uic.loadUi("WindowSprKlients.ui")
    #    # wndSprKlients.setParent(MainWindow)
    #    # wndSprKlients.setWindowFlags(QtCore.Qt.Window)
    # def showWnd(self):
    #     #QtGui.QWidget.show(wndSprKlients)
    #     self.show()
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
    showWndSprKlients()
    QtCore.QObject.connect(MainWindow.sprKlients, QtCore.SIGNAL("triggered()"), showWndSprKlients.showWnd())

class MyWindow(QtGui.QWidget):
    def __init__(self, prent=None):
        QtGui.QWidget.__init__(self, parent=None)
        uic.loadUi("MyForm.ui",self)
        self.connect(self.btnQuit, QtCore.SIGNAL("clicked()"), self.close) # нажатие кнопки ОТМЕНА
        self.connect(self.btnOK, QtCore.SIGNAL("clicked()"), self.InputUser) #Нажата Кннопка ВХОД

        self.setWindowFlags(QtCore.Qt.Window |
                       QtCore.Qt.CustomizeWindowHint |
                       QtCore.Qt.WindowTitleHint |
                       QtCore.Qt.WindowCloseButtonHint |
                       QtCore.Qt.MSWindowsFixedSizeDialogHint)

        MyWindow.initBD(self)

#проверка пароля """
    def InputUser(self):
        curIndex = self.edtInputUser.currentIndex()
        currentPassw = self.edtInputUser.itemData(curIndex)

        if currentPassw == self.InputPassw.text():

            window = MainWnd()
            window.show()

            self.hide()
        else:
            QtGui.QMessageBox.critical(self, "Ошибка", "Проверьте правильность ввода Пароля", QtGui.QMessageBox.Close)
            self.InputPassw.setText("")

    # """заполнение списка пользователей, пароль хранится в роле"""
# def AddListUser():
#         for n in range(0,arr.__len__()):
#             edtInputUser = window.edtInputUser.addItem(arr[n][1], arr[n][2])
#
    def initBD(self):
        con = sqlite3.connect("lombard1.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM user")
        arr = cur.fetchall()

        for n in range(0,arr.__len__()):
            edtInputUser = self.edtInputUser.addItem(arr[n][1], arr[n][2])

        cur.close()
        con.close()


if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.show()
   # MyWindow()
    sys.exit(app.exec_())

#class startApp():
    #global window,MainWindow#,wndSprKlients

    #app = QtGui.QApplication(sys.argv)


    #MainWindow = uic.loadUi("MainWindow.ui")
    #wndSprKlients = uic.loadUi("WindowSprKlients.ui")

    #initialWindows()
    #window.initBD()


    #app.exec()  # запускает приложение

    #sys.exit(app.exec_())

