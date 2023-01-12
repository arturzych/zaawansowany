#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout
from PyQt5.QtGui import QIcon

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