import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt  

class CounterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Счетчик")

        self.layout = QVBoxLayout()
        
        self.label = QLabel("0")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.button = QPushButton("Увеличить")
        self.button.clicked.connect(self.increment_counter)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.counter = 0  # Переменная-счетчик

    def increment_counter(self):
        self.counter += 1
        self.label.setText(str(self.counter))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CounterApp()
    window.show()
    sys.exit(app.exec())
