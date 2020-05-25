# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'container.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Camera(object):
    def setupUi(self, Camera):
        if not Camera.objectName():
            Camera.setObjectName(u"Camera")
        Camera.resize(573, 529)
        font = QFont()
        font.setPointSize(9)
        Camera.setFont(font)
        self.gridLayout = QGridLayout(Camera)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(Camera)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.camera_page = QWidget()
        self.camera_page.setObjectName(u"camera_page")
        self.verticalLayout_3 = QVBoxLayout(self.camera_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_camera = QVBoxLayout()
        self.verticalLayout_camera.setObjectName(u"verticalLayout_camera")

        self.verticalLayout_3.addLayout(self.verticalLayout_camera)

        self.stackedWidget.addWidget(self.camera_page)
        self.database_page = QWidget()
        self.database_page.setObjectName(u"database_page")
        self.verticalLayout = QVBoxLayout(self.database_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_db_btn = QHBoxLayout()
        self.horizontalLayout_db_btn.setObjectName(u"horizontalLayout_db_btn")
        self.remove_btn = QToolButton(self.database_page)
        self.remove_btn.setObjectName(u"remove_btn")
        self.remove_btn.setMinimumSize(QSize(80, 30))
        self.remove_btn.setMaximumSize(QSize(80, 30))

        self.horizontalLayout_db_btn.addWidget(self.remove_btn)

        self.add_btn = QToolButton(self.database_page)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setMinimumSize(QSize(80, 30))
        self.add_btn.setMaximumSize(QSize(80, 30))

        self.horizontalLayout_db_btn.addWidget(self.add_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_db_btn.addItem(self.horizontalSpacer)

        self.search = QLineEdit(self.database_page)
        self.search.setObjectName(u"search")
        self.search.setMinimumSize(QSize(200, 30))
        self.search.setMaximumSize(QSize(200, 30))
        self.search.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_db_btn.addWidget(self.search)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_db_btn.addItem(self.horizontalSpacer_2)

        self.db_status = QLabel(self.database_page)
        self.db_status.setObjectName(u"db_status")

        self.horizontalLayout_db_btn.addWidget(self.db_status)


        self.verticalLayout.addLayout(self.horizontalLayout_db_btn)

        self.tableWidget = QTableWidget(self.database_page)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)

        self.stackedWidget.addWidget(self.database_page)
        self.about_page = QWidget()
        self.about_page.setObjectName(u"about_page")
        self.gridLayout_2 = QGridLayout(self.about_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_about = QVBoxLayout()
        self.verticalLayout_about.setObjectName(u"verticalLayout_about")
        self.label_img = QLabel(self.about_page)
        self.label_img.setObjectName(u"label_img")

        self.verticalLayout_about.addWidget(self.label_img)

        self.textEdit = QTextEdit(self.about_page)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_about.addWidget(self.textEdit)


        self.gridLayout_2.addLayout(self.verticalLayout_about, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.about_page)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.retranslateUi(Camera)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Camera)
    # setupUi

    def retranslateUi(self, Camera):
        Camera.setWindowTitle(QCoreApplication.translate("Camera", u"Form", None))
        self.remove_btn.setText(QCoreApplication.translate("Camera", u"Remove", None))
        self.add_btn.setText(QCoreApplication.translate("Camera", u"Add", None))
        self.search.setPlaceholderText(QCoreApplication.translate("Camera", u"Search", None))
        self.db_status.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Camera", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Camera", u"Full name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Camera", u"Devices", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Camera", u"Problem", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Camera", u"Date", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Camera", u"Time", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Camera", u"Prix", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Camera", u"Status", None));
        self.label_img.setText("")
        self.textEdit.setHtml(QCoreApplication.translate("Camera", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<h1 align=\"center\" style=\" margin-top:78px; margin-bottom:-11px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:112%;\"><a name=\"cc05\"></a><span style=\" font-family:'medium-content-sans-serif-font','Lucida Grande','Lucida Sans Unicode','Lucida Sans','Geneva','Arial','sans-serif'; font-size:xx-large; font-weight:600; text-decoration: underline; color:#009688;\">W</span><span style=\" font-family:'medium-content-sans-serif-font','Lucida Grande','Lucida Sans Unicode','Lucida Sans','Geneva','Arial','sans-serif'; font-size:xx-large; font-weight:600; text-decoration: underline; color:#009688;\">hat is PySide</span></h1>\n"
"<p align=\"cent"
                        "er\" style=\" margin-top:21px; margin-bottom:-11px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:32px; background-color:#263238;\"><a name=\"9014\"></a><span style=\" font-family:'medium-content-serif-font','Georgia','Cambria','Times New Roman','Times','serif'; font-size:21px; color:#f5f5f5; background-color:#263238;\">P</span><span style=\" font-family:'medium-content-serif-font','Georgia','Cambria','Times New Roman','Times','serif'; font-size:21px; color:#f5f5f5; background-color:#263238;\">ySide is a Python binding of the cross-platform GUI development toolkit Qt, currently developed by the Qt company under the</span><span style=\" font-family:'medium-content-serif-font','Georgia','Cambria','Times New Roman','Times','serif'; font-size:21px; color:rgba(0,0,0,0.839216);\"> </span><span style=\" font-family:'medium-content-serif-font','Georgia','Cambria','Times New Roman','Times','serif'; font-size:21px; font-weight:696; color:#fb8c00;\">Qt for Python</span><span style=\""
                        " font-family:'medium-content-serif-font','Georgia','Cambria','Times New Roman','Times','serif'; font-size:21px; color:rgba(0,0,0,0.839216);\"> </span><span style=\" font-family:'medium-content-serif-font','Georgia','Cambria','Times New Roman','Times','serif'; font-size:21px; color:#f5f5f5;\">Project. Pyside provides LGPL-licensed Python bindings for the</span><span style=\" font-family:'medium-content-serif-font','Georgia','Cambria','Times New Roman','Times','serif'; font-size:21px; color:rgba(0,0,0,0.839216);\"> </span><span style=\" font-family:'medium-content-serif-font','Georgia','Cambria','Times New Roman','Times','serif'; font-size:21px; font-weight:696; color:#4caf50;\">Qt 5</span><span style=\" font-family:'medium-content-serif-font','Georgia','Cambria','Times New Roman','Times','serif'; font-size:21px; color:rgba(0,0,0,0.839216);\">. </span><span style=\" font-family:'medium-content-serif-font','Georgia','Cambria','Times New Roman','Times','serif'; font-size:21px; color:#f5f5f5;\">It also includes com"
                        "plete toolchain for rapidly generating bindings for any Qt-based C++ class hierarchies. PySide</span><span style=\" font-family:'medium-content-serif-font','Georgia','Cambria','Times New Roman','Times','serif'; font-size:21px; color:rgba(0,0,0,0.839216);\"> </span><span style=\" font-family:'medium-content-serif-font','Georgia','Cambria','Times New Roman','Times','serif'; font-size:21px; color:#f5f5f5;\">Qt bindings allow both free open source and proprietary software development and ultimately aim to support Qt platforms. Pyside is a really useful framework used for developing cool looking Graphical User Interfaces easily for your python applications. We</span><span style=\" font-family:'medium-content-serif-font','Georgia','Cambria','Times New Roman','Times','serif'; font-size:21px; color:rgba(0,0,0,0.839216);\"> </span><span style=\" font-family:'medium-content-serif-font','Georgia','Cambria','Times New Roman','Times','serif'; font-size:21px; color:#f5f5f5;\">would be using</span><span style=\" font-family:"
                        "'medium-content-serif-font','Georgia','Cambria','Times New Roman','Times','serif'; font-size:21px; color:rgba(0,0,0,0.839216);\"> </span><span style=\" font-family:'medium-content-serif-font','Georgia','Cambria','Times New Roman','Times','serif'; font-size:21px; font-weight:696; color:#039be5;\">Pyside2</span><span style=\" font-family:'medium-content-serif-font','Georgia','Cambria','Times New Roman','Times','serif'; font-size:21px; color:#f5f5f5;\">, the latest version of Pyside.</span></p></body></html>", None))
    # retranslateUi

