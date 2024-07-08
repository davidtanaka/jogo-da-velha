from PySide6.QtWidgets import QGridLayout, QPushButton

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        self.setFont(font)
        self.setMinimumSize(55, 55)

class ButtonsOptions(QGridLayout):
    _buttons = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
        ]
    
    def _makeGrid(self):
        for rowNumber, row in enumerate(self._buttons): # type: ignore
            for colNumber, buttonText in enumerate(row):
                button = Button(buttonText)