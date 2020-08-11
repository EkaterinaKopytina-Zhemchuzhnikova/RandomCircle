import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randint
from gitEllipse import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.test = None
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.radius = randint(0, self.height())
        self.test = True

    def paintEvent(self, event):
        if self.test:
            qp = QPainter(self)
            qp.begin(self)
            qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            qp.drawEllipse(randint(0, self.width() - self.radius), randint(0, self.height() - self.radius),
                           self.radius, self.radius)
            qp.end()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
