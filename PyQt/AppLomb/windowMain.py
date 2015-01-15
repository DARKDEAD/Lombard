__author__ = 'dead'

from PyQt4 import QtCore, QtGui, uic

class startMainWindow:
    def __init__(self,window):
        QtGui.QWidget.show(window)
        #window.setWindowFlags()
        window.setWindowState(QtCore.Qt.WindowMaximized)
        #QtCore.QObject.connect(window.sprKlients, QtCore.SIGNAL("clicked()"), self.showWndSprKlients)

    def showWndSprKlients(self):
        wndSprKlients = uic.loadUi("WindowSprKlients.ui")
        QtGui.QWidget.show(wndSprKlients)