# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
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
        MainWindow.resize(748, 596)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 310, 89, 25))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.user_id = QtGui.QLineEdit(self.centralwidget)
        self.user_id.setGeometry(QtCore.QRect(370, 180, 113, 25))
        self.user_id.setStyleSheet(_fromUtf8(""))
        self.user_id.setObjectName(_fromUtf8("user_id"))
        self.pass_word = QtGui.QLineEdit(self.centralwidget)
        self.pass_word.setGeometry(QtCore.QRect(370, 230, 113, 25))
        self.pass_word.setStyleSheet(_fromUtf8(""))
        self.pass_word.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.pass_word.setObjectName(_fromUtf8("pass_word"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 180, 67, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 230, 67, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 120, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 310, 89, 25))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.results_window = QtGui.QLineEdit(self.centralwidget)
        self.results_window.setGeometry(QtCore.QRect(240, 370, 251, 31))
        self.results_window.setObjectName(_fromUtf8("results_window"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 748, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "login", None))
        self.label.setText(_translate("MainWindow", "User ID :", None))
        self.label_2.setText(_translate("MainWindow", "Password", None))
        self.label_3.setText(_translate("MainWindow", "Login Form", None))
        self.pushButton_2.setText(_translate("MainWindow", "sign up", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

