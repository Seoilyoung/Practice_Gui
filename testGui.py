import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PyQt6.uic import loadUi
from PyQt6.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('Screen.ui', self)
        pixmap = QPixmap('background.png')
        self.label.setPixmap(pixmap)

        # 버튼 연결
        self.button_screen1.clicked.connect(self.show_screen1)
        self.button_screen2.clicked.connect(self.show_screen2)
        self.button_screen3.clicked.connect(self.show_screen3)
        self.button_screen4.clicked.connect(self.show_screen4)
        
    def show_screen1(self):
        self.stackedWidget.setCurrentIndex(0)
    def show_screen2(self):
        self.stackedWidget.setCurrentIndex(1)
    def show_screen3(self):
        self.stackedWidget.setCurrentIndex(2)
    def show_screen4(self):
        self.stackedWidget.setCurrentIndex(3)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
