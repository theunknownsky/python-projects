from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
Form, Window = uic.loadUiType("calculator.ui")

class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Form()
        self.ui.setupUi(self)
        self.ui.calc_btn.clicked.connect(self.calculate)
        self.ui.reset_btn.clicked.connect(self.resetDetails)
    
    def calculate(self):
        result = None
        try:
            num1 = float(self.ui.num1.text())
            num2 = float(self.ui.num2.text())
            operation = self.ui.operation.currentText()
            
            if operation == "+":
                result = num1 + num2
            if operation == "-":
                result = num1 - num2
            if operation == "*":
                result = num1 * num2
            if operation == "/":
                result = num1 / num2
        except (ValueError, ZeroDivisionError) as e:
            result = f"Error: {e}"
        finally:
            self.ui.result.setText(str(result))
    
    def resetDetails(self):
        self.ui.num1.setText("")
        self.ui.num2.setText("")
        self.ui.result.setText("--")
        