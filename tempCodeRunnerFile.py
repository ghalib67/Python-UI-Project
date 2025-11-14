class SideBar(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setObjectName("SideBar")

        self.setStyleSheet("""
            background-color: #1a1a1a;
            border-radius: 15px;
        """)
        layout = QVBoxLayout()
        
        label = QLabel("Sidebar")
        label = QLabel()
        pixmap = QPixmap("images/1h8LDrT_.jpeg")
        pixmap = pixmap.scaled(190, 190, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        
        add_task = QPushButton("Add a task")
        add_task.setFixedSize(150,40)
        add_task.setStyleSheet("border-radius: 0px;")
        today = QLabel("DAte is xx xx xx")
        focus_mode = QPushButton("Focus mode")
        
        
        layout.addWidget(label)
        layout.addWidget(add_task)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)

        self.setLayout(layout)