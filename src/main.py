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

    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info()
    window.addWidgetToVLayout(info)
    info.setText('Jogue com alguem! ')
    
    # Configurando botões Grid
    buttonsGrid = ButtonsGrid(window, info)
    window.vLayout.addLayout(buttonsGrid)

# Condição para aparecer o ícone na barra de tarefas (windows).
    if sys.platform.startswith('win'):
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            u'CompanyName.ProductName.SubProduct.VersionInformation')
         # Arbitrary string 

    # Executando tudo
    window.adjustFixedSize()
    window.show()
    app.exec()

