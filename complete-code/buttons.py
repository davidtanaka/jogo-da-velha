from PySide6.QtWidgets import QGridLayout, QWidget, QPushButton
from main_window import MainWindow             

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        self.setFont(font)
        self.setMinimumSize(90, 90)
        self.setProperty('cssClass', 'specialButton')

class ButtonsGrid(QGridLayout):
    def __init__(self, window: 'MainWindow', *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._window = MainWindow()
        self._gridMask = [
            ['A', 'B', 'C'],
            ['D', 'E', 'F'],
            ['G', 'H', 'I'],
        ]
        self._createButtons()

    def _createButtons(self):
        for rowNumber, row in enumerate(self._gridMask):
            for colNumber, buttonText in enumerate(row):
                button = Button(buttonText)
                button.setStyleSheet('font-size: 60px; width: 70px;')
                self.addWidget(button, rowNumber, colNumber)  
