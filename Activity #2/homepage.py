from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from account import Account
import errorDialogs as ed
Form, Window = uic.loadUiType("ui_files/home.ui")

class Home(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Form()
        self.ui.setupUi(self)
        self.ui.logoutBtn.clicked.connect(self.logout)
        
    def storeAccount(self, a):
        self.account = Account(a.firstname, a.lastname, a.age, a.username, a.password)
        self.ui.welcomePhrase.setText(f"Thank you for logging in, {self.account.firstname}!")
        
    def logout(self):
        ed.showDialog("Logging Out", "You are now being logged out.", QMessageBox.Icon.Information)
        from login import Login
        self.login_window = Login()
        self.login_window.storeAccount(self.account)
        self.login_window.show()
        self.close()
    
        