from PySide2.QtCore import QPoint, Qt
from PySide2.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton


class CustomBar(QWidget):

    def __init__(self, parent):
        super(CustomBar, self).__init__()
        self.parent = parent

        # read style sheet
        with open('./QSS/customBar.qss', 'r', encoding='utf-8') as f:
            self.setStyleSheet(f.read())
            f.close()

        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.title = QLabel("PySide2 - Qt Framework")
        self.title.setObjectName('titleBar')

        btn_size = 30

        self.btn_close = QPushButton("x")
        self.btn_close.setObjectName('closeButton')
        self.btn_close.setFixedSize(btn_size,btn_size)

        self.btn_min = QPushButton("-")
        self.btn_min.setObjectName('minButton')
        self.btn_min.setFixedSize(btn_size, btn_size)

        self.btn_max = QPushButton("□")
        self.btn_max.setObjectName('maxButton')
        self.btn_max.setFixedSize(btn_size, btn_size)

        self.title.setFixedHeight(30)
        self.title.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.btn_min)
        self.layout.addWidget(self.btn_max)
        self.layout.addWidget(self.btn_close)

        self.setLayout(self.layout)

        self.start = QPoint(0, 0)
        self.pressing = False

    def resizeEvent(self, QResizeEvent):
        super(CustomBar, self).resizeEvent(QResizeEvent)
        self.title.setFixedWidth(self.parent.width())

    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end-self.start
            self.parent.setGeometry(self.mapToGlobal(self.movement).x(),
                                self.mapToGlobal(self.movement).y(),
                                self.parent.width(),
                                self.parent.height())
            self.start = self.end

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False