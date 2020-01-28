from PyQt4 import QtCore, QtGui, uic
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import test
from welcome import Ui_MainWindow
from signup import Ui_signup
import sqlite3
class simplecalc(QtGui.QMainWindow, test.Ui_MainWindow):
        def __init__(self):
                super(self.__class__,self).__init__()
                self.setupUi(self)
                self.pushButton.clicked.connect(self.CalculateTax)
		self.pushButton_2.clicked.connect(self.signUpCheck)
        def CalculateTax(self):
                #print("akash")
		username = str(self.user_id.text())
		print('user',username)
		self.pass_word.setEchoMode(QtGui.QLineEdit.Password)
		password=str(self.pass_word.text())
		#password =str(self.pass_word.text())
		print('pass',password)
		connection = sqlite3.connect("login.db")          #create simple database 
        	result = connection.execute("SELECT * FROM akash WHERE USERNAME = ? AND PASSWORD = ?",(username,password))
        	if(len(result.fetchall()) > 0):
            		print(" Autorised User ! ")
			self.results_window.setText('Authorised User')
            		self.welcomeWindowShow()
        	else:
            		print("User Not Found !")
            		self.results_window.setText('Warning,Invalid Username or Password')
       		connection.close()
	def signUpCheck(self):
                print(" Clicked !")
		#self.signup_window.setText('Account has been created')
               	self.signUpShow()
	def welcomeWindowShow(self):
        	self.welcomeWindow = QtGui.QMainWindow()
        	self.ui = Ui_MainWindow()
        	self.ui.setupUi(self.welcomeWindow)
        	self.welcomeWindow.show()
	def signUpShow(self):
		self.signupWindow = QtGui.QDialog()
		self.ui = Ui_signup()
		self.ui.setupUi(self.signupWindow)
		self.signupWindow.show()
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	window = simplecalc()
	window.show()
	sys.exit(app.exec_())
