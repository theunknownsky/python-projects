from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from account import Account
from pay import Pay
import errorDialogs as ed
Form, Window = uic.loadUiType("ui_files/home.ui")

class Home(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Form()
        self.ui.setupUi(self)
        self.ui.currentOrders.setColumnWidth(0, 190)
        self.ui.currentOrders.setColumnWidth(1, 100)
        self.ui.logoutBtn.clicked.connect(self.logout)
        self.ui.removeBtn.clicked.connect(self.removeFoodItem)
        self.ui.payBtn.clicked.connect(self.payForTotalFee)
        self.ui.burgerBtn.clicked.connect(self.burgerPress)
        self.ui.friesBtn.clicked.connect(self.friesPress)
        self.ui.icedTeaBtn.clicked.connect(self.icedTeaPress)
        self.ui.spagBtn.clicked.connect(self.spagPress)
        self.ui.iceCreamBtn.clicked.connect(self.iceCreamPress)
        self.ui.chickenBtn.clicked.connect(self.chickenPress)
        self.prices = {"Burger": 120, "Fries": 70, "Iced Tea": 60, "Spaghetti": 145, "Ice Cream": 45, "Fried Chicken": 160}
        self.total = 0
        
    def storeAccount(self, a):
        self.account = Account(a.firstname, a.lastname, a.age, a.username, a.password)
        self.ui.welcomePhrase.setText(f"Thank you for logging in, {self.account.firstname} {self.account.lastname}!")
        self.ui.ageShow.setText(f"Age: {self.account.age}")
        self.ui.totalShow.setText(f"Total: {self.total}")
        
    def logout(self):
        ed.showDialog("Logging Out", "You are now being logged out.", QMessageBox.Icon.Information)
        from login import Login
        self.login_window = Login()
        self.login_window.storeAccount(self.account)
        self.login_window.show()
        self.close()
        
    def burgerPress(self):
        self.increaseTotal(self.prices["Burger"])
        self.insertFoodItem(self.ui.currentOrders, "Burger", self.prices["Burger"])
        
    def friesPress(self):
        self.increaseTotal(self.prices["Fries"])
        self.insertFoodItem(self.ui.currentOrders, "Fries", self.prices["Fries"])
        
    def icedTeaPress(self):
        self.increaseTotal(self.prices["Iced Tea"])
        self.insertFoodItem(self.ui.currentOrders, "Iced Tea", self.prices["Iced Tea"])
    
    def spagPress(self):
        self.increaseTotal(self.prices["Spaghetti"])
        self.insertFoodItem(self.ui.currentOrders, "Spaghetti", self.prices["Spaghetti"])
    
    def iceCreamPress(self):
        self.increaseTotal(self.prices["Ice Cream"])
        self.insertFoodItem(self.ui.currentOrders, "Ice Cream", self.prices["Ice Cream"])
    
    def chickenPress(self):
        self.increaseTotal(self.prices["Fried Chicken"])
        self.insertFoodItem(self.ui.currentOrders, "Fried Chicken", self.prices["Fried Chicken"])
    
    def increaseTotal(self, price):
        self.total += price
        self.ui.totalShow.setText(f"Total: {self.total}")
        
    def decreaseTotal(self, price):
        self.total -= price
        self.ui.totalShow.setText(f"Total: {self.total}")
    
    def insertFoodItem(self, table_widget, food, price):
        try:
            row_position = table_widget.rowCount()
            table_widget.insertRow(row_position)
            table_widget.setItem(row_position, 0, QTableWidgetItem(food))
            table_widget.setItem(row_position, 1, QTableWidgetItem(str(price)))
        except Exception as e:
            ed.showDialog("insertFoodItem Error", str(e), QMessageBox.Icon.Critical)
        
    def removeFoodItem(self):
        try:
            row = self.getSelectedRowIndex()
            if row != -1:
                food = self.ui.currentOrders.item(row, 0).text()
                self.decreaseTotal(self.prices[food])
                self.ui.currentOrders.removeRow(row)
                ed.showDialog("Removal Success", f"'{food}' in row {row} has been removed from the current order", QMessageBox.Icon.Information)
        except Exception as e:
            ed.showDialog("removeFoodItem Error", str(e), QMessageBox.Icon.Critical)
        
    def getSelectedRowIndex(self):
        try:
            selected_row = self.ui.currentOrders.currentRow()
            if selected_row != -1:
                print(f"Selected Row Index: {selected_row}")
                return selected_row
            else:
                ed.showDialog("No Selected Item", "Please select an item to remove", QMessageBox.Icon.Warning)
                return -1
        except Exception as e:
            ed.showDialog("getSelectedRowIndex Error", str(e), QMessageBox.Icon.Critical)
            return -1
        
    def payForTotalFee(self):
        self.pay_window = Pay()
        self.pay_window.storeAccount(self.account, self.total)
        self.pay_window.show()
        self.close()   