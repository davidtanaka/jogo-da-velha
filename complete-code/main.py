import sys
from main_window import MainWindow
from constants import WINDOW_ICON_PATH
from buttons import ButtonsGrid
from PySide6.QtGui import QIcon
from info import Info
from styles import setupTheme
from PySide6.QtWidgets import QApplication

if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()

    #  Definindo o Ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info()
    window.addWidgetToVLayout(info)
    
    # Configurando botões Grid
    buttonsGrid = ButtonsGrid(window, info)
    window.vLayout.addLayout(buttonsGrid)

    # Executando tudo
    window.adjustFixedSize()
    window.show()
    app.exec()

