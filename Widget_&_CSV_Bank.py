#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout

from PyQt5.QtWidgets import QHBoxLayout, QLineEdit

class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interface()

    def interface(self): # GUI - Graphical User Interface

        # labels
        label1 = QLabel("Kategoria:", self)
        label2 = QLabel("Wartość:", self)

        # placing the labels on the Window
        position = QGridLayout()
        position.addWidget(label1, 0, 0)
        position.addWidget(label2, 0, 1)

        # 1-lined edit field
        self.category = QLineEdit('Tutaj umieść nazwę kategorii')
        self.amount = QLineEdit('Tutaj umieść wartość')

        # placing the edit fields on the Window
        position.addWidget(self.category, 1, 0)
        position.addWidget(self.amount, 1, 1)

        # connecting defined layout(układu) with created window
        self.setLayout(position)

        # size and positioning of the window
        self.setGeometry(0, 0, 400, 100)
        self.setWindowTitle("Zestawienie bankowe")
        self.show()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    o = Window()
    sys.exit(app.exec_())