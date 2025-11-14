from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout, QPushButton,
    QLineEdit, QLabel, QListWidget, QGridLayout,
    QDialog, QScrollArea, QSizePolicy
)

from PyQt6.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Task Manager App")
        self.setMinimumSize(900,700)
        #The main widget


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()