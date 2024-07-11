from PySide6.QtWidgets import QGridLayout, QWidget, QPushButton
from main_window import MainWindow             

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
        self.state = None  # Inicialmente nenhum estado

    def configStyle(self):
        font = self.font()
        self.setFont(font)
        self.setMinimumSize(90, 90)
        self.setProperty('cssClass', 'specialButton')

    def setState(self, state):
        self.state = state
        self.setText(state)


class ButtonsGrid(QGridLayout):
    def __init__(self, window: 'MainWindow', *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._window = window  # Passamos a janela principal recebida como parâmetro
        self.current_turn = 'X'  # Inicialmente, começa com 'X'
        self._gridMask = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]
        self._createButtons()

    def _createButtons(self):
        for rowNumber, row in enumerate(self._gridMask):
            for colNumber, buttonText in enumerate(row):
                button = Button(buttonText)
                button.setStyleSheet('font-size: 60px; width: 70px;')
                button.clicked.connect(lambda _, b=button: self.buttonClicked(b))
                self.addWidget(button, rowNumber, colNumber)

    def buttonClicked(self, button):
        if button.state is None:  # Verifica se o botão ainda não foi marcado
            button.setState(self.current_turn)
             # Alterna entre 'X' e 'O'
            self.current_turn = 'O' if self.current_turn == 'X' else 'X' 