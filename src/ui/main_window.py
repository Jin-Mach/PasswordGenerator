from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QGroupBox, QSlider, \
    QGridLayout, QCheckBox, QApplication, QLineEdit

from src.ui.dialog.dialog_manager import DialogManager
from src.utilities.exception_manager import ExceptionManager
from src.utilities.generate_password import password_generator


# noinspection PyUnresolvedReferences
class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Password generator")
        self.setFixedSize(450, 300)
        self.create_gui()
        self.center_application()

    def create_gui(self) -> None:
        central_widget = QWidget()
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.create_password_widget())
        main_layout.addWidget(self.create_settings_widget())
        main_layout.addWidget(self.create_button_widget())
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def create_password_widget(self) -> QWidget:
        password_widget = QWidget()
        password_layout = QVBoxLayout()
        text_label = QLabel("Pasword:   ")
        text_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.password_lineedit = QLineEdit()
        self.password_lineedit.setText("*****")
        self.password_lineedit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.password_lineedit.setFont(QFont("Arial", 20))
        self.password_lineedit.setReadOnly(True)
        copy_layout = QHBoxLayout()
        copy_button = QPushButton("click here to copy password")
        copy_button.clicked.connect(self.copy_to_clipboard)
        copy_layout.addStretch()
        copy_layout.addWidget(copy_button)
        copy_layout.addStretch()
        password_layout.addWidget(text_label)
        password_layout.addWidget(self.password_lineedit)
        password_layout.addLayout(copy_layout)
        password_widget.setLayout(password_layout)
        return password_widget

    def create_settings_widget(self) -> QGroupBox:
        settings_groupbox = QGroupBox("settings")
        setting_layout = QVBoxLayout()
        lenght_text_layout = QHBoxLayout()
        lenght_text = QLabel(" password length")
        lenght_text.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.password_length = QLabel("10")
        self.password_length.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.password_slider = QSlider()
        self.password_slider.setRange(5, 20)
        self.password_slider.setValue(10)
        self.password_slider.setOrientation(Qt.Orientation.Horizontal)
        self.password_slider.valueChanged.connect(self.set_password_length)
        check_box_layout = QGridLayout()
        self.uppercase_checkbox = QCheckBox("Uppercase letters (A-Z)")
        self.uppercase_checkbox.setChecked(True)
        self.lowercase_checkbox = QCheckBox("Lowercase letters (a-z)")
        self.numbers_checkbox = QCheckBox("Numbers (0-9)")
        self.symbols_checkbox = QCheckBox("Symbols (!, @, #, etc.)")
        check_box_layout.addWidget(self.uppercase_checkbox, 0, 0)
        check_box_layout.addWidget(self.lowercase_checkbox, 1, 0)
        check_box_layout.addWidget(self.numbers_checkbox, 0, 1)
        check_box_layout.addWidget(self.symbols_checkbox, 1, 1)
        lenght_text_layout.addWidget(lenght_text)
        lenght_text_layout.addWidget(self.password_length)
        setting_layout.addLayout(lenght_text_layout)
        setting_layout.addWidget(self.password_slider)
        setting_layout.addLayout(check_box_layout)
        settings_groupbox.setLayout(setting_layout)
        return settings_groupbox

    def create_button_widget(self) -> QWidget:
        buttons_widget = QWidget()
        buttons_layout = QHBoxLayout()
        self.generate_password_button = QPushButton("Generate password")
        self.generate_password_button.clicked.connect(self.get_password)
        buttons_layout.addStretch()
        buttons_layout.addWidget(self.generate_password_button)
        buttons_layout.addStretch()
        buttons_widget.setLayout(buttons_layout)
        return buttons_widget

    def center_application(self) -> None:
        screen = QApplication.primaryScreen()
        screen_geometry = screen.geometry()
        window_geometry = self.geometry()
        x = (screen_geometry.width() - window_geometry.width()) // 2
        y = (screen_geometry.height() - window_geometry.height()) // 2
        self.move(x, y)

    def set_password_length(self, value) -> None:
        self.password_length.setText(str(value))

    def get_password(self) -> None:
        try:
            password = password_generator(self.password_slider, self.uppercase_checkbox, self.lowercase_checkbox,
                                          self.numbers_checkbox, self.symbols_checkbox)
            self.password_lineedit.setText(password)
        except Exception as e:
            ExceptionManager.exception_handler(e, self)

    def copy_to_clipboard(self) -> None:
        try:
            if self.password_lineedit.text() == "*****":
                DialogManager.show_non_password_error(self)
            else:
                DialogManager.show_password_copied_message()
                clipboard = QApplication.clipboard()
                clipboard.setText(self.password_lineedit.text().strip())
        except Exception as e:
            ExceptionManager.exception_handler(e, self)