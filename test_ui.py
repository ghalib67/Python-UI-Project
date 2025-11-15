from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout, QPushButton,
    QLineEdit, QLabel, QListWidget, QGridLayout,
    QDialog, QScrollArea, QSizePolicy,QGraphicsDropShadowEffect,
    
)
from PyQt6.QtGui import QPixmap, QColor, QIcon
from PyQt6.QtCore import Qt
import sys

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFrame
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class SideBar(QFrame):
    def __init__(self):
        super().__init__()

        self.setFixedWidth(230)

        # Use QFrame + stylesheet for rounded corners
        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.setStyleSheet("""
            QFrame {
                background-color: #1a1a1a;
                border-radius: 15px;
            }
            QPushButton {
                border-radius: 20px;
                background-color: green;
            }
        """)

        layout = QVBoxLayout()
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)

        # Image
        label = QLabel()
        pixmap = QPixmap("images/1h8LDrT_.jpeg").scaled(120, 120, Qt.AspectRatioMode.KeepAspectRatio)
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        # Button
        add_task = QPushButton("Add a task")
        add_task.setFixedSize(150, 40)

        # Focus mode button (no functionality as requested)
        focus_btn = QPushButton("Focus mode")
        focus_btn.setFixedSize(150, 40)

        # Time label (static placeholder)
        time_label = QLabel("Time now XXXX")
        time_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        time_label.setStyleSheet("color: white;")

        layout.addWidget(label)
        layout.addWidget(time_label)
        layout.addWidget(add_task)
        layout.addWidget(focus_btn)

        self.setLayout(layout)


class TitleCard(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
            background-color: #1a1a1a;
            border-radius: 15px;
        """)
        layout = QVBoxLayout()
        label = QLabel("Main Hub")
        label.setStyleSheet("color: white; font-size: 20px;")
        layout.addWidget(label)
        self.setLayout(layout)

class contentCard(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
            background-color: white;
            border-radius: 15px;
        """)
        
        layout = QVBoxLayout()
        label = QLabel("Main Hub")
        label.setStyleSheet("color: black;")
        layout.addWidget(label)
        self.setLayout(layout)
        
class MainHub(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
            background-color: #1a1a1a;
            border-radius: 15px;
        """)
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
        #layout.addWidget(TitleCard(),1)
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
        self.h_layout.setSpacing(0)
        self.h_layout.setContentsMargins(0, 0, 0, 0)

        main_widget.setLayout(self.h_layout)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()