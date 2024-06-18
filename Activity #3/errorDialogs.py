from PyQt6.QtWidgets import QMessageBox

def showDialog(title, message, icon):
    dlg = QMessageBox()
    dlg.setWindowTitle(title)
    dlg.setText(message)
    dlg.setIcon(icon)
    button = dlg.exec()
    if button == QMessageBox.StandardButton.Ok:
        print(message)
