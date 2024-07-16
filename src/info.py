from PySide6.QtWidgets import QLabel, QWidget
from constants import MEDIUM_FONT_SIZE

# Classe para mostrar as contas em cima do display
class Info(QLabel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f'font-size: {MEDIUM_FONT_SIZE}px;')
        from PySide6.QtCore import Qt
        self.setAlignment(Qt.AlignmentFlag.AlignRight)