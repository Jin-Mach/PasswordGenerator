import secrets

from PyQt6.QtWidgets import QSlider, QCheckBox

from src.ui.dialog.dialog_manager import DialogManager

UPPER_CASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER_CASE = "abcdefghijklmnopqrstuvwxyz"
NUMBERS = "0123456789"
SYMBOLS = "!@#$%^&*()-_+="

def password_generator(length: QSlider, upper_case: QCheckBox, lower_case: QCheckBox, numbers: QCheckBox, symbols: QCheckBox) -> str:
    password_length = length.value()
    checkboxes = [upper_case, lower_case, numbers, symbols]
    if not check_settings(checkboxes):
        DialogManager.show_password_error()
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
        return password

def check_settings(settings: list[QCheckBox]) -> bool:
    for setting in settings:
        if setting.isChecked():
            return True
    return False