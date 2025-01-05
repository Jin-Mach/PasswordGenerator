from PyQt6.QtWidgets import QMessageBox


class DialogManager:

    @staticmethod
    def show_error_message(exception: Exception, parent=None) -> None:
        messagebox = QMessageBox(parent)
        messagebox.setWindowTitle("Error")
        messagebox.setText(f"Unexpected error: {exception}")
        messagebox.exec()

    @staticmethod
    def show_password_error(parent=None) -> None:
        messagebox = QMessageBox(parent)
        messagebox.setWindowTitle("Password error")
        messagebox.setText("You must check one or more options in settings!\n"
                           "Like: uppercase, lowercase, numbers or symbols")
        messagebox.exec()