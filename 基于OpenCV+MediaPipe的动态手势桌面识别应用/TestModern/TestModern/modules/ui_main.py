# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QTextEdit,
    QVBoxLayout, QWidget)
from .resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(940, 560)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_new = QPushButton(self.topMenu)
        self.btn_new.setObjectName(u"btn_new")
        sizePolicy.setHeightForWidth(self.btn_new.sizePolicy().hasHeightForWidth())
        self.btn_new.setSizePolicy(sizePolicy)
        self.btn_new.setMinimumSize(QSize(0, 45))
        self.btn_new.setFont(font)
        self.btn_new.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new.setLayoutDirection(Qt.LeftToRight)
        self.btn_new.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-hand-point-right.png);")

        self.verticalLayout_8.addWidget(self.btn_new)

        self.btn_new_2 = QPushButton(self.topMenu)
        self.btn_new_2.setObjectName(u"btn_new_2")
        sizePolicy.setHeightForWidth(self.btn_new_2.sizePolicy().hasHeightForWidth())
        self.btn_new_2.setSizePolicy(sizePolicy)
        self.btn_new_2.setMinimumSize(QSize(0, 45))
        self.btn_new_2.setFont(font)
        self.btn_new_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new_2.setLayoutDirection(Qt.LeftToRight)
        self.btn_new_2.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-align-left.png);")

        self.verticalLayout_8.addWidget(self.btn_new_2)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-people.png)")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_user = QPushButton(self.extraTopMenu)
        self.btn_user.setObjectName(u"btn_user")
        sizePolicy.setHeightForWidth(self.btn_user.sizePolicy().hasHeightForWidth())
        self.btn_user.setSizePolicy(sizePolicy)
        self.btn_user.setMinimumSize(QSize(0, 45))
        self.btn_user.setFont(font)
        self.btn_user.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_user.setLayoutDirection(Qt.LeftToRight)
        self.btn_user.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-voice-over-record.png);")

        self.verticalLayout_11.addWidget(self.btn_user)

        self.btn_re_password = QPushButton(self.extraTopMenu)
        self.btn_re_password.setObjectName(u"btn_re_password")
        sizePolicy.setHeightForWidth(self.btn_re_password.sizePolicy().hasHeightForWidth())
        self.btn_re_password.setSizePolicy(sizePolicy)
        self.btn_re_password.setMinimumSize(QSize(0, 45))
        self.btn_re_password.setFont(font)
        self.btn_re_password.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_re_password.setLayoutDirection(Qt.LeftToRight)
        self.btn_re_password.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-dialpad.png);")

        self.verticalLayout_11.addWidget(self.btn_re_password)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_nameshowTitle = QLabel(self.leftBox)
        self.label_nameshowTitle.setObjectName(u"label_nameshowTitle")
        self.label_nameshowTitle.setStyleSheet(u"font-size: 20px;font-weight: bold;")
        self.label_nameshowTitle.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_nameshowTitle, 0, 0, 1, 1)

        self.label_nameshow = QLabel(self.leftBox)
        self.label_nameshow.setObjectName(u"label_nameshow")
        self.label_nameshow.setStyleSheet(u"font-size: 20px;font-weight: bold;")

        self.gridLayout_9.addWidget(self.label_nameshow, 0, 1, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout_9)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"background-image: url(:/images/images/images/PyDracula_vertical.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.stackedWidget.addWidget(self.home)
        self.new_page = QWidget()
        self.new_page.setObjectName(u"new_page")
        self.verticalLayout_20 = QVBoxLayout(self.new_page)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.stackedWidget.addWidget(self.new_page)
        self.help_page = QWidget()
        self.help_page.setObjectName(u"help_page")
        self.verticalLayout = QVBoxLayout(self.help_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.lineEdit_title = QLineEdit(self.help_page)
        self.lineEdit_title.setObjectName(u"lineEdit_title")
        self.lineEdit_title.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_title.setReadOnly(False)

        self.gridLayout_7.addWidget(self.lineEdit_title, 3, 1, 1, 1)

        self.head_label_2 = QLabel(self.help_page)
        self.head_label_2.setObjectName(u"head_label_2")
        self.head_label_2.setMaximumSize(QSize(16777215, 150))
        self.head_label_2.setLayoutDirection(Qt.LeftToRight)
        self.head_label_2.setStyleSheet(u"image: url(:/images/images/images/PyDracula_vertical.png);")

        self.gridLayout_7.addWidget(self.head_label_2, 1, 1, 1, 1)

        self.set_call_email = QLabel(self.help_page)
        self.set_call_email.setObjectName(u"set_call_email")
        self.set_call_email.setTextFormat(Qt.AutoText)
        self.set_call_email.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.set_call_email, 5, 0, 1, 1)

        self.lineEdit_call_email = QLineEdit(self.help_page)
        self.lineEdit_call_email.setObjectName(u"lineEdit_call_email")
        self.lineEdit_call_email.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_7.addWidget(self.lineEdit_call_email, 5, 1, 1, 1)

        self.lineEdit_content = QLineEdit(self.help_page)
        self.lineEdit_content.setObjectName(u"lineEdit_content")
        self.lineEdit_content.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_7.addWidget(self.lineEdit_content, 4, 1, 1, 1)

        self.set_content = QLabel(self.help_page)
        self.set_content.setObjectName(u"set_content")
        self.set_content.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.set_content, 4, 0, 1, 1)

        self.set_title = QLabel(self.help_page)
        self.set_title.setObjectName(u"set_title")
        self.set_title.setFont(font)
        self.set_title.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.set_title, 3, 0, 1, 1)

        self.btn_save_feedback = QPushButton(self.help_page)
        self.btn_save_feedback.setObjectName(u"btn_save_feedback")
        self.btn_save_feedback.setMaximumSize(QSize(100, 16777215))
        self.btn_save_feedback.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_7.addWidget(self.btn_save_feedback, 6, 1, 1, 1)

        self.label_17 = QLabel(self.help_page)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"font-size: 40px;font-weight: bold;")

        self.gridLayout_7.addWidget(self.label_17, 2, 0, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout_7)

        self.stackedWidget.addWidget(self.help_page)
        self.administrators_page = QWidget()
        self.administrators_page.setObjectName(u"administrators_page")
        self.verticalLayout_17 = QVBoxLayout(self.administrators_page)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.stackedWidget.addWidget(self.administrators_page)
        self.set_page = QWidget()
        self.set_page.setObjectName(u"set_page")
        self.verticalLayout_21 = QVBoxLayout(self.set_page)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_3 = QLabel(self.set_page)
        self.label_3.setObjectName(u"label_3")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setBold(True)
        font4.setItalic(False)
        font4.setUnderline(False)
        font4.setStrikeOut(False)
        self.label_3.setFont(font4)
        self.label_3.setAcceptDrops(False)
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setStyleSheet(u"font-size: 20px;font-weight: bold;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_3)

        self.label_4 = QLabel(self.set_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font-size: 20px;font-weight: bold;")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_4)


        self.verticalLayout_22.addLayout(self.horizontalLayout_7)

        self.gridLayout_100 = QGridLayout()
        self.gridLayout_100.setObjectName(u"gridLayout_100")
        self.comboBox_101 = QComboBox(self.set_page)
        self.comboBox_101.addItem("")
        self.comboBox_101.addItem("")
        self.comboBox_101.addItem("")
        self.comboBox_101.addItem("")
        self.comboBox_101.addItem("")
        self.comboBox_101.addItem("")
        self.comboBox_101.addItem("")
        self.comboBox_101.addItem("")
        self.comboBox_101.addItem("")
        self.comboBox_101.addItem("")
        self.comboBox_101.addItem("")
        self.comboBox_101.addItem("")
        self.comboBox_101.addItem("")
        self.comboBox_101.addItem("")
        self.comboBox_101.addItem("")
        self.comboBox_101.addItem("")
        self.comboBox_101.addItem("")
        self.comboBox_101.addItem("")
        self.comboBox_101.addItem("")
        self.comboBox_101.addItem("")
        self.comboBox_101.addItem("")
        self.comboBox_101.setObjectName(u"comboBox_101")

        self.gridLayout_100.addWidget(self.comboBox_101, 1, 0, 1, 1)

        self.label_111 = QLabel(self.set_page)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setFont(font)

        self.gridLayout_100.addWidget(self.label_111, 0, 0, 1, 1)

        self.comboBox_102 = QComboBox(self.set_page)
        self.comboBox_102.addItem("")
        self.comboBox_102.addItem("")
        self.comboBox_102.addItem("")
        self.comboBox_102.addItem("")
        self.comboBox_102.addItem("")
        self.comboBox_102.addItem("")
        self.comboBox_102.addItem("")
        self.comboBox_102.addItem("")
        self.comboBox_102.addItem("")
        self.comboBox_102.addItem("")
        self.comboBox_102.addItem("")
        self.comboBox_102.addItem("")
        self.comboBox_102.addItem("")
        self.comboBox_102.addItem("")
        self.comboBox_102.addItem("")
        self.comboBox_102.addItem("")
        self.comboBox_102.addItem("")
        self.comboBox_102.addItem("")
        self.comboBox_102.addItem("")
        self.comboBox_102.addItem("")
        self.comboBox_102.addItem("")
        self.comboBox_102.setObjectName(u"comboBox_102")

        self.gridLayout_100.addWidget(self.comboBox_102, 1, 1, 1, 1)


        self.verticalLayout_22.addLayout(self.gridLayout_100)

        self.gridLayout_200 = QGridLayout()
        self.gridLayout_200.setObjectName(u"gridLayout_200")
        self.label_222 = QLabel(self.set_page)
        self.label_222.setObjectName(u"label_222")
        self.label_222.setFont(font)

        self.gridLayout_200.addWidget(self.label_222, 0, 0, 1, 1)

        self.comboBox_201 = QComboBox(self.set_page)
        self.comboBox_201.addItem("")
        self.comboBox_201.addItem("")
        self.comboBox_201.addItem("")
        self.comboBox_201.addItem("")
        self.comboBox_201.addItem("")
        self.comboBox_201.addItem("")
        self.comboBox_201.addItem("")
        self.comboBox_201.addItem("")
        self.comboBox_201.addItem("")
        self.comboBox_201.addItem("")
        self.comboBox_201.addItem("")
        self.comboBox_201.addItem("")
        self.comboBox_201.addItem("")
        self.comboBox_201.addItem("")
        self.comboBox_201.addItem("")
        self.comboBox_201.addItem("")
        self.comboBox_201.addItem("")
        self.comboBox_201.addItem("")
        self.comboBox_201.addItem("")
        self.comboBox_201.addItem("")
        self.comboBox_201.addItem("")
        self.comboBox_201.setObjectName(u"comboBox_201")

        self.gridLayout_200.addWidget(self.comboBox_201, 1, 0, 1, 1)

        self.comboBox_202 = QComboBox(self.set_page)
        self.comboBox_202.addItem("")
        self.comboBox_202.addItem("")
        self.comboBox_202.addItem("")
        self.comboBox_202.addItem("")
        self.comboBox_202.addItem("")
        self.comboBox_202.addItem("")
        self.comboBox_202.addItem("")
        self.comboBox_202.addItem("")
        self.comboBox_202.addItem("")
        self.comboBox_202.addItem("")
        self.comboBox_202.addItem("")
        self.comboBox_202.addItem("")
        self.comboBox_202.addItem("")
        self.comboBox_202.addItem("")
        self.comboBox_202.addItem("")
        self.comboBox_202.addItem("")
        self.comboBox_202.addItem("")
        self.comboBox_202.addItem("")
        self.comboBox_202.addItem("")
        self.comboBox_202.addItem("")
        self.comboBox_202.addItem("")
        self.comboBox_202.setObjectName(u"comboBox_202")

        self.gridLayout_200.addWidget(self.comboBox_202, 1, 1, 1, 1)


        self.verticalLayout_22.addLayout(self.gridLayout_200)

        self.gridLayout_300 = QGridLayout()
        self.gridLayout_300.setObjectName(u"gridLayout_300")
        self.label_333 = QLabel(self.set_page)
        self.label_333.setObjectName(u"label_333")
        self.label_333.setFont(font)

        self.gridLayout_300.addWidget(self.label_333, 0, 0, 1, 1)

        self.comboBox_301 = QComboBox(self.set_page)
        self.comboBox_301.addItem("")
        self.comboBox_301.addItem("")
        self.comboBox_301.addItem("")
        self.comboBox_301.addItem("")
        self.comboBox_301.addItem("")
        self.comboBox_301.addItem("")
        self.comboBox_301.addItem("")
        self.comboBox_301.addItem("")
        self.comboBox_301.addItem("")
        self.comboBox_301.addItem("")
        self.comboBox_301.addItem("")
        self.comboBox_301.addItem("")
        self.comboBox_301.addItem("")
        self.comboBox_301.addItem("")
        self.comboBox_301.addItem("")
        self.comboBox_301.addItem("")
        self.comboBox_301.addItem("")
        self.comboBox_301.addItem("")
        self.comboBox_301.addItem("")
        self.comboBox_301.addItem("")
        self.comboBox_301.addItem("")
        self.comboBox_301.setObjectName(u"comboBox_301")

        self.gridLayout_300.addWidget(self.comboBox_301, 1, 0, 1, 1)

        self.comboBox_302 = QComboBox(self.set_page)
        self.comboBox_302.addItem("")
        self.comboBox_302.addItem("")
        self.comboBox_302.addItem("")
        self.comboBox_302.addItem("")
        self.comboBox_302.addItem("")
        self.comboBox_302.addItem("")
        self.comboBox_302.addItem("")
        self.comboBox_302.addItem("")
        self.comboBox_302.addItem("")
        self.comboBox_302.addItem("")
        self.comboBox_302.addItem("")
        self.comboBox_302.addItem("")
        self.comboBox_302.addItem("")
        self.comboBox_302.addItem("")
        self.comboBox_302.addItem("")
        self.comboBox_302.addItem("")
        self.comboBox_302.addItem("")
        self.comboBox_302.addItem("")
        self.comboBox_302.addItem("")
        self.comboBox_302.addItem("")
        self.comboBox_302.addItem("")
        self.comboBox_302.setObjectName(u"comboBox_302")

        self.gridLayout_300.addWidget(self.comboBox_302, 1, 1, 1, 1)


        self.verticalLayout_22.addLayout(self.gridLayout_300)

        self.gridLayout_400 = QGridLayout()
        self.gridLayout_400.setObjectName(u"gridLayout_400")
        self.label_444 = QLabel(self.set_page)
        self.label_444.setObjectName(u"label_444")
        self.label_444.setFont(font)

        self.gridLayout_400.addWidget(self.label_444, 0, 0, 1, 1)

        self.comboBox_402 = QComboBox(self.set_page)
        self.comboBox_402.addItem("")
        self.comboBox_402.addItem("")
        self.comboBox_402.addItem("")
        self.comboBox_402.addItem("")
        self.comboBox_402.addItem("")
        self.comboBox_402.addItem("")
        self.comboBox_402.addItem("")
        self.comboBox_402.addItem("")
        self.comboBox_402.addItem("")
        self.comboBox_402.addItem("")
        self.comboBox_402.addItem("")
        self.comboBox_402.addItem("")
        self.comboBox_402.addItem("")
        self.comboBox_402.addItem("")
        self.comboBox_402.addItem("")
        self.comboBox_402.addItem("")
        self.comboBox_402.addItem("")
        self.comboBox_402.addItem("")
        self.comboBox_402.addItem("")
        self.comboBox_402.addItem("")
        self.comboBox_402.addItem("")
        self.comboBox_402.setObjectName(u"comboBox_402")

        self.gridLayout_400.addWidget(self.comboBox_402, 1, 1, 1, 1)

        self.comboBox_401 = QComboBox(self.set_page)
        self.comboBox_401.addItem("")
        self.comboBox_401.addItem("")
        self.comboBox_401.addItem("")
        self.comboBox_401.addItem("")
        self.comboBox_401.addItem("")
        self.comboBox_401.addItem("")
        self.comboBox_401.addItem("")
        self.comboBox_401.addItem("")
        self.comboBox_401.addItem("")
        self.comboBox_401.addItem("")
        self.comboBox_401.addItem("")
        self.comboBox_401.addItem("")
        self.comboBox_401.addItem("")
        self.comboBox_401.addItem("")
        self.comboBox_401.addItem("")
        self.comboBox_401.addItem("")
        self.comboBox_401.addItem("")
        self.comboBox_401.addItem("")
        self.comboBox_401.addItem("")
        self.comboBox_401.addItem("")
        self.comboBox_401.addItem("")
        self.comboBox_401.setObjectName(u"comboBox_401")

        self.gridLayout_400.addWidget(self.comboBox_401, 1, 0, 1, 1)


        self.verticalLayout_22.addLayout(self.gridLayout_400)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_saveSet = QPushButton(self.set_page)
        self.pushButton_saveSet.setObjectName(u"pushButton_saveSet")

        self.horizontalLayout_6.addWidget(self.pushButton_saveSet)

        self.pushButton_default = QPushButton(self.set_page)
        self.pushButton_default.setObjectName(u"pushButton_default")

        self.horizontalLayout_6.addWidget(self.pushButton_default)


        self.verticalLayout_22.addLayout(self.horizontalLayout_6)


        self.gridLayout_3.addLayout(self.verticalLayout_22, 0, 0, 1, 1)

        self.label_2 = QLabel(self.set_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"image: url(:/images/images/images/handsPort.png);")
        self.label_2.setScaledContents(True)

        self.gridLayout_3.addWidget(self.label_2, 0, 2, 1, 1)

        self.label_5 = QLabel(self.set_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 0))
        self.label_5.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_3.addWidget(self.label_5, 0, 1, 1, 1)


        self.verticalLayout_21.addLayout(self.gridLayout_3)

        self.stackedWidget.addWidget(self.set_page)
        self.user_page = QWidget()
        self.user_page.setObjectName(u"user_page")
        self.gridLayout_2 = QGridLayout(self.user_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_phone = QLineEdit(self.user_page)
        self.lineEdit_phone.setObjectName(u"lineEdit_phone")
        self.lineEdit_phone.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.lineEdit_phone, 3, 1, 1, 1)

        self.btn_save_user = QPushButton(self.user_page)
        self.btn_save_user.setObjectName(u"btn_save_user")
        self.btn_save_user.setMaximumSize(QSize(100, 16777215))
        self.btn_save_user.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.btn_save_user, 5, 1, 1, 1)

        self.lineEdit_username = QLineEdit(self.user_page)
        self.lineEdit_username.setObjectName(u"lineEdit_username")
        self.lineEdit_username.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_username.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_username, 2, 1, 1, 1)

        self.set_phone = QLabel(self.user_page)
        self.set_phone.setObjectName(u"set_phone")
        self.set_phone.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.set_phone, 3, 0, 1, 1)

        self.lineEdit_email = QLineEdit(self.user_page)
        self.lineEdit_email.setObjectName(u"lineEdit_email")
        self.lineEdit_email.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.lineEdit_email, 4, 1, 1, 1)

        self.set_username = QLabel(self.user_page)
        self.set_username.setObjectName(u"set_username")
        self.set_username.setFont(font)
        self.set_username.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.set_username, 2, 0, 1, 1)

        self.set_email = QLabel(self.user_page)
        self.set_email.setObjectName(u"set_email")
        self.set_email.setTextFormat(Qt.AutoText)
        self.set_email.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.set_email, 4, 0, 1, 1)

        self.head_label = QLabel(self.user_page)
        self.head_label.setObjectName(u"head_label")
        self.head_label.setMaximumSize(QSize(16777215, 150))
        self.head_label.setLayoutDirection(Qt.LeftToRight)
        self.head_label.setStyleSheet(u"image: url(:/images/images/images/PyDracula_vertical.png);")

        self.gridLayout.addWidget(self.head_label, 1, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)

        self.label_11 = QLabel(self.user_page)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 0, 0, 1, 1)

        self.label_12 = QLabel(self.user_page)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 0, 2, 1, 1)

        self.stackedWidget.addWidget(self.user_page)
        self.we_page = QWidget()
        self.we_page.setObjectName(u"we_page")
        self.gridLayout_8 = QGridLayout(self.we_page)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_14 = QLabel(self.we_page)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_6.addWidget(self.label_14, 1, 0, 1, 1)

        self.label_13 = QLabel(self.we_page)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"font-size:30px;font-weight: bold;")

        self.gridLayout_6.addWidget(self.label_13, 0, 0, 1, 1)

        self.label_15 = QLabel(self.we_page)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"font-size: 30px;font-weight: bold;")

        self.gridLayout_6.addWidget(self.label_15, 2, 0, 1, 1)

        self.label_16 = QLabel(self.we_page)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_6.addWidget(self.label_16, 3, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_6, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.we_page)
        self.re_password_page = QWidget()
        self.re_password_page.setObjectName(u"re_password_page")
        self.gridLayout_5 = QGridLayout(self.re_password_page)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_9 = QLabel(self.re_password_page)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_5.addWidget(self.label_9, 0, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_8 = QLabel(self.re_password_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_8, 4, 0, 1, 1)

        self.lineEdit_re_oldpw = QLineEdit(self.re_password_page)
        self.lineEdit_re_oldpw.setObjectName(u"lineEdit_re_oldpw")
        self.lineEdit_re_oldpw.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_re_oldpw.setEchoMode(QLineEdit.Password)

        self.gridLayout_4.addWidget(self.lineEdit_re_oldpw, 2, 1, 1, 1)

        self.lineEdit_re_username = QLineEdit(self.re_password_page)
        self.lineEdit_re_username.setObjectName(u"lineEdit_re_username")
        self.lineEdit_re_username.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_re_username.setEchoMode(QLineEdit.Normal)
        self.lineEdit_re_username.setReadOnly(True)

        self.gridLayout_4.addWidget(self.lineEdit_re_username, 1, 1, 1, 1)

        self.re_save = QPushButton(self.re_password_page)
        self.re_save.setObjectName(u"re_save")
        self.re_save.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_4.addWidget(self.re_save, 5, 1, 1, 1)

        self.label_6 = QLabel(self.re_password_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_6, 2, 0, 1, 1)

        self.lineEdit_re_newpw = QLineEdit(self.re_password_page)
        self.lineEdit_re_newpw.setObjectName(u"lineEdit_re_newpw")
        self.lineEdit_re_newpw.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_re_newpw.setEchoMode(QLineEdit.Password)

        self.gridLayout_4.addWidget(self.lineEdit_re_newpw, 3, 1, 1, 1)

        self.label = QLabel(self.re_password_page)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 1)

        self.label_7 = QLabel(self.re_password_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_7, 3, 0, 1, 1)

        self.lineEdit_re_snewpw = QLineEdit(self.re_password_page)
        self.lineEdit_re_snewpw.setObjectName(u"lineEdit_re_snewpw")
        self.lineEdit_re_snewpw.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_re_snewpw.setEchoMode(QLineEdit.Password)

        self.gridLayout_4.addWidget(self.lineEdit_re_snewpw, 4, 1, 1, 1)

        self.label_re_pw = QLabel(self.re_password_page)
        self.label_re_pw.setObjectName(u"label_re_pw")
        self.label_re_pw.setMaximumSize(QSize(16777215, 200))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setBold(False)
        font5.setItalic(False)
        self.label_re_pw.setFont(font5)
        self.label_re_pw.setStyleSheet(u"font-size: 30px;")
        self.label_re_pw.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_re_pw, 0, 1, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 1, 1, 1)

        self.label_10 = QLabel(self.re_password_page)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_5.addWidget(self.label_10, 0, 2, 1, 1)

        self.stackedWidget.addWidget(self.re_password_page)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-loop-circular.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_help_feedback = QPushButton(self.topMenus)
        self.btn_help_feedback.setObjectName(u"btn_help_feedback")
        sizePolicy.setHeightForWidth(self.btn_help_feedback.sizePolicy().hasHeightForWidth())
        self.btn_help_feedback.setSizePolicy(sizePolicy)
        self.btn_help_feedback.setMinimumSize(QSize(0, 45))
        self.btn_help_feedback.setFont(font)
        self.btn_help_feedback.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_help_feedback.setLayoutDirection(Qt.LeftToRight)
        self.btn_help_feedback.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-find-in-page.png);")

        self.verticalLayout_14.addWidget(self.btn_help_feedback)

        self.btn_we = QPushButton(self.topMenus)
        self.btn_we.setObjectName(u"btn_we")
        sizePolicy.setHeightForWidth(self.btn_we.sizePolicy().hasHeightForWidth())
        self.btn_we.setSizePolicy(sizePolicy)
        self.btn_we.setMinimumSize(QSize(0, 45))
        self.btn_we.setFont(font)
        self.btn_we.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_we.setLayoutDirection(Qt.LeftToRight)
        self.btn_we.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-mood-good.png);")

        self.verticalLayout_14.addWidget(self.btn_we)

        self.btn_administrators = QPushButton(self.topMenus)
        self.btn_administrators.setObjectName(u"btn_administrators")
        sizePolicy.setHeightForWidth(self.btn_administrators.sizePolicy().hasHeightForWidth())
        self.btn_administrators.setSizePolicy(sizePolicy)
        self.btn_administrators.setMinimumSize(QSize(0, 45))
        self.btn_administrators.setFont(font)
        self.btn_administrators.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_administrators.setLayoutDirection(Qt.LeftToRight)
        self.btn_administrators.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-people.png);")

        self.verticalLayout_14.addWidget(self.btn_administrators)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-level-up.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        self.creditsLabel.setFont(font5)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"\u624b\u52bf\u8bc6\u522b", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"\u57fa\u4e8eOpenCV\u6280\u672f", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"\u83dc\u5355", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"\u9996\u9875", None))
        self.btn_new.setText(QCoreApplication.translate("MainWindow", u"\u624b\u52bf\u753b\u9762", None))
        self.btn_new_2.setText(QCoreApplication.translate("MainWindow", u"\u624b\u52bf\u8bbe\u7f6e", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"\u4e2a\u4eba", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"\u4e2a\u4eba\u4fe1\u606f\u8bbe\u7f6e", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_user.setText(QCoreApplication.translate("MainWindow", u"\u4e2a\u4eba\u4fe1\u606f", None))
        self.btn_re_password.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u5bc6\u7801", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">\u624b\u52bf\u8bc6\u522b\u753b\u9762</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; marg"
                        "in-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">\u57fa\u4e8eOpenCV\u5e93\u7684\u8ba1\u7b97\u673a\u89c6\u89c9\u529f\u80fd</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">\u624b\u52bf\u8bc6\u522b\u8bad\u7ec3\u6570\u636e</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">\u5229\u7528mediapipe\u5e93\u6570\u636e\u8fdb\u884c\u8bc6\u522b\u5224\u65ad</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"\u624b\u52bf\u8bc6\u522b\u7684\u6280\u672f\u5e94\u7528", None))
        self.label_nameshowTitle.setText(QCoreApplication.translate("MainWindow", u"\u8d26\u53f7 \uff1a", None))
        self.label_nameshow.setText("")
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.head_label_2.setText("")
        self.set_call_email.setText(QCoreApplication.translate("MainWindow", u"\u8054\u7cfb\u90ae\u7bb1", None))
        self.set_content.setText(QCoreApplication.translate("MainWindow", u"\u5185\u5bb9", None))
        self.set_title.setText(QCoreApplication.translate("MainWindow", u"\u6807\u9898", None))
        self.btn_save_feedback.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u4ea4", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u5efa\u8bae\u6216\u53cd\u9988", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u89e6\u53d1\u53f71", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u89e6\u53d1\u53f72", None))
        self.comboBox_101.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.comboBox_101.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_101.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_101.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_101.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_101.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_101.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_101.setItemText(7, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_101.setItemText(8, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_101.setItemText(9, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_101.setItemText(10, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox_101.setItemText(11, QCoreApplication.translate("MainWindow", u"11", None))
        self.comboBox_101.setItemText(12, QCoreApplication.translate("MainWindow", u"12", None))
        self.comboBox_101.setItemText(13, QCoreApplication.translate("MainWindow", u"13", None))
        self.comboBox_101.setItemText(14, QCoreApplication.translate("MainWindow", u"14", None))
        self.comboBox_101.setItemText(15, QCoreApplication.translate("MainWindow", u"15", None))
        self.comboBox_101.setItemText(16, QCoreApplication.translate("MainWindow", u"16", None))
        self.comboBox_101.setItemText(17, QCoreApplication.translate("MainWindow", u"17", None))
        self.comboBox_101.setItemText(18, QCoreApplication.translate("MainWindow", u"18", None))
        self.comboBox_101.setItemText(19, QCoreApplication.translate("MainWindow", u"19", None))
        self.comboBox_101.setItemText(20, QCoreApplication.translate("MainWindow", u"20", None))

        self.label_111.setText(QCoreApplication.translate("MainWindow", u"\u529f\u80fd\u4e00\uff1a\u590d\u5236", None))
        self.comboBox_102.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.comboBox_102.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_102.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_102.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_102.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_102.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_102.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_102.setItemText(7, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_102.setItemText(8, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_102.setItemText(9, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_102.setItemText(10, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox_102.setItemText(11, QCoreApplication.translate("MainWindow", u"11", None))
        self.comboBox_102.setItemText(12, QCoreApplication.translate("MainWindow", u"12", None))
        self.comboBox_102.setItemText(13, QCoreApplication.translate("MainWindow", u"13", None))
        self.comboBox_102.setItemText(14, QCoreApplication.translate("MainWindow", u"14", None))
        self.comboBox_102.setItemText(15, QCoreApplication.translate("MainWindow", u"15", None))
        self.comboBox_102.setItemText(16, QCoreApplication.translate("MainWindow", u"16", None))
        self.comboBox_102.setItemText(17, QCoreApplication.translate("MainWindow", u"17", None))
        self.comboBox_102.setItemText(18, QCoreApplication.translate("MainWindow", u"18", None))
        self.comboBox_102.setItemText(19, QCoreApplication.translate("MainWindow", u"19", None))
        self.comboBox_102.setItemText(20, QCoreApplication.translate("MainWindow", u"20", None))

        self.label_222.setText(QCoreApplication.translate("MainWindow", u"\u529f\u80fd\u4e8c\uff1a\u7c98\u8d34", None))
        self.comboBox_201.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.comboBox_201.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_201.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_201.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_201.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_201.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_201.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_201.setItemText(7, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_201.setItemText(8, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_201.setItemText(9, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_201.setItemText(10, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox_201.setItemText(11, QCoreApplication.translate("MainWindow", u"11", None))
        self.comboBox_201.setItemText(12, QCoreApplication.translate("MainWindow", u"12", None))
        self.comboBox_201.setItemText(13, QCoreApplication.translate("MainWindow", u"13", None))
        self.comboBox_201.setItemText(14, QCoreApplication.translate("MainWindow", u"14", None))
        self.comboBox_201.setItemText(15, QCoreApplication.translate("MainWindow", u"15", None))
        self.comboBox_201.setItemText(16, QCoreApplication.translate("MainWindow", u"16", None))
        self.comboBox_201.setItemText(17, QCoreApplication.translate("MainWindow", u"17", None))
        self.comboBox_201.setItemText(18, QCoreApplication.translate("MainWindow", u"18", None))
        self.comboBox_201.setItemText(19, QCoreApplication.translate("MainWindow", u"19", None))
        self.comboBox_201.setItemText(20, QCoreApplication.translate("MainWindow", u"20", None))

        self.comboBox_202.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.comboBox_202.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_202.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_202.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_202.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_202.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_202.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_202.setItemText(7, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_202.setItemText(8, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_202.setItemText(9, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_202.setItemText(10, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox_202.setItemText(11, QCoreApplication.translate("MainWindow", u"11", None))
        self.comboBox_202.setItemText(12, QCoreApplication.translate("MainWindow", u"12", None))
        self.comboBox_202.setItemText(13, QCoreApplication.translate("MainWindow", u"13", None))
        self.comboBox_202.setItemText(14, QCoreApplication.translate("MainWindow", u"14", None))
        self.comboBox_202.setItemText(15, QCoreApplication.translate("MainWindow", u"15", None))
        self.comboBox_202.setItemText(16, QCoreApplication.translate("MainWindow", u"16", None))
        self.comboBox_202.setItemText(17, QCoreApplication.translate("MainWindow", u"17", None))
        self.comboBox_202.setItemText(18, QCoreApplication.translate("MainWindow", u"18", None))
        self.comboBox_202.setItemText(19, QCoreApplication.translate("MainWindow", u"19", None))
        self.comboBox_202.setItemText(20, QCoreApplication.translate("MainWindow", u"20", None))

        self.label_333.setText(QCoreApplication.translate("MainWindow", u"\u529f\u80fd\u4e09\uff1a\u8fd4\u56de\u684c\u9762", None))
        self.comboBox_301.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.comboBox_301.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_301.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_301.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_301.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_301.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_301.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_301.setItemText(7, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_301.setItemText(8, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_301.setItemText(9, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_301.setItemText(10, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox_301.setItemText(11, QCoreApplication.translate("MainWindow", u"11", None))
        self.comboBox_301.setItemText(12, QCoreApplication.translate("MainWindow", u"12", None))
        self.comboBox_301.setItemText(13, QCoreApplication.translate("MainWindow", u"13", None))
        self.comboBox_301.setItemText(14, QCoreApplication.translate("MainWindow", u"14", None))
        self.comboBox_301.setItemText(15, QCoreApplication.translate("MainWindow", u"15", None))
        self.comboBox_301.setItemText(16, QCoreApplication.translate("MainWindow", u"16", None))
        self.comboBox_301.setItemText(17, QCoreApplication.translate("MainWindow", u"17", None))
        self.comboBox_301.setItemText(18, QCoreApplication.translate("MainWindow", u"18", None))
        self.comboBox_301.setItemText(19, QCoreApplication.translate("MainWindow", u"19", None))
        self.comboBox_301.setItemText(20, QCoreApplication.translate("MainWindow", u"20", None))

        self.comboBox_302.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.comboBox_302.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_302.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_302.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_302.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_302.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_302.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_302.setItemText(7, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_302.setItemText(8, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_302.setItemText(9, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_302.setItemText(10, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox_302.setItemText(11, QCoreApplication.translate("MainWindow", u"11", None))
        self.comboBox_302.setItemText(12, QCoreApplication.translate("MainWindow", u"12", None))
        self.comboBox_302.setItemText(13, QCoreApplication.translate("MainWindow", u"13", None))
        self.comboBox_302.setItemText(14, QCoreApplication.translate("MainWindow", u"14", None))
        self.comboBox_302.setItemText(15, QCoreApplication.translate("MainWindow", u"15", None))
        self.comboBox_302.setItemText(16, QCoreApplication.translate("MainWindow", u"16", None))
        self.comboBox_302.setItemText(17, QCoreApplication.translate("MainWindow", u"17", None))
        self.comboBox_302.setItemText(18, QCoreApplication.translate("MainWindow", u"18", None))
        self.comboBox_302.setItemText(19, QCoreApplication.translate("MainWindow", u"19", None))
        self.comboBox_302.setItemText(20, QCoreApplication.translate("MainWindow", u"20", None))

        self.label_444.setText(QCoreApplication.translate("MainWindow", u"\u529f\u80fd\u56db\uff1a\u622a\u56fe", None))
        self.comboBox_402.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.comboBox_402.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_402.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_402.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_402.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_402.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_402.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_402.setItemText(7, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_402.setItemText(8, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_402.setItemText(9, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_402.setItemText(10, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox_402.setItemText(11, QCoreApplication.translate("MainWindow", u"11", None))
        self.comboBox_402.setItemText(12, QCoreApplication.translate("MainWindow", u"12", None))
        self.comboBox_402.setItemText(13, QCoreApplication.translate("MainWindow", u"13", None))
        self.comboBox_402.setItemText(14, QCoreApplication.translate("MainWindow", u"14", None))
        self.comboBox_402.setItemText(15, QCoreApplication.translate("MainWindow", u"15", None))
        self.comboBox_402.setItemText(16, QCoreApplication.translate("MainWindow", u"16", None))
        self.comboBox_402.setItemText(17, QCoreApplication.translate("MainWindow", u"17", None))
        self.comboBox_402.setItemText(18, QCoreApplication.translate("MainWindow", u"18", None))
        self.comboBox_402.setItemText(19, QCoreApplication.translate("MainWindow", u"19", None))
        self.comboBox_402.setItemText(20, QCoreApplication.translate("MainWindow", u"20", None))

        self.comboBox_401.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.comboBox_401.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_401.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_401.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_401.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_401.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_401.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_401.setItemText(7, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_401.setItemText(8, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_401.setItemText(9, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_401.setItemText(10, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox_401.setItemText(11, QCoreApplication.translate("MainWindow", u"11", None))
        self.comboBox_401.setItemText(12, QCoreApplication.translate("MainWindow", u"12", None))
        self.comboBox_401.setItemText(13, QCoreApplication.translate("MainWindow", u"13", None))
        self.comboBox_401.setItemText(14, QCoreApplication.translate("MainWindow", u"14", None))
        self.comboBox_401.setItemText(15, QCoreApplication.translate("MainWindow", u"15", None))
        self.comboBox_401.setItemText(16, QCoreApplication.translate("MainWindow", u"16", None))
        self.comboBox_401.setItemText(17, QCoreApplication.translate("MainWindow", u"17", None))
        self.comboBox_401.setItemText(18, QCoreApplication.translate("MainWindow", u"18", None))
        self.comboBox_401.setItemText(19, QCoreApplication.translate("MainWindow", u"19", None))
        self.comboBox_401.setItemText(20, QCoreApplication.translate("MainWindow", u"20", None))

        self.pushButton_saveSet.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u4fee\u6539", None))
        self.pushButton_default.setText(QCoreApplication.translate("MainWindow", u"\u6062\u590d\u9ed8\u8ba4", None))
        self.label_2.setText("")
        self.label_5.setText("")
        self.btn_save_user.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.set_phone.setText(QCoreApplication.translate("MainWindow", u"\u624b\u673a\u53f7", None))
        self.set_username.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u540d", None))
        self.set_email.setText(QCoreApplication.translate("MainWindow", u"\u90ae\u7bb1", None))
        self.head_label.setText("")
        self.label_11.setText("")
        self.label_12.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"                \u8be5\u9879\u76ee\u4e3b\u8981\u57fa\u4e8eOpencv\u89c6\u89c9\u6280\u672f+mediapipe\u5e93\u8fdb\u884c\u624b\u52bf\u8bc6\u522b\u5b9e\u73b0\u624b\u52bf\u4eba\u673a\u4ea4\u4e92\u5e94\u7528\u3002", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u7b80\u4ecb", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u8054\u7cfb\u90ae\u7bb1", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"                674792094@qq.com", None))
        self.label_9.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4\u65b0\u5bc6\u7801", None))
        self.re_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u540d", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5bc6\u7801", None))
        self.label_re_pw.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u5bc6\u7801", None))
        self.label_10.setText("")
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"\u76ae\u80a4\u5207\u6362", None))
        self.btn_help_feedback.setText(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9\u4e0e\u53cd\u9988", None))
        self.btn_we.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e\u6211\u4eec", None))
        self.btn_administrators.setText(QCoreApplication.translate("MainWindow", u"\u7ba1\u7406\u5458\u9875\u9762", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"\u8fd4\u56de\u767b\u5f55", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: hh", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.4.0", None))
    # retranslateUi

