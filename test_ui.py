from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout, QPushButton,
    QLineEdit, QLabel, QListWidget, QGridLayout,
    QDialog, QScrollArea, QSizePolicy,QGraphicsDropShadowEffect,
    QSpacerItem, QCheckBox, QFrame,
    
)
from PyQt6.QtGui import QPixmap, QColor, QIcon
from PyQt6.QtCore import Qt, QTimer
import sys

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFrame
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFrame, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

from datetime import datetime

class SideBar(QFrame):
    def __init__(self):
        super().__init__()

        self.setFixedWidth(230)
        self.setStyleSheet("""
            QFrame {
                background-color: #1a1a1a;
                border-radius: 15px;
            }
            QPushButton#primary {
                background-color: #FF6600; 
                color: white;
                border-radius: 20px;
                font-weight: bold;
                font-size: 14px;
                padding: 8px;
            }
            QPushButton#primary:hover {
                background-color: #FF8533;  /* lighter orange */
            }
            QPushButton#secondary {
                background-color: #444444;  
                color: white;
                border-radius: 20px;
                font-weight: normal;
                font-size: 14px;
                padding: 8px;
            }
            QPushButton#secondary:hover {
                background-color: #666666;  /* lighter grey */
            }
        """)

        layout = QVBoxLayout()
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(20)

        label = QLabel()
        pixmap = QPixmap("images/1h8LDrT_.jpeg").scaled(120, 120, Qt.AspectRatioMode.KeepAspectRatio)
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(label)

        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        add_task = QPushButton("Add a Task")
        add_task.setObjectName("primary")
        add_task.setFixedSize(180, 45)

        shadow1 = QGraphicsDropShadowEffect()
        shadow1.setBlurRadius(15)
        shadow1.setXOffset(0)
        shadow1.setYOffset(0)
        shadow1.setColor(Qt.GlobalColor.transparent)
        add_task.setGraphicsEffect(shadow1)
        add_task.enterEvent = lambda e, s=shadow1: s.setColor(Qt.GlobalColor.white)
        add_task.leaveEvent = lambda e, s=shadow1: s.setColor(Qt.GlobalColor.transparent)
        layout.addWidget(add_task, alignment=Qt.AlignmentFlag.AlignHCenter)


        focus_btn = QPushButton("Focus Mode")
        focus_btn.setObjectName("secondary")
        focus_btn.setFixedSize(180, 45)
        shadow2 = QGraphicsDropShadowEffect()
        shadow2.setBlurRadius(15)
        shadow2.setXOffset(0)
        shadow2.setYOffset(0)
        shadow2.setColor(Qt.GlobalColor.transparent)
        focus_btn.setGraphicsEffect(shadow2)
        focus_btn.enterEvent = lambda e, s=shadow2: s.setColor(Qt.GlobalColor.white)
        focus_btn.leaveEvent = lambda e, s=shadow2: s.setColor(Qt.GlobalColor.transparent)
        layout.addWidget(focus_btn, alignment=Qt.AlignmentFlag.AlignHCenter)

        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))


        self.time_label = QLabel()
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.time_label.setStyleSheet("color: #CCCCCC; font-weight: bold;")
        layout.addWidget(self.time_label)

        self.setLayout(layout)
        timer = QTimer(self)
        timer.timeout.connect(self.update_time)
        timer.start(1000)
        self.update_time()

    def update_time(self):
        now = datetime.now()
        self.time_label.setText(now.strftime("Time now: %H:%M:%S"))


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

class contentCard(QFrame):
    def __init__(self, title="Task 1"):
        super().__init__()

        self.setMinimumSize(200,150)
        self.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 15px;
            }
        """)
        main_layout = QVBoxLayout()
        self.button = QPushButton("Do Task")
        self.button.setFixedSize(100,40)
        self.button.setStyleSheet("""
            QPushButton {
                background-color: lightgray;
                border-radius: 10px;
            }
        """)
        main_layout.addWidget(self.button,alignment=Qt.AlignmentFlag.AlignBottom)

        self.setLayout(main_layout)
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