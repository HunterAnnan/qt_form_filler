# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TestPRD.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QDateEdit,
    QFormLayout, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 346)
        MainWindow.setMinimumSize(QSize(600, 200))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QSize(600, 200))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setMinimumSize(QSize(0, 20))
        self.title.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(True)
        font.setKerning(True)
        self.title.setFont(font)
        self.title.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.title, 0, 0, 1, 1)

        self.main_section = QFrame(self.centralwidget)
        self.main_section.setObjectName(u"main_section")
        self.main_section.setFrameShape(QFrame.StyledPanel)
        self.main_section.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.main_section)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(0)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.line1 = QFrame(self.main_section)
        self.line1.setObjectName(u"line1")
        self.line1.setMaximumSize(QSize(16777215, 40))
        self.line1.setFrameShape(QFrame.StyledPanel)
        self.line1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.line1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(-1, 6, -1, 6)
        self.label_8 = QLabel(self.line1)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(40, 0))
        font1 = QFont()
        font1.setBold(True)
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_8)

        self.label_7 = QLabel(self.line1)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(200, 0))
        self.label_7.setIndent(5)

        self.horizontalLayout.addWidget(self.label_7)

        self.lineEdit_4 = QLineEdit(self.line1)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout.addWidget(self.lineEdit_4)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 5)
        self.horizontalLayout.setStretch(2, 4)

        self.gridLayout_4.addWidget(self.line1, 0, 0, 1, 1)

        self.line2 = QFrame(self.main_section)
        self.line2.setObjectName(u"line2")
        self.line2.setMaximumSize(QSize(16777215, 40))
        self.line2.setFrameShape(QFrame.StyledPanel)
        self.line2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.line2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(-1, 6, -1, 6)
        self.label_6 = QLabel(self.line2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(40, 0))
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_6)

        self.label_5 = QLabel(self.line2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(200, 0))
        self.label_5.setIndent(5)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.checkBox = QCheckBox(self.line2)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_3.addWidget(self.checkBox)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 5)
        self.horizontalLayout_3.setStretch(2, 4)

        self.gridLayout_4.addWidget(self.line2, 1, 0, 1, 1)

        self.line3 = QFrame(self.main_section)
        self.line3.setObjectName(u"line3")
        self.line3.setMaximumSize(QSize(16777215, 40))
        self.line3.setFrameShape(QFrame.StyledPanel)
        self.line3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.line3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 6, -1, 6)
        self.label_9 = QLabel(self.line3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(40, 0))
        self.label_9.setFont(font1)
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_9)

        self.label_10 = QLabel(self.line3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(200, 0))
        self.label_10.setIndent(5)

        self.horizontalLayout_4.addWidget(self.label_10)

        self.checkBox_2 = QCheckBox(self.line3)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.horizontalLayout_4.addWidget(self.checkBox_2)

        self.lineEdit = QLineEdit(self.line3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaxLength(4)

        self.horizontalLayout_4.addWidget(self.lineEdit)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 5)
        self.horizontalLayout_4.setStretch(2, 2)
        self.horizontalLayout_4.setStretch(3, 2)

        self.gridLayout_4.addWidget(self.line3, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.main_section, 2, 0, 1, 1)

        self.top_section = QFrame(self.centralwidget)
        self.top_section.setObjectName(u"top_section")
        self.top_section.setMaximumSize(QSize(16777215, 80))
        self.top_section.setFrameShape(QFrame.StyledPanel)
        self.top_section.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.top_section)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setRowWrapPolicy(QFormLayout.DontWrapRows)
        self.formLayout_4.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout_4.setHorizontalSpacing(6)
        self.wONumberLabel_2 = QLabel(self.top_section)
        self.wONumberLabel_2.setObjectName(u"wONumberLabel_2")
        self.wONumberLabel_2.setMinimumSize(QSize(150, 0))
        self.wONumberLabel_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.wONumberLabel_2)

        self.wONumberSpinBox_2 = QSpinBox(self.top_section)
        self.wONumberSpinBox_2.setObjectName(u"wONumberSpinBox_2")
        self.wONumberSpinBox_2.setMaximumSize(QSize(60, 16777215))
        self.wONumberSpinBox_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.wONumberSpinBox_2.setMaximum(99999)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.wONumberSpinBox_2)

        self.serialNumberLabel_2 = QLabel(self.top_section)
        self.serialNumberLabel_2.setObjectName(u"serialNumberLabel_2")
        self.serialNumberLabel_2.setMinimumSize(QSize(150, 0))
        self.serialNumberLabel_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.serialNumberLabel_2)

        self.serialNumberSpinBox_2 = QSpinBox(self.top_section)
        self.serialNumberSpinBox_2.setObjectName(u"serialNumberSpinBox_2")
        self.serialNumberSpinBox_2.setMaximumSize(QSize(60, 16777215))
        self.serialNumberSpinBox_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.serialNumberSpinBox_2.setMaximum(999)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.serialNumberSpinBox_2)


        self.horizontalLayout_5.addLayout(self.formLayout_4)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setHorizontalSpacing(6)
        self.wOStartLabel_2 = QLabel(self.top_section)
        self.wOStartLabel_2.setObjectName(u"wOStartLabel_2")
        self.wOStartLabel_2.setMinimumSize(QSize(150, 0))
        self.wOStartLabel_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.wOStartLabel_2)

        self.wOStartDateEdit_2 = QDateEdit(self.top_section)
        self.wOStartDateEdit_2.setObjectName(u"wOStartDateEdit_2")
        self.wOStartDateEdit_2.setMaximumSize(QSize(100, 16777215))
        self.wOStartDateEdit_2.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.wOStartDateEdit_2.setCalendarPopup(True)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.wOStartDateEdit_2)

        self.wOFinishedLabel_2 = QLabel(self.top_section)
        self.wOFinishedLabel_2.setObjectName(u"wOFinishedLabel_2")
        self.wOFinishedLabel_2.setMinimumSize(QSize(150, 0))
        self.wOFinishedLabel_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.wOFinishedLabel_2)

        self.wOFinishedDateEdit_2 = QDateEdit(self.top_section)
        self.wOFinishedDateEdit_2.setObjectName(u"wOFinishedDateEdit_2")
        self.wOFinishedDateEdit_2.setMaximumSize(QSize(100, 16777215))
        self.wOFinishedDateEdit_2.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.wOFinishedDateEdit_2.setCalendarPopup(True)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.wOFinishedDateEdit_2)


        self.horizontalLayout_5.addLayout(self.formLayout_3)


        self.gridLayout.addWidget(self.top_section, 1, 0, 1, 1)

        self.submit_section = QFrame(self.centralwidget)
        self.submit_section.setObjectName(u"submit_section")
        self.submit_section.setMinimumSize(QSize(0, 30))
        self.submit_section.setMaximumSize(QSize(16777215, 30))
        self.submit_section.setFrameShape(QFrame.StyledPanel)
        self.submit_section.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.submit_section)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.submitButton = QPushButton(self.submit_section)
        self.submitButton.setObjectName(u"submitButton")
        self.submitButton.setMinimumSize(QSize(120, 24))
        self.submitButton.setMaximumSize(QSize(120, 24))
        self.submitButton.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_2.addWidget(self.submitButton, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.saveButton = QPushButton(self.submit_section)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_2.addWidget(self.saveButton, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.submit_section, 3, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 600, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"PRD____ Traveller (Example)", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"1.2.3", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Activity description 1 (serial no.)", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"X0-XXX-XX000", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"2.3.4", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Activity description 2 (check confirm)", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"3.4.5", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Activity description 3 (check and sign)", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Initial", None))
        self.wONumberLabel_2.setText(QCoreApplication.translate("MainWindow", u"Work Order Number:", None))
        self.serialNumberLabel_2.setText(QCoreApplication.translate("MainWindow", u"Serial Number:", None))
        self.wOStartLabel_2.setText(QCoreApplication.translate("MainWindow", u"Work Order Started:", None))
        self.wOStartDateEdit_2.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd MMM yyyy", None))
        self.wOFinishedLabel_2.setText(QCoreApplication.translate("MainWindow", u"Work Order Finished:", None))
        self.wOFinishedDateEdit_2.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd MMM yyyy", None))
        self.submitButton.setText(QCoreApplication.translate("MainWindow", u"Submit Traveller", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"Save (part-complete)", None))
    # retranslateUi

