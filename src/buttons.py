from PySide6.QtWidgets import QGridLayout, QPushButton
from main_window import MainWindow
from info import Info

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
        self.state = None  # Inicialmente nenhum estado

    def configStyle(self):
        font = self.font()
        self.setFont(font)
        self.setMinimumSize(90, 90)
        
    def setState(self, state):
        self.state = state
        self.setText(state)

    def reset(self):
        self.state = None
        self.setText('')

class ButtonsGrid(QGridLayout):
    def __init__(self, window: 'MainWindow', info: 'Info', *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._window = window  # Passamos a janela principal recebida como parâmetro
        self._info = info  # Adiciona a instância de Info
        self.currentTurn = 'X'  # Inicialmente, começa com 'X'
        self._gridMask = [
            ['', '', ''],
            ['', '', ''],
            ['', '', ''],
        ]
        self.__createButtons()

    def __createButtons(self):
        self.buttons = []
        for rowNumber, row in enumerate(self._gridMask):
            rowButtons = []
            for colNumber, buttonText in enumerate(row):
                button = Button()
                button.setStyleSheet('font-size: 60px; width: 70px;')
                
                button.clicked.connect(lambda _, r=rowNumber, c=colNumber,
                                        b=button: self.buttonClicked(b, r, c))
                self.addWidget(button, rowNumber, colNumber)
                rowButtons.append(button)
            self.buttons.append(rowButtons)


    def buttonClicked(self, button: Button, row: int, col: int):
        if button.state is None:  # Verifica se o botão ainda não foi marcado
            button.setState(self.currentTurn)

            # Atualiza _gridMask na posição do botão clicado
            self._gridMask[row][col] = self.currentTurn  

            # Verifica se alguém venceu
            if self.checkWin():
                self.printResult('Winner is ', self.currentTurn)
                self.resetGame()  # Reinicia o jogo
                return  # Interrompe a função se houver um vencedor

            # Verifica se todos os botões foram clicados e não há vencedor
            if self.checkDraw():
                self.printResult('Results is ', 'DRAW')
                self.resetGame()  # Reinicia o jogo
                return  # Interrompe a função se houver um empate

            # Alterna entre 'X' e 'O'
            self.currentTurn = 'O' if self.currentTurn == 'X' else 'X'

    def checkWin(self):
        # Verificação de linhas
        for row in self._gridMask:
            if row[0] == row[1] == row[2] and row[0] != '':
                return True
        
        # Verificação de colunas
        for col in range(3):
            if (self._gridMask[0][col] == self._gridMask[1][col] ==
                self._gridMask[2][col] and self._gridMask[0][col] != ''):
                return True

        # Verificação das diagonais
        if (self._gridMask[0][0] == self._gridMask[1][1] == self._gridMask[2][2]
            and self._gridMask[0][0] != ''):
            return True
        if (self._gridMask[0][2] == self._gridMask[1][1] == self._gridMask[2][0]
            and self._gridMask[0][2] != ''):
            return True
        
        return False

    def checkDraw(self):
        for row in self._gridMask:
            for cell in row:
                if cell == '':
                    return False
        return True
    

    def resetGame(self):
        self.currentTurn = 'X'  # Reinicia com 'X'
        self._gridMask = [
            ['', '', ''],
            ['', '', ''],
            ['', '', ''],
        ]
        for row in self.buttons:
            for button in row:
                button.reset()  # Redefine cada botão


    def printResult(self, textAnswers, value):
        self._info.setText(f'{textAnswers}: {value}')
