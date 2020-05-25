import sys

from PySide2.QtCore import Qt
from PySide2.QtGui import QColor
from PySide2.QtWidgets import (QApplication, QHBoxLayout, QVBoxLayout,
                               QWidget, QMainWindow, QFrame, QLabel)

from components.customTitleBar import CustomBar
from components.sideBar import SideBar
from components.container import pagesWidget

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        # include components
        self.titleBar = CustomBar(self)
        self.sidBar = SideBar()
        self.container = pagesWidget()

        # line Decoration
        line1 = QFrame()
        line1.setStyleSheet("background-color: #FFB300;")
        line1.setObjectName("Vline")
        line1.setMinimumHeight(2)

        # Main window layout
        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(0,0,0,0)
        mainLayout.setSpacing(0)

        # custom bar layout
        TitleBarLayout = QVBoxLayout()
        TitleBarLayout.setContentsMargins(0,0,0,0)
        TitleBarLayout.addWidget(self.titleBar)
        TitleBarLayout.addWidget(line1)
        mainLayout.addLayout(TitleBarLayout)

        BodyContentLayout = QHBoxLayout()
        BodyContentLayout.addWidget(self.sidBar)
        BodyContentLayout.addWidget(self.container)
        BodyContentLayout.setContentsMargins(0,0,0,0)
        mainLayout.addLayout(BodyContentLayout)

        # Set Minimum size of window
        self.setMinimumSize(700, 500)

        # Get Frame less window
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.CustomizeWindowHint)

        # Create Widget to add Layout
        widget = QWidget()
        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)

        # Database Status
        label_db = QLabel()
        self.container.db_status.setText("No Database Connection!")
        self.container.horizontalLayout_db_btn.addWidget(label_db)

        # Buttons Clicked Signal
        self.titleBar.btn_close.clicked.connect(self.close)
        self.titleBar.btn_max.clicked.connect(self.windowResize)
        self.titleBar.btn_min.clicked.connect(self.showMinimized)
        self.sidBar.DataBase.clicked.connect(self.setCustomersPage)
        self.sidBar.About.clicked.connect(self.setAboutPage)

    def setAboutPage(self):
        self.container.stackedWidget.setCurrentIndex(2)

    def setCustomersPage(self):
        self.container.stackedWidget.setCurrentIndex(1)

    def windowResize(self):
        if not self.isMaximized():
            self.setWindowState(Qt.WindowMaximized)
        else:
            self.setWindowState(Qt.WindowNoState)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
