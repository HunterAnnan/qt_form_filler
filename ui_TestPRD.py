# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TestPRDRpsRGN.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
        self.entry1 = QFrame(self.main_section)
        self.entry1.setObjectName(u"entry1")
        self.entry1.setMaximumSize(QSize(16777215, 40))
        self.entry1.setFrameShape(QFrame.StyledPanel)
        self.entry1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.entry1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(-1, 6, -1, 6)
        self.entry1_num_Label = QLabel(self.entry1)
        self.entry1_num_Label.setObjectName(u"entry1_num_Label")
        self.entry1_num_Label.setMinimumSize(QSize(40, 0))
        font1 = QFont()
        font1.setBold(True)
        self.entry1_num_Label.setFont(font1)
        self.entry1_num_Label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.entry1_num_Label)

        self.entry1_desc_Label = QLabel(self.entry1)
        self.entry1_desc_Label.setObjectName(u"entry1_desc_Label")
        self.entry1_desc_Label.setMinimumSize(QSize(200, 0))
        self.entry1_desc_Label.setIndent(5)

        self.horizontalLayout.addWidget(self.entry1_desc_Label)

        self.entry1_LineEdit = QLineEdit(self.entry1)
        self.entry1_LineEdit.setObjectName(u"entry1_LineEdit")

        self.horizontalLayout.addWidget(self.entry1_LineEdit)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 5)
        self.horizontalLayout.setStretch(2, 4)

        self.gridLayout_4.addWidget(self.entry1, 0, 0, 1, 1)

        self.entry2 = QFrame(self.main_section)
        self.entry2.setObjectName(u"entry2")
        self.entry2.setMaximumSize(QSize(16777215, 40))
        self.entry2.setFrameShape(QFrame.StyledPanel)
        self.entry2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.entry2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(-1, 6, -1, 6)
        self.entry2_num_Label = QLabel(self.entry2)
        self.entry2_num_Label.setObjectName(u"entry2_num_Label")
        self.entry2_num_Label.setMinimumSize(QSize(40, 0))
        self.entry2_num_Label.setFont(font1)
        self.entry2_num_Label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.entry2_num_Label)

        self.entry2_desc_Label = QLabel(self.entry2)
        self.entry2_desc_Label.setObjectName(u"entry2_desc_Label")
        self.entry2_desc_Label.setMinimumSize(QSize(200, 0))
        self.entry2_desc_Label.setIndent(5)

        self.horizontalLayout_3.addWidget(self.entry2_desc_Label)

        self.entry2_CheckBox = QCheckBox(self.entry2)
        self.entry2_CheckBox.setObjectName(u"entry2_CheckBox")

        self.horizontalLayout_3.addWidget(self.entry2_CheckBox)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 5)
        self.horizontalLayout_3.setStretch(2, 4)

        self.gridLayout_4.addWidget(self.entry2, 1, 0, 1, 1)

        self.entry3 = QFrame(self.main_section)
        self.entry3.setObjectName(u"entry3")
        self.entry3.setMaximumSize(QSize(16777215, 40))
        self.entry3.setFrameShape(QFrame.StyledPanel)
        self.entry3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.entry3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 6, -1, 6)
        self.entry3_num_Label = QLabel(self.entry3)
        self.entry3_num_Label.setObjectName(u"entry3_num_Label")
        self.entry3_num_Label.setMinimumSize(QSize(40, 0))
        self.entry3_num_Label.setFont(font1)
        self.entry3_num_Label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.entry3_num_Label)

        self.entry3_desc_Label = QLabel(self.entry3)
        self.entry3_desc_Label.setObjectName(u"entry3_desc_Label")
        self.entry3_desc_Label.setMinimumSize(QSize(200, 0))
        self.entry3_desc_Label.setIndent(5)

        self.horizontalLayout_4.addWidget(self.entry3_desc_Label)

        self.entry3_CheckBox = QCheckBox(self.entry3)
        self.entry3_CheckBox.setObjectName(u"entry3_CheckBox")

        self.horizontalLayout_4.addWidget(self.entry3_CheckBox)

        self.entry3_LineEdit = QLineEdit(self.entry3)
        self.entry3_LineEdit.setObjectName(u"entry3_LineEdit")
        self.entry3_LineEdit.setMaxLength(4)

        self.horizontalLayout_4.addWidget(self.entry3_LineEdit)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 5)
        self.horizontalLayout_4.setStretch(2, 2)
        self.horizontalLayout_4.setStretch(3, 2)

        self.gridLayout_4.addWidget(self.entry3, 2, 0, 1, 1)


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
        self.wo_num_Label = QLabel(self.top_section)
        self.wo_num_Label.setObjectName(u"wo_num_Label")
        self.wo_num_Label.setMinimumSize(QSize(150, 0))
        self.wo_num_Label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.wo_num_Label)

        self.wo_num_SpinBox = QSpinBox(self.top_section)
        self.wo_num_SpinBox.setObjectName(u"wo_num_SpinBox")
        self.wo_num_SpinBox.setMaximumSize(QSize(60, 16777215))
        self.wo_num_SpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.wo_num_SpinBox.setMaximum(99999)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.wo_num_SpinBox)

        self.serial_num_Label = QLabel(self.top_section)
        self.serial_num_Label.setObjectName(u"serial_num_Label")
        self.serial_num_Label.setMinimumSize(QSize(150, 0))
        self.serial_num_Label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.serial_num_Label)

        self.serial_num_SpinBox = QSpinBox(self.top_section)
        self.serial_num_SpinBox.setObjectName(u"serial_num_SpinBox")
        self.serial_num_SpinBox.setMaximumSize(QSize(60, 16777215))
        self.serial_num_SpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.serial_num_SpinBox.setMaximum(999)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.serial_num_SpinBox)


        self.horizontalLayout_5.addLayout(self.formLayout_4)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setHorizontalSpacing(6)
        self.wo_start_Label = QLabel(self.top_section)
        self.wo_start_Label.setObjectName(u"wo_start_Label")
        self.wo_start_Label.setMinimumSize(QSize(150, 0))
        self.wo_start_Label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.wo_start_Label)

        self.wo_start_DateEdit = QDateEdit(self.top_section)
        self.wo_start_DateEdit.setObjectName(u"wo_start_DateEdit")
        self.wo_start_DateEdit.setMaximumSize(QSize(100, 16777215))
        self.wo_start_DateEdit.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.wo_start_DateEdit.setCalendarPopup(True)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.wo_start_DateEdit)

        self.wo_finish_Label = QLabel(self.top_section)
        self.wo_finish_Label.setObjectName(u"wo_finish_Label")
        self.wo_finish_Label.setMinimumSize(QSize(150, 0))
        self.wo_finish_Label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.wo_finish_Label)

        self.wo_finish_DateEdit = QDateEdit(self.top_section)
        self.wo_finish_DateEdit.setObjectName(u"wo_finish_DateEdit")
        self.wo_finish_DateEdit.setMaximumSize(QSize(100, 16777215))
        self.wo_finish_DateEdit.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.wo_finish_DateEdit.setCalendarPopup(True)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.wo_finish_DateEdit)


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
        self.menubar.setEnabled(True)
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
        self.entry1_num_Label.setText(QCoreApplication.translate("MainWindow", u"1.2.3", None))
        self.entry1_desc_Label.setText(QCoreApplication.translate("MainWindow", u"Activity description 1 (serial no.)", None))
        self.entry1_LineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"X0-XXX-XX000", None))
        self.entry2_num_Label.setText(QCoreApplication.translate("MainWindow", u"2.3.4", None))
        self.entry2_desc_Label.setText(QCoreApplication.translate("MainWindow", u"Activity description 2 (check confirm)", None))
        self.entry2_CheckBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.entry3_num_Label.setText(QCoreApplication.translate("MainWindow", u"3.4.5", None))
        self.entry3_desc_Label.setText(QCoreApplication.translate("MainWindow", u"Activity description 3 (check and sign)", None))
        self.entry3_CheckBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.entry3_LineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Initial", None))
        self.wo_num_Label.setText(QCoreApplication.translate("MainWindow", u"Work Order Number:", None))
        self.serial_num_Label.setText(QCoreApplication.translate("MainWindow", u"Serial Number:", None))
        self.wo_start_Label.setText(QCoreApplication.translate("MainWindow", u"Work Order Started:", None))
        self.wo_start_DateEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd MMM yyyy", None))
        self.wo_finish_Label.setText(QCoreApplication.translate("MainWindow", u"Work Order Finished:", None))
        self.wo_finish_DateEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd MMM yyyy", None))
        self.submitButton.setText(QCoreApplication.translate("MainWindow", u"Submit Traveller", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"Save (part-complete)", None))
    # retranslateUi

