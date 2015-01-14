__author__ = 'dead'
# -*- coding:utf-8 -*-
"""
окно фиксированное по размерам. Одна кнопка "крестик"
"""
# noinspection PyUnresolvedReferences
from PyQt4 import QtCore, QtGui
import sys

app = QtGui.QApplication(sys.argv)
windows = QtGui.QWidget()
windows.setWindowTitle("First programm")

label = QtGui.QLabel("First programm")

btnQuit = QtGui.QPushButton("Cancel")
btnOK = QtGui.QPushButton("OK")

vbox = QtGui.QVBoxLayout()
hbox = QtGui.QHBoxLayout()


hbox.addWidget(label)
hbox.addWidget(btnQuit)
hbox.addWidget(btnOK)

#windows.setLayout(vbox)
windows.setLayout(hbox)


windows.resize(300, 70)
windows.setWindowFlags(QtCore.Qt.Window |
                       QtCore.Qt.CustomizeWindowHint |
                       QtCore.Qt.WindowTitleHint |
                       QtCore.Qt.WindowCloseButtonHint |
                       QtCore.Qt.MSWindowsFixedSizeDialogHint)
windows.show()
sys.exit(app.exec_())
