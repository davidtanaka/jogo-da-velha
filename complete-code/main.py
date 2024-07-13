import sys
from main_window import MainWindow
from constants import WINDOW_ICON_PATH
from buttons import ButtonsGrid
from PySide6.QtGui import QIcon
from styles import setupTheme
from PySide6.QtWidgets import QApplication
from display import Display

if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()

    #  Definindo o Ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Display
    display = Display()
    window.addWidgetToVLayout(display)


    # Configurando botões Grid
    buttonsGrid = ButtonsGrid(window)
    window.vLayout.addLayout(buttonsGrid)

    # Executando tudo
    window.adjustFixedSize()
    window.show()
    app.exec()

