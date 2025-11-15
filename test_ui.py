from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout, QPushButton,
    QLineEdit, QLabel, QListWidget, QGridLayout,
    QDialog, QScrollArea, QSizePolicy,QGraphicsDropShadowEffect,
    QSpacerItem, QCheckBox, QFrame
    
)
from PyQt6.QtGui import QPixmap, QColor, QIcon
from PyQt6.QtCore import Qt, QTimer, QSize, QPropertyAnimation
import sys

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFrame
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFrame, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

from datetime import datetime

class HoverButton(QPushButton):
    def __init__(self, text, color="#FF6600", hover_color="#FF8533", parent=None):
        super().__init__(text, parent)
        self.default_color = color
        self.hover_color = hover_color
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {self.default_color};
                color: white;
                border-radius: 20px;
                font-weight: bold;
                font-size: 14px;
                padding: 8px;
            }}
        """)
        self.setFixedSize(180, 45)
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(Qt.GlobalColor.transparent)
        self.setGraphicsEffect(self.shadow)

    def enterEvent(self, event):
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {self.hover_color};
                color: white;
                border-radius: 20px;
                font-weight: bold;
                font-size: 14px;
                padding: 8px;
            }}
        """)
        self.shadow.setColor(Qt.GlobalColor.white)
        self.setFixedSize(190, 50) 
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {self.default_color};
                color: white;
                border-radius: 20px;
                font-weight: bold;
                font-size: 14px;
                padding: 8px;
            }}
        """)
        self.shadow.setColor(Qt.GlobalColor.transparent)
        self.setFixedSize(180, 45)
        super().leaveEvent(event)

class SideBar(QFrame):
    def __init__(self):
        super().__init__()
        self.setFixedWidth(230)
        self.setStyleSheet("""
            QFrame {
                background-color: #1a1a1a;
                border-radius: 15px;
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

        self.add_task = HoverButton("Add a Task", color="#FF6600", hover_color="#FF8533")
        layout.addWidget(self.add_task, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.focus_btn = HoverButton("Focus Mode", color="#444444", hover_color="#666666")
        layout.addWidget(self.focus_btn, alignment=Qt.AlignmentFlag.AlignHCenter)
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

        self.setFixedSize(250, 180)
        self.setStyleSheet("""
            QFrame {
                background-color: #2b2b2b;  /* dark grey background */
                border-radius: 15px;
            }
        """)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(10)

        self.label = QLabel(title)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("color: white; font-size: 18px; font-weight: bold;")
        main_layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)

        main_layout.addStretch()

        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        button_layout.setSpacing(10)

        self.do_task_btn = QPushButton("Do Task")
        self.do_task_btn.setFixedSize(70, 30)
        self.do_task_btn.setStyleSheet("""
            QPushButton {
                background-color: #FF6600;  /* orange */
                color: white;
                border-radius: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #FF8533;
            }
        """)
        button_layout.addWidget(self.do_task_btn)
        self.edit_btn = QPushButton("Edit Task")
        self.edit_btn.setFixedSize(70, 30)
        self.edit_btn.setStyleSheet("""
            QPushButton {
                background-color: #444444;  /* grey */
                color: white;
                border-radius: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #666666;
            }
        """)
        button_layout.addWidget(self.edit_btn)

        main_layout.addLayout(button_layout)
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
            if col >= 3:
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