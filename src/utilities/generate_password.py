import secrets

from PyQt6.QtWidgets import QSlider, QCheckBox, QLineEdit

from src.ui.dialog.dialog_manager import DialogManager

UPPER_CASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER_CASE = "abcdefghijklmnopqrstuvwxyz"
NUMBERS = "0123456789"
SYMBOLS = "!@#$%^&*()-_+="

def password_generator(tab_index: int, length: QSlider, upper_case: QCheckBox, lower_case: QCheckBox, numbers: QCheckBox,
                       symbols: QCheckBox, user_input: QLineEdit) -> str:
    password_length = length.value()
    checkboxes = [upper_case, lower_case, numbers, symbols]
    user_text = user_input.text().strip().replace(" ", "")
    if tab_index == 0:
        if not check_settings(checkboxes):
            DialogManager.show_password_error("You must check one or more options in settings!\n"
                           "Like: uppercase, lowercase, numbers or symbols")
            return ""
        else:
            password_characters = ""
            if upper_case.isChecked():
                password_characters += UPPER_CASE
            if lower_case.isChecked():
                password_characters += LOWER_CASE
            if numbers.isChecked():
                password_characters += NUMBERS
            if symbols.isChecked():
                password_characters += SYMBOLS
            password = "".join(secrets.choice(password_characters) for _ in range(password_length))
    else:
        if len(user_text) < 5:
            DialogManager.show_password_error("To generate a password from custom characters, at least 5 characters must be entered.\n"
                                              "Please fill in the field and try again.")
            user_input.selectAll()
            user_input.setFocus()
            return ""
        else:
            password = "".join(secrets.choice(user_text) for _ in range(password_length))
    return password

def check_settings(settings: list[QCheckBox]) -> bool:
    for setting in settings:
        if setting.isChecked():
            return True
    return False