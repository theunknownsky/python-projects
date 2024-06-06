from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from mamaril_calculate import CalculatorApp

if __name__ == "__main__":
    Mamaril_app = QApplication([])
    Mamaril_window = CalculatorApp()
    Mamaril_window.show()
    Mamaril_app.exec()