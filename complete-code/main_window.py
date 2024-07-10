from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QWidget, QGridLayout, QLabel

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Configurando o básico do layout
        self.cw = QWidget()
        self.v_layout = QGridLayout()
        self.cw.setLayout(self.v_layout) # type: ignore
        self.setCentralWidget(self.cw)

        # Título da janela
        self.setWindowTitle( 'Jogo da velha ')


    def adjustFixedSize(self) -> None:
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetToVLayout(self, widget: QWidget):
        self.v_layout.addWidget(widget)
