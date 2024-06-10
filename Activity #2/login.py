from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from account import Account
from homepage import Home
import errorDialogs as ed
Form, Window = uic.loadUiType("ui_files/login.ui")

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Form()
        self.ui.setupUi(self)
        self.ui.loginBtn.clicked.connect(self.loginAcct)
        
    def storeAccount(self, a):
        self.account = Account(a.firstname, a.lastname, a.age, a.username, a.password)
        
    def loginAcct(self):
        try:
            username = self.ui.loginUsername.text()
            password = self.ui.loginPassword.text()
            
            if len(username) == 0:
                ed.showDialog("Empty Field", "Please fill out the Username field.", QMessageBox.Icon.Warning)
            elif len(password) == 0:
                ed.showDialog("Empty Field", "Please fill out the Password field.", QMessageBox.Icon.Warning)
            else:
                if(self.account.checkCredentials(username, password)):
                    ed.showDialog("Valid Credentials", "You are now being logged in.", QMessageBox.Icon.Information)
                    self.home_window = Home()
                    self.home_window.storeAccount(self.account)
                    self.home_window.show()
                    self.close()
                    
            
            
        except Exception as e:
            ed.showDialog("Error!", str(e), QMessageBox.Icon.Critical)
    
        