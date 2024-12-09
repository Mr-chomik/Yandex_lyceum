import sys, random, time

from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.drawer(qp)
            qp.end()

        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def drawer(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        a = random.randrange(5, 300)
        qp.drawEllipse(random.randrange(-10, 280), random.randrange(-10, 280), a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())