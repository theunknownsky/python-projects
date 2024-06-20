import backend.errorDialogs as ed
from PyQt6.QtWidgets import QMessageBox

class Account():
    def __init__(self, firstname, lastname, age, username, password):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.username = username
        self.password = password
        
    def checkCredentials(self, username, password):
        access = False
        if self.username != username:
            ed.showDialog("Wrong Credential", "This user does not exist.", QMessageBox.Icon.Critical)
        elif self.password != password:
            ed.showDialog("Wrong Credential", "You entered a wrong password.", QMessageBox.Icon.Critical)
        else:
            access = True
        return access