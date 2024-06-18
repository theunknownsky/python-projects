from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from account import Account
from login import Login
import errorDialogs as ed
Form, Window = uic.loadUiType("ui_files/register.ui")

class Registration(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Form()
        self.ui.setupUi(self)
        self.ui.regBtn.clicked.connect(self.registerAcct)
        
    def registerAcct(self):
        try:
            firstname = self.ui.regFirstName.text()
            lastname = self.ui.regLastName.text()
            age = self.ui.regAge.text()
            username = self.ui.regUsername.text()
            password = self.ui.regPassword.text()
            if len(firstname) == 0:
                ed.showDialog("Empty Field", "Please fill out the First Name field.", QMessageBox.Icon.Warning)
            elif len(lastname) == 0:
                ed.showDialog("Empty Field", "Please fill out the Last Name field.", QMessageBox.Icon.Warning)
            elif len(age) == 0:
                ed.showDialog("Empty Field", "Please fill out the Age field.", QMessageBox.Icon.Warning)
            elif len(username) == 0:
                ed.showDialog("Empty Field", "Please fill out the Username field.", QMessageBox.Icon.Warning)
            elif len(password) == 0:
                ed.showDialog("Empty Field", "Please fill out the Password field.", QMessageBox.Icon.Warning)
            else:
                try:
                    age = int(age)
                    if age < 18:
                        ed.showDialog("Age Requirement", "You are not yet 18+ to register in this form.", QMessageBox.Icon.Warning)
                    elif len(password) < 8:
                        ed.showDialog("Password Requirement", "You must enter 8 or more characters for your password.", QMessageBox.Icon.Warning)
                    else:
                        currentAcct = Account(firstname, lastname, age, username, password)
                        ed.showDialog("Registration", "You are now registered!", QMessageBox.Icon.Information)
                        self.login_window = Login()
                        self.login_window.storeAccount(currentAcct)
                        self.login_window.show()
                        self.close() 
                except ValueError:
                    ed.showDialog("Wrong Input", "Please enter a number in the Age field.", QMessageBox.Icon.Warning)  
        except Exception as e:
            ed.showDialog("Error!", str(e), QMessageBox.Icon.Critical)
    
        