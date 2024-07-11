import sys
from main_window import MainWindow
from constants import WINDOW_ICON_PATH
from buttons import Button, ButtonsGrid
from PySide6.QtGui import QIcon
from styles import setupTheme
from PySide6.QtWidgets import QApplication, QLabel

if __name__ == '__main__':
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()

    #  Definindo o Ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    buttonsGrid = ButtonsGrid(window)
    window.vLayout.addLayout(buttonsGrid)

    # Executando tudo
    window.adjustFixedSize()
    window.show()
    app.exec()

