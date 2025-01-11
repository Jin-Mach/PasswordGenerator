import pathlib

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMessageBox


class DialogManager:

    @staticmethod
    def show_error_message(exception: Exception, parent=None) -> None:
        messagebox = QMessageBox(parent)
        messagebox.setWindowIcon(QIcon(str(pathlib.Path(__file__).parent.parent.parent.joinpath("data", "icons", "app_icon.png"))))
        messagebox.setWindowTitle("Error")
        messagebox.setText(f"Unexpected error: {exception}")
        messagebox.exec()

    @staticmethod
    def show_password_error(text: str, parent=None) -> None:
        messagebox = QMessageBox(parent)
        messagebox.setWindowIcon(QIcon(str(pathlib.Path(__file__).parent.parent.parent.joinpath("data", "icons", "app_icon.png"))))
        messagebox.setWindowTitle("Password error")
        messagebox.setText(text)
        messagebox.exec()

    @staticmethod
    def show_non_password_error(parent=None) -> None:
        messagebox = QMessageBox(parent)
        messagebox.setWindowIcon(QIcon(str(pathlib.Path(__file__).parent.parent.parent.joinpath("data", "icons", "app_icon.png"))))
        messagebox.setWindowTitle("Non password error")
        messagebox.setText("Cannot copy: Password is not generated yet.")
        messagebox.exec()

    @staticmethod
    def show_password_copied_message(parent=None) -> None:
        messagebox = QMessageBox(parent)
        messagebox.setWindowIcon(QIcon(str(pathlib.Path(__file__).parent.parent.parent.joinpath("data", "icons", "app_icon.png"))))
        messagebox.setWindowTitle("Password copied")
        messagebox.setText("Password successfully copied to clipboard.")
        messagebox.exec()