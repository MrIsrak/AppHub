from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys

def on_key_press(event):
    if event.key() == Qt.Key_Escape:
        app.quit()
        print('Выход из приложения')



class MainWindow(QMainWindow): # главное окно
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
        self.setupbuttons()
    def setupUi(self):
        self.setWindowTitle("Hello, world") # заголовок окна
        self.move(400, 500) # положение окна
        self.resize(1200, 800) # размер окна
        self.lbl = QLabel('<h1>Hello, world!!!<h1>', self)
        self.lbl.setAlignment(Qt.AlignCenter)  # Выравнивание текста по центру метки
        self.setCentralWidget(self.lbl)  # Устанавливаем метку как центральный виджет
    def setupbuttons(self):
        self.btn = QPushButton(self)
        self.btn.setText("Button1")
        self.btn.move(50,20)
        self.btn.clicked.connect( self.b1_clicked)
    def b1_clicked(self):
        print("кнопка нажата")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    win.keyPressEvent = on_key_press
    sys.exit(app.exec_()) 