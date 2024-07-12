from PySide6.QtWidgets import QGridLayout, QPushButton
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
        self.currentTurn = 'X'  # Inicialmente, começa com 'X'
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
                
                button.clicked.connect(lambda _, r=rowNumber, c=colNumber,
                                        b=button: self.buttonClicked(b, r, c))
                self.addWidget(button, rowNumber, colNumber)

    def buttonClicked(self, button: Button, row: int, col: int):
        if button.state is None:  # Verifica se o botão ainda não foi marcado
            button.setState(self.currentTurn)

            # Atualiza _gridMask na posição do botão clicado
            self._gridMask[row][col] = self.currentTurn  
            print(self._gridMask)
            # Alterna entre 'X' e 'O'
            self.currentTurn = 'O' if self.currentTurn == 'X' else 'X'

