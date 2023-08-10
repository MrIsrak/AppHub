import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QLabel
from PyQt5.uic import loadUi

def on_key_press(event):
    if event.key() == Qt.Key_Escape:
        app.quit()
        print('Выход из приложения')


class CustomLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)  # Enable drop events for the label

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            if urls:
                image_path = urls[0].toLocalFile()
                pixmap = QPixmap(image_path)
                self.setPixmap(pixmap)


#creating class for the window
class MainWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        #load ui from file
        loadUi(r"C:\Users\evgen\OneDrive\Рабочий стол\пайтон\AppHub\AppHub\PyQt\ui.ui", self)
        self.browse.clicked.connect(self.browsefiles)
        self.label_widget = self.findChild(QtWidgets.QLabel, "dragdrop", )    # Override the setPixmap method to call the superclass implementation
        self.custom_label = CustomLabel(self.label_widget)
    def setPixmap(self, image):
        super().setPixmap(image)
    
    #opening folder to pick file
    def browsefiles(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Open file', 'D:/codefirst.io/PyQt5 tutorials/Browse Files', 'Images (*.png *.jpg *.jpeg *.bmp *.gif *.tif *.tiff *.ico *.svg *.svgz *.wbmp *.webp *.xbm *.xpm *.jp2)')
        self.filename.setText(fname)




if __name__ == '__main__':
    #open window
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    
    # Adjust the window size here
    window_width = 855
    window_height = 550
    
    widget.setFixedWidth(window_width)
    widget.setFixedHeight(window_height)
    
    widget.show()
    sys.exit(app.exec_())
