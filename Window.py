# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:/Projetos/Programming/Python/StatisticalDataOrganizer/MainWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(721, 558)
        MainWindow.setMinimumSize(QtCore.QSize(721, 558))
        MainWindow.setMaximumSize(QtCore.QSize(721, 558))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.txtValues = QtGui.QPlainTextEdit(self.centralwidget)
        self.txtValues.setGeometry(QtCore.QRect(40, 70, 641, 171))
        self.txtValues.setObjectName(_fromUtf8("txtValues"))
        self.btnGen = QtGui.QPushButton(self.centralwidget)
        self.btnGen.setGeometry(QtCore.QRect(40, 260, 81, 23))
        self.btnGen.setObjectName(_fromUtf8("btnGen"))
        self.btnClean = QtGui.QPushButton(self.centralwidget)
        self.btnClean.setGeometry(QtCore.QRect(140, 260, 81, 23))
        self.btnClean.setObjectName(_fromUtf8("btnClean"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 40, 151, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(40, 310, 641, 171))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.chrDecimal = QtGui.QLineEdit(self.groupBox)
        self.chrDecimal.setGeometry(QtCore.QRect(220, 60, 21, 20))
        self.chrDecimal.setText(_fromUtf8(""))
        self.chrDecimal.setMaxLength(1)
        self.chrDecimal.setCursorPosition(0)
        self.chrDecimal.setAlignment(QtCore.Qt.AlignCenter)
        self.chrDecimal.setObjectName(_fromUtf8("chrDecimal"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 611, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.txtExclude = QtGui.QLineEdit(self.groupBox)
        self.txtExclude.setGeometry(QtCore.QRect(20, 130, 221, 20))
        self.txtExclude.setObjectName(_fromUtf8("txtExclude"))
        self.chrSplit = QtGui.QLineEdit(self.groupBox)
        self.chrSplit.setGeometry(QtCore.QRect(220, 20, 21, 20))
        self.chrSplit.setMaxLength(1)
        self.chrSplit.setAlignment(QtCore.Qt.AlignCenter)
        self.chrSplit.setObjectName(_fromUtf8("chrSplit"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 171, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 171, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.btnPath = QtGui.QPushButton(self.centralwidget)
        self.btnPath.setGeometry(QtCore.QRect(240, 260, 81, 23))
        self.btnPath.setObjectName(_fromUtf8("btnPath"))
        self.txtPath = QtGui.QLineEdit(self.centralwidget)
        self.txtPath.setGeometry(QtCore.QRect(320, 261, 361, 22))
        self.txtPath.setObjectName(_fromUtf8("txtPath"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 721, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionSobre = QtGui.QAction(MainWindow)
        self.actionSobre.setObjectName(_fromUtf8("actionSobre"))
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Statistical Data Organizer", None))
        self.btnGen.setText(_translate("MainWindow", "Generate", None))
        self.btnClean.setText(_translate("MainWindow", "Clean", None))
        self.label.setText(_translate("MainWindow", "Enter the values to organize", None))
        self.label_4.setText(_translate("MainWindow", "Set the unnecessary characters to be ignored, such as the Thousands separator among others, separate them with a space", None))
        self.label_2.setText(_translate("MainWindow", "Set the value separator character", None))
        self.label_3.setText(_translate("MainWindow", "Set the decimal separator character", None))
        self.btnPath.setText(_translate("MainWindow", "Output Path", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionSobre.setText(_translate("MainWindow", "Sobre", None))
        self.actionHelp.setText(_translate("MainWindow", "Data Organizer Help", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))

