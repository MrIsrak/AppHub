from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
import sys

def on_key_press(event):
    if event.key() == Qt.Key_Escape:
        app.quit()
        print('Выход из приложения')

class MainWindow(QMainWindow): # главное окно
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi(r'C:\Users\evgen\OneDrive\Рабочий стол\пайтон\AppHub\AppHub\PyQt\ui.ui', self)  # Provide the full path to the ui.ui file
        self.browse.clicked.connect(self.browsefiles)
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Hello, world") # заголовок окна
        self.move(400, 500) # положение окна
        self.resize(1200, 800) # размер окна

    def browsefiles(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Open file', r'C:\Users\evgen\OneDrive\Рабочий стол\пайтон\AppHub\AppHub', 'Images (*.png *.xmp *.jpg)')
        self.filename.setText(fname)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    win.keyPressEvent = on_key_press
    sys.exit(app.exec_())
