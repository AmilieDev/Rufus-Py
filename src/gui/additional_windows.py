# Additional windows, such as logging, and about.

from PyQt6.QtWidgets import (QVBoxLayout, QDialog, QTextEdit)
from PyQt6.QtGui import QFont

class LogWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RufusPy: Logs")
        self.resize(650, 450)
        layout = QVBoxLayout()
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        self.log_text.setFont(QFont("Consolas", 9))
        self.log_text.setStyleSheet("background-color: white; border: 1px solid #ccc;")
        layout.addWidget(self.log_text)
        self.setLayout(layout)

class AboutWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RufusPy: About")
        self.resize(650, 450)
        layout = QVBoxLayout()
        self.about_text = QTextEdit()
        self.about_text.setReadOnly(True)
        self.about_text.setFont(QFont("Consolas", 9))
        self.about_text.setStyleSheet("background-color: white; border: 1px solid #ccc;")
        layout.addWidget(self.about_text)
        self.setLayout(layout)