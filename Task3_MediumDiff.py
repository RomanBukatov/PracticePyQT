import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Калькулятор")
        self.setGeometry(100, 100, 300, 250)

        self.layout = QVBoxLayout()

        self.input1 = QLineEdit(self)
        self.input1.setPlaceholderText("Введите первое число")
        self.layout.addWidget(self.input1)

        self.input2 = QLineEdit(self)
        self.input2.setPlaceholderText("Введите второе число")
        self.layout.addWidget(self.input2)

        self.result_label = QLabel("Результат: ", self)
        self.layout.addWidget(self.result_label)

        self.add_button = QPushButton("Сложение", self)
        self.add_button.clicked.connect(self.add_numbers)
        self.layout.addWidget(self.add_button)

        self.subtract_button = QPushButton("Вычитание", self)
        self.subtract_button.clicked.connect(self.subtract_numbers)
        self.layout.addWidget(self.subtract_button)

        self.multiply_button = QPushButton("Умножение", self)
        self.multiply_button.clicked.connect(self.multiply_numbers)
        self.layout.addWidget(self.multiply_button)

        self.divide_button = QPushButton("Деление", self)
        self.divide_button.clicked.connect(self.divide_numbers)
        self.layout.addWidget(self.divide_button)

        self.setLayout(self.layout)

    def add_numbers(self):
        num1 = float(self.input1.text())
        num2 = float(self.input2.text())
        result = num1 + num2
        self.result_label.setText(f"Результат: {result}")

    def subtract_numbers(self):
        num1 = float(self.input1.text())
        num2 = float(self.input2.text())
        result = num1 - num2
        self.result_label.setText(f"Результат: {result}")

    def multiply_numbers(self):
        num1 = float(self.input1.text())
        num2 = float(self.input2.text())
        result = num1 * num2
        self.result_label.setText(f"Результат: {result}")

    def divide_numbers(self):
        num1 = float(self.input1.text())
        num2 = float(self.input2.text())
        if num2 != 0:
            result = num1 / num2
            self.result_label.setText(f"Результат: {result}")
        else:
            self.result_label.setText("Ошибка: Деление на ноль")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
