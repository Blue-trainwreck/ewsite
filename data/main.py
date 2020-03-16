from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QInputDialog, QColorDialog
from ui_file import Ui_MainWindow
from PyQt5.QtGui import QPainter, QColor, QBrush
import sys
from math import sin, cos, sin, pi


class Dialog(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        kol_side, da = QInputDialog.getInt(self, "Введите количество сторон многоуголника", "", 4, 3, 100)
        if da:
            c = QColorDialog.getColor(title="Введите цвет линий")
            if c.isValid():
                side = self.spinBox.value()
                count = self.spinBox_2.value()
                scale = self.doubleSpinBox.value()
                self.side = side
                self.sw = SquareWindow(side, count, scale, kol_side, c)
                self.sw.show()
                self.hide()



class SquareWindow(QWidget):
    def __init__(self, side, count, scale, kol_side, c):
        super().__init__()
        self.setWindowTitle('Многоугольник')
        self.side = side
        self.c = c
        self.count = count
        self.scale = scale
        self.kol_side = kol_side
        self.setGeometry(50, 50, self.side / sin(180/self.kol_side * pi / 180),
                         self.side / sin(180/self.kol_side * pi / 180))

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setBrush(QColor.fromRgb(255, 255, 255))
        painter.setPen(self.c)

        R = (self.side / sin(180/self.kol_side * pi / 180)) / 2
        painter.drawRect(0, 0, R * 2, R * 2)
        alpha = 45
        points = []
        for _ in range(self.kol_side):
            points.append([(R + (R*cos(alpha * pi / 180)), R + (R*sin(alpha * pi / 180)))])
            alpha += 360 / self.kol_side
        for i in range(self.count - 1):
            for j in range(self.kol_side - 1):
                points[j].append((points[j][i][0] * self.scale + points[j + 1][i][0] * (1 - self.scale),
                                  points[j][i][1] * self.scale + points[j + 1][i][1] * (1 - self.scale)))
            points[j + 1].append((points[j + 1][i][0] * self.scale + points[0][i][0] * (1 - self.scale),
                              points[j + 1][i][1] * self.scale + points[0][i][1] * (1 - self.scale)))

        for i in range(len(points[0])):
            for j in range(self.kol_side - 1):
                painter.drawLine(*points[j][i], *points[j + 1][i])
            painter.drawLine(*points[j + 1][i], *points[0][i])
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Dialog()
    ex.show()
    sys.exit(app.exec_())
