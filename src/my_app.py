

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_apper() # встановлює, як виглядатиме вікно
        self.initUI() # створюємо та налаштовуємо графічкі елементи
        self.connects() # встановлює зв'язки між елементами
        self.show() # зробити вікно видимим / старт

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_X, win_y)
        
    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.button = QPushButton(txt_next)
        self.layout = QVBoxLayout()
        self.hello_text.addWidget(self.layout)
        self.instruction.addWidget(self.layout)
        self.button.addWigdet(self.layout)
        
    def connects(self):
        pass
        
