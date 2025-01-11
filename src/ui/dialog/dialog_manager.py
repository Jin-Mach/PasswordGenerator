from PyQt6.QtWidgets import QMessageBox


class DialogManager:

    @staticmethod
    def show_error_message(exception: Exception, parent=None) -> None:
        messagebox = QMessageBox(parent)
        messagebox.setWindowTitle("Error")
        messagebox.setText(f"Unexpected error: {exception}")
        messagebox.exec()

    @staticmethod
    def show_password_error(text: str, parent=None) -> None:
        messagebox = QMessageBox(parent)
        messagebox.setWindowTitle("Password error")
        messagebox.setText(text)
        messagebox.exec()

    @staticmethod
    def show_non_password_error(parent=None) -> None:
        message = QMessageBox(parent)
        message.setWindowTitle("Non password error")
        message.setText("Cannot copy: Password is not generated yet.")
        message.exec()

    @staticmethod
    def show_password_copied_message(parent=None) -> None:
        message = QMessageBox(parent)
        message.setWindowTitle("Password copied")
        message.setText("Password successfully copied to clipboard.")
        message.exec()