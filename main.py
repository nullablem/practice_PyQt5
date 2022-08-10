import sys

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.show()

    def initUI(self):
        # this will hide the title bar
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.setGeometry(100, 100, 300, 300)

    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = event.globalPos()

run = QApplication(sys.argv)
app = MyApp()
run.exec_()