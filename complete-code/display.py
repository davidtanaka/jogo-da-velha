from PySide6.QtWidgets import QLineEdit
from PySide6.QtGui import Qt

class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    # Configurando o Display
    def configStyle(self):
        margins = [15 for _ in range(4)]
        self.setStyleSheet('font-size: 33px;')
        self.setMinimumHeight(20 * 3)
        self.setMinimumWidth(24)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margins)
        self.setPlaceholderText('Digite seu nome: ')