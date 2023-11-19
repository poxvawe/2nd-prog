import sys
import random

from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class MyProgram(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.drawButton.clicked.connect(self.run)

        self.radius = 0
        self.center_x = 0
        self.center_y = 0

    def run(self):
        self.radius = random.randint(13, 123)
        self.center_x = random.randint(self.radius, self.width() - self.radius)
        self.center_y = random.randint(self.radius, self.height() - self.radius)

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)

        color = QColor(255, 255, 0)
        painter.setPen(color)

        painter.drawEllipse(self.center_x - self.radius, self.center_y - self.radius, 2 * self.radius, 2 * self.radius)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyProgram()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
