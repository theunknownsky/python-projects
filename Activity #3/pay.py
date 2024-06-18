from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from account import Account
# from homepage import Home
import errorDialogs as ed
Form, Window = uic.loadUiType("ui_files/pay.ui")

class Pay(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Form()
        self.ui.setupUi(self)
        self.ui.payBtn.clicked.connect(self.payPrice)
        
    def storeAccount(self, a, price):
        self.account = Account(a.firstname, a.lastname, a.age, a.username, a.password)
        self.price = price
        self.ui.totalPriceShow.setText(f"{self.price}")
        self.checkDiscount()
        
    def checkDiscount(self):
        if self.account.age >= 60:
            self.discountedPrice = self.price * 0.8
            self.ui.discPriceShow.setText(f"{self.discountedPrice}")
        else:
            self.discountedPrice = self.price
            self.ui.discPriceShow.setText(f"Not eligible")
        
    def payPrice(self):
        try:
            try:
                toPay = float(self.ui.yourMoney.text())
                if toPay >= self.discountedPrice:
                    ed.showDialog("Change", f"Your change is {toPay - self.discountedPrice}. Thank you!", QMessageBox.Icon.Information)
                    self.close()
                else:
                    ed.showDialog("Insufficient Money", "Given money is not enough.", QMessageBox.Icon.Warning)
            except ValueError:
                ed.showDialog("Wrong Input", "Please enter a number in the Your Money field.", QMessageBox.Icon.Warning)
        except Exception as e:
            ed.showDialog("payPrice Error", str(e), QMessageBox.Icon.Critical)