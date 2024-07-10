import sys
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow,
                               QPushButton, QWidget)

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('Minha janela bonita')


botao = QPushButton('n')
botao.setStyleSheet('font-size: 30px;')

botao2 = QPushButton('n')
botao2.setStyleSheet('font-size: 30px;')

botao3 = QPushButton('n')
botao3.setStyleSheet('font-size: 30px;')

botao4 = QPushButton('n')
botao4.setStyleSheet('font-size: 30px;')

botao5 = QPushButton('n')
botao5.setStyleSheet('font-size: 30px;')

botao6 = QPushButton('n')
botao6.setStyleSheet('font-size: 30px;')

botao7 = QPushButton('n')
botao7.setStyleSheet('font-size: 30px;')

botao8 = QPushButton('n')
botao8.setStyleSheet('font-size: 30px;')

botao9 = QPushButton('n')
botao9.setStyleSheet('font-size: 30px;')


central_widget = QWidget()
layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao, 1, 1)
layout.addWidget(botao2, 1, 2)
layout.addWidget(botao3, 1, 3)
layout.addWidget(botao4, 2, 1)
layout.addWidget(botao5, 2, 2)
layout.addWidget(botao6, 2, 3)
layout.addWidget(botao7, 3, 1)
layout.addWidget(botao8, 3, 2)
layout.addWidget(botao9, 3, 3)

central_widget.show()
app.exec()
