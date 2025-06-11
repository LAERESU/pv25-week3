import sys
import random
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mouse Tracker | Yusril Ibtida Ramdhani - F1D022102")
        self.setGeometry(100, 100, 500, 400)

        self.label = QLabel("Move your mouse here", self)
        self.label.move(100, 100)
        self.label.setStyleSheet("background-color: lightgray; padding: 5px;")
        self.setMouseTracking(True)
        self.label.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        x = event.x()
        y = event.y()
        self.label.setText(f"Mouse at ({x}, {y})")

    def enterEvent(self, event):
        self.move_label()

    def move_label(self):
        max_x = self.width() - self.label.width()
        max_y = self.height() - self.label.height()
        new_x = random.randint(0, max_x)
        new_y = random.randint(0, max_y)
        self.label.move(new_x, new_y)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
