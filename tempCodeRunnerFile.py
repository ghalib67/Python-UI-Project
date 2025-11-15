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