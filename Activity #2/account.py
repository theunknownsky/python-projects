import errorDialogs as ed

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
            ed.showDialog("Wrong Credential", "This user does not exist.")
        elif self.password != password:
            ed.showDialog("Wrong Credential", "You entered a wrong password.")
        else:
            access = True
        return access