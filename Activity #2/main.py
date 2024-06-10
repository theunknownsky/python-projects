from PyQt6.QtWidgets import QApplication
from registration import Registration

if __name__ == "__main__":
    mamaril_app = QApplication([])
    mamaril_window = Registration()
    mamaril_window.show()
    mamaril_app.exec()