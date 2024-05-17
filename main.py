# main.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox
from backend import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('J-Soft Point of Sale')
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.name_input = QLineEdit()
        self.price_input = QLineEdit()
        self.quantity_input = QLineEdit()

        self.layout.addWidget(QLabel("Name:"))
        self.layout.addWidget(self.name_input)
        self.layout.addWidget(QLabel("Price:"))
        self.layout.addWidget(self.price_input)
        self.layout.addWidget(QLabel("Quantity:"))
        self.layout.addWidget(self.quantity_input)

        add_product_btn = QPushButton('Add Product')
        add_product_btn.clicked.connect(self.add_product)
        self.layout.addWidget(add_product_btn)

    def add_product(self):
        name = self.name_input.text()
        price = float(self.price_input.text())
        quantity = int(self.quantity_input.text())
        add_product_to_inventory(name, price, quantity)
        QMessageBox.information(self, 'Success', 'Product added successfully.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

