from PySide2.QtCore import QSize
from PySide2.QtWidgets import QWidget, QVBoxLayout, QLabel, QToolButton
from PySide2.QtGui import QPixmap, QColor, Qt
import iconify as ico


class SideBar(QWidget):

    def __init__(self):
        super(SideBar, self).__init__()
        # read StyleSheet
        with open('QSS/sideBar.qss', 'r') as f:
            self.setStyleSheet(f.read())
            f.close()
        # Vertical Layout
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setContentsMargins(0,0,0,0)

        # Icons
        camera_icon = ico.Icon('font-awesome:solid:camera-retro', QColor('#E91E63'))
        database_icon = ico.Icon('font-awesome:solid:database', QColor('#03A9F4'))
        about_icon = ico.Icon('font-awesome:solid:exclamation-triangle', QColor('#FDD835'))

        # logo image
        logo = QLabel()
        logo.setFixedSize(110,110)
        logo_img = QPixmap('resources/qt.png')
        logo.setPixmap(logo_img)
        logo.setContentsMargins(20,20,20,20)

        # bottom label like spacer
        bottom_label = QLabel()

        # Create Buttons
        btn_width = 110
        btn_height = 40

        self.Camera = QToolButton()
        self.Camera.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.Camera.setObjectName('Camera_btn')
        self.Camera.setText(' Camera')
        self.Camera.setFixedSize(btn_width, btn_height)
        self.Camera.setIcon(camera_icon)
        self.Camera.setIconSize(QSize(20,20))

        self.DataBase = QToolButton()
        self.DataBase.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.DataBase.setObjectName('customers_btn')
        self.DataBase.setText(' DataBase')
        self.DataBase.setFixedSize(btn_width, btn_height)
        self.DataBase.setIcon(database_icon)
        self.DataBase.setIconSize(QSize(20,20))

        self.About = QToolButton()
        self.About.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.About.setObjectName('About_btn')
        self.About.setText(' About')
        self.About.setFixedSize(btn_width, btn_height)
        self.About.setIcon(about_icon)
        self.About.setIconSize(QSize(20,20))

        # add widget
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.addWidget(logo)
        self.verticalLayout.addWidget(self.Camera)
        self.verticalLayout.addWidget(self.DataBase)
        self.verticalLayout.addWidget(self.About)
        self.verticalLayout.addWidget(bottom_label)
        self.setLayout(self.verticalLayout)
