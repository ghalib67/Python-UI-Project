from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout, QPushButton,
    QLineEdit, QLabel, QListWidget, QGridLayout,
    QDialog, QScrollArea, QSizePolicy
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import sys

class SideBar(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: black;")
        layout = QVBoxLayout()
        label = QLabel("Sidebar")
        label = QLabel()
        pixmap = QPixmap("images/1h8LDrT_.jpeg")
        pixmap = pixmap.scaled(40, 40, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
        label.setPixmap(pixmap)
        layout.addWidget(label)
        self.setLayout(layout)

class TitleCard(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: black;")
        layout = QVBoxLayout()
        label = QLabel("Main Hub")
        label.setStyleSheet("color: white; font-size: 20px;")
        layout.addWidget(label)
        self.setLayout(layout)

class contentCard(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: white;")
        layout = QVBoxLayout()
        label = QLabel("Main Hub")
        label.setStyleSheet("color: black;")
        layout.addWidget(label)
        self.setLayout(layout)
        
class MainHub(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: black;")
        layout = QVBoxLayout()
        grid = QGridLayout()
        main_widget = QWidget()
        main_widget.setStyleSheet("background-color: black;")
        row = 0
        col = 0
        for i in range(7):
            grid.addWidget(contentCard(), row, col)
            col += 1
            if col >= 3:  # 3 columns for example
                col = 0
                row += 1
        
        main_widget.setLayout(grid)
        layout.addWidget(TitleCard(),1)
        layout.addWidget(main_widget,4)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Task Manager App")
        self.setMinimumSize(900,700)
        #The main widget
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        #creating the sidebar
        self.sidebar = SideBar()
        #main hub area
        main_hub = MainHub()
        #Main layout
        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.sidebar,1)
        self.h_layout.addWidget(main_hub,4)
        
        main_widget.setLayout(self.h_layout)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()