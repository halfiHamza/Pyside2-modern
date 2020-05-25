from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel
from PySide2.QtCore import Qt

from components.container_ui import Ui_Camera
from webcame import Camera

class pagesWidget(QWidget, Ui_Camera):
    def __init__(self):
        super(pagesWidget, self).__init__()
        self.setupUi(self)

        # container margins
        self.gridLayout.setContentsMargins(0,0,0,0)

        # read styleSheet
        with open('./QSS/container.qss', 'r', encoding='utf-8') as f:
            self.setStyleSheet(f.read())
            f.close()

        # set default page
        self.stackedWidget.setCurrentIndex(0)

        # set label image
        self.label_img.setScaledContents(True)
        img = QPixmap('./resources/qt+pyside2.jpeg')
        self.label_img.setPixmap(img)
        self.label_img.setMaximumSize(300,100)

        label = QLabel(self.camera_page)
        label.setText('test')
        label.setStyleSheet("color:white; border:1px solid red;")
        label.setAlignment(Qt.AlignCenter)
        self.verticalLayout_camera.addWidget(label)

