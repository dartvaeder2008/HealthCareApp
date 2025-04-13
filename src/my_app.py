from inst import*
from PyQt5.QtWidgets import *
from second_win import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear() # встановлює, як виглядатиме вікно
        self.initUI() # створюємо та налаштовуємо графічкі елементи
        self.connects() # встановлює зв'язки між елементами
        self.show() # зробити вікно видимим / старт

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
        
    def initUI(self):
        self.hello_text = QLabel(self.hello_text)
        self.instruction = QLabel(self.instruction)
        self.button = QPushButton(self.button)
        self.layout = QVBoxLayout()

        
    def connects(self):
        self.btn_next.connect(self. next_click)

    def next_click(self):
        self.hide()

app = QApplication([])
mw = MainWin()
app.exec_()