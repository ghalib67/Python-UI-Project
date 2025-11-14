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
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        #creating the sidebar
        sidebar = QWidget()
        sidebar.setStyleSheet("background-color: black;")
        #main hub area
        main_hub = QWidget()
        main_hub.setStyleSheet("background-color: black;")
        #Main layout
        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(sidebar,1)
        self.h_layout.addWidget(main_hub,4)
        
        main_widget.setLayout(self.h_layout)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()