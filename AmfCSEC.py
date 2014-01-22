# -*- coding: utf-8 -*-

# AMF Auto-Pilot Source-Codes
# CoreSEC Software Development Group
# Created: Sun Nov 17 19:59:11 2013
# Written in Python and QT
# Mark Anthony Pequeras

from PyQt4 import QtCore, QtGui
import sqlite3 as data

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(839, 159)
        Form.setStyleSheet(_fromUtf8("background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #26293B , stop: 1 #333751);"))
        self.Logo = QtGui.QLabel(Form)
        self.Logo.setGeometry(QtCore.QRect(20, 50, 191, 21))


        self.Logo.setStyleSheet(_fromUtf8("background: transparent;"))
        self.Logo.setText(_fromUtf8(""))
        self.Logo.setPixmap(QtGui.QPixmap(_fromUtf8("imgs/logo.png")))
        self.Logo.setObjectName(_fromUtf8("Logo"))
        self.OrangeBar = QtGui.QPlainTextEdit(Form)
        self.OrangeBar.setEnabled(False)
        self.OrangeBar.setGeometry(QtCore.QRect(220, 10, 611, 131))
        self.OrangeBar.setStyleSheet(_fromUtf8("border-radius: 15px 33px 22px 33px;\n"
"border: 3px outset #333751;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #26293B , stop: 1 #26293B);"))
        self.OrangeBar.setObjectName(_fromUtf8("OrangeBar"))
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(240, 20, 571, 111))
        self.tabWidget.setStyleSheet(_fromUtf8("QTabWidget::tab-bar {\n"
"background: none;\n"
"border: transparent;\n"
"border-color: transparent;\n"
"\n"
" }\n"
"\n"
" QTabBar::tab {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #26293B , stop: 1 #26293B);\n"
"  color: white;\n"
"border: none;\n"
"  padding: 10px;\n"
" }\n"
"\n"
" QTabBar::tab:selected {\n"
"  background: orange;\n"
"border: none;\n"
" }\n"
"\n"
"\n"
"QTabWidget::pane { border: 0; }"))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.SettingsTab = QtGui.QWidget()
        self.SettingsTab.setObjectName(_fromUtf8("SettingsTab"))
        self.StartButton = QtGui.QPushButton(self.SettingsTab)
        self.StartButton.setGeometry(QtCore.QRect(300, 10, 261, 51))
        self.StartButton.setStyleSheet(_fromUtf8("QPushButton{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffcc00, stop: 1 #b87f2b);\n"
"color: #ffffff;\n"
"border: none;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2980b9, stop: 1 #3498db);\n"
"\n"
"border: none;\n"
"\n"
"}\n"
"\n"
""))
        self.StartButton.setObjectName(_fromUtf8("StartButton"))
        self.CreateAccountButton = QtGui.QPushButton(self.SettingsTab)
        self.CreateAccountButton.setGeometry(QtCore.QRect(150, 10, 141, 31))
        self.CreateAccountButton.setStyleSheet(_fromUtf8("background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #3498db, stop: 1 #2980b9); \n"
"border: none;\n"
"color: white;"))
        self.CreateAccountButton.setObjectName(_fromUtf8("CreateAccountButton"))
        self.label_8 = QtGui.QLabel(self.SettingsTab)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(_fromUtf8("color: rgb(181, 181, 181);"))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.SettingsTab)
        self.label_9.setGeometry(QtCore.QRect(10, 30, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(_fromUtf8("color: rgb(181, 181, 181);"))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.SettingsTab)
        self.label_10.setGeometry(QtCore.QRect(10, 50, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(_fromUtf8("color: rgb(181, 181, 181);"))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.SliderValue = QtGui.QLabel(self.SettingsTab)
        self.SliderValue.setGeometry(QtCore.QRect(270, 50, 21, 16))
        self.SliderValue.setStyleSheet(_fromUtf8("background: transparent;\n"
"color: white;"))
        self.SliderValue.setObjectName(_fromUtf8("SliderValue"))
        self.SpeedSlider = QtGui.QSlider(self.SettingsTab)
        self.SpeedSlider.setGeometry(QtCore.QRect(190, 50, 71, 20))
        self.SpeedSlider.setStyleSheet(_fromUtf8("background: none;"))
        self.SpeedSlider.setMinimum(1)
        self.SpeedSlider.setMaximum(100)
        self.SpeedSlider.setTracking(True)
        self.SpeedSlider.setOrientation(QtCore.Qt.Horizontal)
        self.SpeedSlider.setInvertedAppearance(False)
        self.SpeedSlider.setInvertedControls(False)
        self.SpeedSlider.setTickPosition(QtGui.QSlider.TicksBelow)
        self.SpeedSlider.setTickInterval(0)
        self.SpeedSlider.setObjectName(_fromUtf8("SpeedSlider"))
        self.label_33 = QtGui.QLabel(self.SettingsTab)
        self.label_33.setGeometry(QtCore.QRect(150, 50, 31, 16))
        self.label_33.setStyleSheet(_fromUtf8("color: #ffffff;\n"
"background: none;"))
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.tabWidget.addTab(self.SettingsTab, _fromUtf8(""))
        self.PlayNow = QtGui.QWidget()
        self.PlayNow.setObjectName(_fromUtf8("PlayNow"))
        self.label_11 = QtGui.QLabel(self.PlayNow)
        self.label_11.setGeometry(QtCore.QRect(10, 10, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(_fromUtf8("background: transparent;\n"
"color: white;"))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.PlayNow)
        self.label_12.setGeometry(QtCore.QRect(10, 40, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(_fromUtf8("background: transparent;\n"
"color: white;"))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.MainXBox = QtGui.QPlainTextEdit(self.PlayNow)
        ### CONDS MX
        mxx = open('main/mainx', 'r+')
        mxo = mxx.read()
        if len(str(mxo)) > 0:
            self.MainXBox.insertPlainText(str(mxo))
        self.MainXBox.setGeometry(QtCore.QRect(120, 10, 51, 21))
        mxx.close()  ### CLOSE
        self.MainXBox.setStyleSheet(_fromUtf8("color: white;\n"
"border-radius: 7px 7px 7px 30px;\n"
"\n"
"border: 1px outset #f2f2f2;"))
        self.MainXBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.MainXBox.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.MainXBox.setObjectName(_fromUtf8("MainXBox"))


        self.MainYBox = QtGui.QPlainTextEdit(self.PlayNow)
        myo = open('main/mainy', 'r+')
        myr = myo.read()
        if len(str(myr)) > 0:
            self.MainYBox.insertPlainText(str(myr))
        self.MainYBox.setGeometry(QtCore.QRect(120, 40, 51, 21))
        myo.close()
        self.MainYBox.setStyleSheet(_fromUtf8("color: white;\n"
"border-radius: 7px 7px 7px 30px;\n"
"\n"
"border: 1px outset #f2f2f2;"))
        self.MainYBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.MainYBox.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.MainYBox.setObjectName(_fromUtf8("MainYBox"))
        self.PointerXBox = QtGui.QPlainTextEdit(self.PlayNow)
        pxo = open('pointer/pointerx', 'r+')
        pxr = pxo.read()
        if len(str(pxr)) > 0:
            self.PointerXBox.insertPlainText(str(pxr))
        self.PointerXBox.setGeometry(QtCore.QRect(310, 10, 51, 21))
        pxo.close()
        self.PointerXBox.setStyleSheet(_fromUtf8("color: white;\n"
"border-radius: 7px 7px 7px 30px;\n"
"\n"
"border: 1px outset #f2f2f2;"))
        self.PointerXBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.PointerXBox.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.PointerXBox.setObjectName(_fromUtf8("PointerXBox"))
        self.label_13 = QtGui.QLabel(self.PlayNow)
        self.label_13.setGeometry(QtCore.QRect(200, 10, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(_fromUtf8("background: transparent;\n"
"color: white;"))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.PointerYBox = QtGui.QPlainTextEdit(self.PlayNow)
        pyo = open('pointer/pointery', 'r+')
        pyr = pyo.read()
        if len(str(pxr)) > 0:
            self.PointerYBox.insertPlainText(str(pyr))
        self.PointerYBox.setGeometry(QtCore.QRect(310, 40, 51, 21))
        pyo.close()
        self.PointerYBox.setStyleSheet(_fromUtf8("color: white;\n"
"border-radius: 7px 7px 7px 30px;\n"
"\n"
"border: 1px outset #f2f2f2;"))
        self.PointerYBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.PointerYBox.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.PointerYBox.setObjectName(_fromUtf8("PointerYBox"))
        self.label_14 = QtGui.QLabel(self.PlayNow)
        self.label_14.setGeometry(QtCore.QRect(200, 40, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(_fromUtf8("background: transparent;\n"
"color: white;"))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.CloseXBox = QtGui.QPlainTextEdit(self.PlayNow)
        co = open('close/closex', 'r+')
        cor = co.read()
        if len(str(cor)) > 0:
            self.CloseXBox.insertPlainText(str(cor))
        self.CloseXBox.setGeometry(QtCore.QRect(500, 10, 51, 21))
        co.close()
        self.CloseXBox.setStyleSheet(_fromUtf8("color: white;\n"
"border-radius: 7px 7px 7px 30px;\n"
"\n"
"border: 1px outset #f2f2f2;"))
        self.CloseXBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.CloseXBox.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.CloseXBox.setObjectName(_fromUtf8("CloseXBox"))
        self.label_15 = QtGui.QLabel(self.PlayNow)
        self.label_15.setGeometry(QtCore.QRect(390, 10, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(_fromUtf8("background: transparent;\n"
"color: white;"))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(self.PlayNow)
        self.label_16.setGeometry(QtCore.QRect(390, 40, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet(_fromUtf8("background: transparent;\n"
"color: white;"))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.CloseYBox = QtGui.QPlainTextEdit(self.PlayNow)
        cy = open('close/closey', 'r+')
        cyr = cy.read()
        if len(str(cyr)) > 0:
            self.CloseYBox.insertPlainText(str(cyr))
        self.CloseYBox.setGeometry(QtCore.QRect(500, 40, 51, 21))
        cy.close()
        self.CloseYBox.setStyleSheet(_fromUtf8("color: white;\n"
"border-radius: 7px 7px 7px 30px;\n"
"\n"
"border: 1px outset #f2f2f2;"))
        self.CloseYBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.CloseYBox.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.CloseYBox.setObjectName(_fromUtf8("CloseYBox"))
        self.line = QtGui.QFrame(self.PlayNow)
        self.line.setGeometry(QtCore.QRect(180, 0, 3, 61))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.PlayNow)
        self.line_2.setGeometry(QtCore.QRect(380, 0, 3, 61))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.ListCoordinatesButton_2 = QtGui.QPushButton(self.PlayNow)
        self.ListCoordinatesButton_2.setGeometry(QtCore.QRect(200, 60, 60, 16))
        self.ListCoordinatesButton_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.ListCoordinatesButton_2.setStyleSheet(_fromUtf8("QPushButton{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #3498db, stop: 1 #2980b9);\n"
"color: #ffffff;\n"
"border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2980b9, stop: 1 #3498db);\n"
"\n"
"border: none;\n"
"\n"
"}\n"
"\n"
""))
        self.ListCoordinatesButton_2.setObjectName(_fromUtf8("ListCoordinatesButton_2"))



        self.GetMain = QtGui.QPushButton(self.PlayNow)
        self.GetMain.setGeometry(QtCore.QRect(75, 60, 40, 16))
        self.GetMain.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.GetMain.setStyleSheet(_fromUtf8("QPushButton{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #3498db, stop: 1 #2980b9);\n"
"color: #ffffff;\n"
"border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2980b9, stop: 1 #3498db);\n"
"\n"
"border: none;\n"
"\n"
"}\n"
"\n"
""))
        self.GetMain.setObjectName(_fromUtf8("GetMainx"))


        self.GetPoint = QtGui.QPushButton(self.PlayNow)
        self.GetPoint.setGeometry(QtCore.QRect(265, 60, 40, 16))
        self.GetPoint.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.GetPoint.setStyleSheet(_fromUtf8("QPushButton{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #3498db, stop: 1 #2980b9);\n"
"color: #ffffff;\n"
"border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2980b9, stop: 1 #3498db);\n"
"\n"
"border: none;\n"
"\n"
"}\n"
"\n"
""))
        self.GetPoint.setObjectName(_fromUtf8("GetPoint"))





        self.ListCoordinatesButton_3 = QtGui.QPushButton(self.PlayNow)
        self.ListCoordinatesButton_3.setGeometry(QtCore.QRect(10, 60, 60, 16))
        self.ListCoordinatesButton_3.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.ListCoordinatesButton_3.setStyleSheet(_fromUtf8("QPushButton{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #3498db, stop: 1 #2980b9);\n"
"color: #ffffff;\n"
"border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2980b9, stop: 1 #3498db);\n"
"\n"
"border: none;\n"
"\n"
"}\n"
"\n"
""))
        self.ListCoordinatesButton_3.setObjectName(_fromUtf8("ListCoordinatesButton_3"))
        self.ListCoordinatesButton_4 = QtGui.QPushButton(self.PlayNow)
        self.ListCoordinatesButton_4.setGeometry(QtCore.QRect(390, 60, 60, 16))
        self.ListCoordinatesButton_4.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.ListCoordinatesButton_4.setStyleSheet(_fromUtf8("QPushButton{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #3498db, stop: 1 #2980b9);\n"
"color: #ffffff;\n"
"border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2980b9, stop: 1 #3498db);\n"
"\n"
"border: none;\n"
"\n"
"}\n"
"\n"
""))
        self.ListCoordinatesButton_4.setObjectName(_fromUtf8("ListCoordinatesButton_4"))
        self.tabWidget.addTab(self.PlayNow, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.ListCoordinatesButton = QtGui.QPushButton(self.tab)
        self.ListCoordinatesButton.setGeometry(QtCore.QRect(310, 10, 251, 51))
        self.ListCoordinatesButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.ListCoordinatesButton.setStyleSheet(_fromUtf8("QPushButton{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #3498db, stop: 1 #2980b9);\n"
"color: #ffffff;\n"
"border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2980b9, stop: 1 #3498db);\n"
"\n"
"border: none;\n"
"\n"
"}\n"
"\n"
""))
        self.ListCoordinatesButton.setObjectName(_fromUtf8("ListCoordinatesButton"))
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(20, 10, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(_fromUtf8("background: transparent;\n"
"color: white;"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(40, 40, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(_fromUtf8("background: transparent;\n"
"color: white;"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.GetPosX = QtGui.QTextEdit(self.tab)
        self.GetPosX.setGeometry(QtCore.QRect(150, 10, 151, 21))
        self.GetPosX.setStyleSheet(_fromUtf8("color: white;"))
        self.GetPosX.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.GetPosX.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.GetPosX.setObjectName(_fromUtf8("GetPosX"))
        self.GetPosY = QtGui.QTextEdit(self.tab)
        self.GetPosY.setGeometry(QtCore.QRect(150, 40, 151, 21))
        self.GetPosY.setStyleSheet(_fromUtf8("color: white;"))
        self.GetPosY.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.GetPosY.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.GetPosY.setObjectName(_fromUtf8("GetPosY"))

        self.GetClose = QtGui.QPushButton(self.PlayNow)
        self.GetClose.setGeometry(QtCore.QRect(454, 60, 40, 16))
        self.GetClose.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.GetClose.setStyleSheet(_fromUtf8("QPushButton{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #3498db, stop: 1 #2980b9);\n"
"color: #ffffff;\n"
"border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2980b9, stop: 1 #3498db);\n"
"\n"
"border: none;\n"
"\n"
"}\n"
"\n"
""))
        self.GetClose.setObjectName(_fromUtf8("GetClose"))


        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.ContactTab = QtGui.QWidget()
        self.ContactTab.setObjectName(_fromUtf8("ContactTab"))
        self.label_36 = QtGui.QLabel(self.ContactTab)
        self.label_36.setGeometry(QtCore.QRect(20, 0, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet(_fromUtf8("color: rgb(166, 166, 166);\n"
"background: none;"))
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.UpgradeButton = QtGui.QPushButton(self.ContactTab)
        self.UpgradeButton.setGeometry(QtCore.QRect(360, 30, 201, 21))
        self.UpgradeButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.UpgradeButton.setStyleSheet(_fromUtf8("QPushButton{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #3498db, stop: 1 #2980b9);\n"
"color: #ffffff;\n"
"border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2980b9, stop: 1 #3498db);\n"
"\n"
"border: none;\n"
"\n"
"}\n"
"\n"
""))
        self.UpgradeButton.setObjectName(_fromUtf8("UpgradeButton"))
        self.SerialBox = QtGui.QLineEdit(self.ContactTab)
        self.SerialBox.setGeometry(QtCore.QRect(360, 0, 201, 20))
        self.SerialBox.setStyleSheet(_fromUtf8("color: white;\n"
"border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;"))
        self.SerialBox.setEchoMode(QtGui.QLineEdit.Password)
        self.SerialBox.setObjectName(_fromUtf8("SerialBox"))
        self.OrderButton = QtGui.QPushButton(self.ContactTab)
        self.OrderButton.setGeometry(QtCore.QRect(130, 45, 50, 24))
        self.OrderButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.OrderButton.setStyleSheet(_fromUtf8("QPushButton{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #3498db, stop: 1 #2980b9);\n"
"color: #ffffff;\n"
"border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2980b9, stop: 1 #3498db);\n"
"\n"
"border: none;\n"
"\n"
"}\n"
"\n"
""))
        self.OrderButton.setObjectName(_fromUtf8("OrderButton"))
        self.SubscriptionStatus = QtGui.QLabel(self.ContactTab)
        self.SubscriptionStatus.setGeometry(QtCore.QRect(380, 50, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.SubscriptionStatus.setFont(font)
        self.SubscriptionStatus.setStyleSheet(_fromUtf8("background: transparent;\n"
"color: white;"))
        self.SubscriptionStatus.setObjectName(_fromUtf8("SubscriptionStatus"))
        self.lineEdit = QtGui.QLineEdit(self.ContactTab)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(360, 20, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(5)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(_fromUtf8("background: transparent;\n"
"color: white;"))
        self.lineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.YourKeyBox = QtGui.QTextEdit(self.ContactTab)

        self.YourKeyBox.setGeometry(QtCore.QRect(190, 40, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.YourKeyBox.setFont(font)
        self.YourKeyBox.setStyleSheet(_fromUtf8("background: transparent;\n"
"color: rgb(116, 116, 116);"))
        self.YourKeyBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.YourKeyBox.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.YourKeyBox.setObjectName(_fromUtf8("YourKeyBox"))
        self.label = QtGui.QLabel(self.ContactTab)
        self.label.setGeometry(QtCore.QRect(250, 30, 46, 13))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color: white;"))
        self.label.setObjectName(_fromUtf8("label"))
        self.tabWidget.addTab(self.ContactTab, _fromUtf8(""))

        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 70, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("color: rgb(181, 181, 181);"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.footercoresec = QtGui.QLabel(Form)
        self.footercoresec.setGeometry(QtCore.QRect(450, 140, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.footercoresec.setFont(font)
        self.footercoresec.setStyleSheet(_fromUtf8("background: transparent;\n"
"color: rgb(162, 162, 162);"))
        self.footercoresec.setObjectName(_fromUtf8("footercoresec"))
        self.CloseButton = QtGui.QPushButton(Form)
        self.CloseButton.setGeometry(QtCore.QRect(70, 10, 31, 21))
        self.CloseButton.setStyleSheet(_fromUtf8("background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #3498db, stop: 1 #2980b9); \n"
"border: none;\n"
"color: white;"))
        self.CloseButton.setObjectName(_fromUtf8("CloseButton"))
        self.MinimizeButton = QtGui.QPushButton(Form)
        self.MinimizeButton.setGeometry(QtCore.QRect(30, 10, 31, 21))
        self.MinimizeButton.setStyleSheet(_fromUtf8("background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #3498db, stop: 1 #2980b9); \n"
"border: none;\n"
"color: white;"))
        self.MinimizeButton.setObjectName(_fromUtf8("MinimizeButton"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 95, 181, 16))
        self.label_2.setStyleSheet(_fromUtf8("color: white;"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.textEdit = QtGui.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(20, 110, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet(_fromUtf8("color: white;"))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        #QtCore.QObject.connect(self.OrangeBar, QtCore.SIGNAL(_fromUtf8('clicked()')), self.moveMe)
        QtCore.QObject.connect(self.SerialBox, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.lineEdit.setText)
        QtCore.QObject.connect(self.SpeedSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.SliderValue.setNum)
        QtCore.QObject.connect(self.CreateAccountButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.CreateAccountFunction)
        QtCore.QObject.connect(self.StartButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.StartThreadsFunction)
        QtCore.QObject.connect(self.ListCoordinatesButton_3, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.SaveMainPositionFunction)
        QtCore.QObject.connect(self.ListCoordinatesButton_2, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.SavePointerPositionFunction)
        QtCore.QObject.connect(self.ListCoordinatesButton_4, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.SaveClosePositionFunction)
        QtCore.QObject.connect(self.ListCoordinatesButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.ListGetPositionsFunction)
        QtCore.QObject.connect(self.OrderButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.OrderNowFunction)
        QtCore.QObject.connect(self.UpgradeButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.UpgradeNowFunction)
        QtCore.QObject.connect(self.MinimizeButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showMinimized)
        QtCore.QObject.connect(self.CloseButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.closeFunction)
        QtCore.QObject.connect(self.GetMain, QtCore.SIGNAL(_fromUtf8("clicked()")), self.GetMainFunction)
        QtCore.QObject.connect(self.GetPoint, QtCore.SIGNAL(_fromUtf8("clicked()")), self.GetPointFunction)
        QtCore.QObject.connect(self.GetClose, QtCore.SIGNAL(_fromUtf8("clicked()")), self.GetCloseFunction)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "AMF Auto-Clicker", None))
        self.StartButton.setText(_translate("Form", "Start Threads", None))
        self.CreateAccountButton.setText(_translate("Form", "Create Account Now", None))
        self.label_8.setText(_translate("Form", "- Create an Account", None))
        self.label_9.setText(_translate("Form", "- Edit Settings (Positions)", None))
        self.label_10.setText(_translate("Form", "- Start Threads!", None))
        self.SliderValue.setText(_translate("Form", "7", None))
        self.label_33.setText(_translate("Form", "Speed", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SettingsTab), _translate("Form", "Start", None))
        #mx = open('main/mainx', 'r+').read() ## Open MX File
        #my = open('main/mainy', 'r+').read() ## Open MY File
        readlic = open('lic','r+').read()
        if len(readlic) > 1:
            self.YourKeyBox.insertPlainText(str(readlic))

        self.label_11.setText(_translate("Form", "Horizontal Main Position", None))
        self.label_12.setText(_translate("Form", "Vertical Main Position", None))
        self.label_13.setText(_translate("Form", "Horizontal Points Position", None))
        self.label_14.setText(_translate("Form", "Horizontal Points Position", None))
        self.label_15.setText(_translate("Form", "Horizontal Close Position", None))
        self.label_16.setText(_translate("Form", "Vertical Close Position", None))
        self.GetClose.setText(_translate("Form", "GET", None))
        self.GetPoint.setText(_translate("Form", "GET", None))
        self.GetMain.setText(_translate("Form", "GET", None))
        self.ListCoordinatesButton_2.setText(_translate("Form", "Save", None))
        self.ListCoordinatesButton_3.setText(_translate("Form", "Save", None))
        self.ListCoordinatesButton_4.setText(_translate("Form", "Save", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PlayNow), _translate("Form", "Settings", None))
        self.ListCoordinatesButton.setText(_translate("Form", "List Coordinates", None))
        self.label_6.setText(_translate("Form", "Horizontal Position", None))
        self.label_7.setText(_translate("Form", "Vertical Position", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Get Position", None))
        self.label_36.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#eeeeee;\">Found a Bug? Send it to http://www.hacore.sf.net/ </span></p><p><span style=\" color:#eeeeee;\">We will appreciate your donation!, </span></p><p><span style=\" color:#eeeeee;\">Visit here to Donate</span></p></body></html>", None))
        self.UpgradeButton.setText(_translate("Form", "Update Now", None))
        self.SerialBox.setPlaceholderText(_translate("Form", "  License Number...", None))
        self.OrderButton.setText(_translate("Form", "Donate", None))
        self.SubscriptionStatus.setText(_translate("Form", "      You are Using a Free Version!", None))
        self.label.setText(_translate("Form", "Your Key", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ContactTab), _translate("Form", "Donate and Upgrade!", None))
        self.label_4.setText(_translate("Form", "Ultimate AMF Auto-Pilot - Licensed", None))
        self.footercoresec.setText(_translate("Form", "CoreSEC Software Development | M. Pequeras", None))
        self.CloseButton.setText(_translate("Form", "X", None))
        self.MinimizeButton.setText(_translate("Form", "-", None))
        self.label_2.setText(_translate("Form", "Message:", None))


    def moveMe(self):
        pass

######################## CreateAccountFunction Property #####################
    def CreateAccountFunction(self):
        import os
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.CAFFunction)
        box = self.textEdit
        box.append('Starting Browser...')
        self.timer.start(1000)


    def CAFFunction(self):
        import subprocess
        #subprocess.call('ext/reg/reg.exe')
        QtCore.QProcess.startDetached('ext/reg/reg.exe') ##PROCCALL
       # QtCore.QProcess.sta
######################## CreateAccountFunction Property #####################


    def StartThrFirst(self):
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.StartThreadsFunction)
        box = self.textEdit
        box.append('Starting Tnreads...')
        self.timer.start(1000)


    def StartThreadsFunction(self):
        import win32api
        import win32con
        import random
        import time
        sbox = self.textEdit
        def CheckKey(object):
            """ Lets Check Some Key! :)
            """
            openKey = open('lic','r+')
            readKey = openKey.read()

            if len(readKey) > 1:
                openKey.close()
                sbox.insertPlainText('Now Starting...')
                return True
            else:
                # Generate Static Lic
                genlic = 'MyAMFLicense'+str(random.randrange(13314,30752))
                hashlic = hash(str(genlic))
                wkey = open('lic','w+')  #### String Key
                wkey.write(str(genlic))

                reopen = open('lic','w+')
                sbox.insertPlainText('Key Generated!')
                reopen.write(str(hashlic))
                reopen.close()
                wkey.close()
                return True


        CheckKey(object)
        self.timert = QtCore.QTimer()
        self.timert.setSingleShot(False)
        self.timert.timeout.connect(self.FinalRun)
        self.timert.start(1000)

        ############## RUN NOW ########### :P


    def FinalRun(self):
        import time
        import win32con
        import win32api


        mbox = self.textEdit
        mxopen = self.MainXBox.toPlainText()
        myopen = self.MainYBox.toPlainText()



        pxopen = self.PointerXBox.toPlainText()
        pyopen = self.PointerYBox.toPlainText()

        cxopen = self.CloseXBox.toPlainText()
        cyopen = self.CloseYBox.toPlainText()
        speed = self.SliderValue.text()
        if mxopen == '':
            mbox.append('Error Please check the Value')
            return False
        if myopen == '':
            mbox.append('Error check the Value')
            return False

        if pxopen == '':
            mbox.append('Error check the Value')
            return False
        if pyopen == '':
            mbox.append('Error check the Value')
            return False
        if cxopen == '':
            mbox.append('Error Please check the Value')
            return False
        if cyopen == '':
            mbox.append('Error Please check the Value')
            return False
        ############ CLICK #### MAIN
        time.sleep(int(speed))
        win32api.SetCursorPos((int(mxopen),int(myopen)))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,int(mxopen),int(myopen),0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,int(mxopen),int(myopen),0,0)
        mbox.append('Click One Finished!\n')
        time.sleep(int(speed))

        ########### CLICK #### LIKE
        win32api.SetCursorPos((int(pxopen),int(pyopen)))

        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,int(pxopen),int(pyopen),0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,int(pxopen),int(pyopen),0,0)
        mbox.append('Click Two Finished!\n')
        ########### CLICK #### CLOSE
        time.sleep(int(speed))
        win32api.SetCursorPos((int(cxopen),int(cyopen)))
        win32api.SetCursorPos((793,23))
        win32api.SetCursorPos((int(cxopen),int(cyopen)))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,int(cxopen),int(cyopen),0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,int(cxopen),int(cyopen),0,0)


    def SaveMainPositionFunction(self):
        mx = self.MainXBox.toPlainText()
        my = self.MainYBox.toPlainText()
        mxo = open('main/mainx','w+')
        myo = open('main/mainy','w+')
        sbox = self.textEdit

        if len(mx) == 0:
            sbox.append('Ooops! Insufficient Characters at H Position!')
            return False
        if len(my) == 0:
            sbox.append('Ooops! Insufficient Characters at V Position!')
            return False
        else:
            mxo.write(str(mx))
            myo.write(str(my))
            sbox.append('Values Saved!!')
            myo.close()
            mxo.close()

    def SavePointerPositionFunction(self):
        """ Save Pointer X and Y """

        px = self.PointerXBox.toPlainText()
        py = self.PointerYBox.toPlainText()
        pxopen = open('pointer/pointerx','w+')
        pyopen = open('pointer/pointery','w+')
        #global mB
        mBox = self.textEdit
        if len(px) == 0:
            mBox.append('Ooops Please check your H Pointer')
            return False
        if len(py) == 0:
            mBox.append('Please check your V Pointer Value!')
            return False
        else:
            pxopen.write(str(px))
            pyopen.write(str(py))
            mBox.append('Pointers Saved')
            pxopen.close()
            pyopen.close()

    def SaveClosePositionFunction(self):
        px = self.CloseXBox.toPlainText()
        py = self.CloseYBox.toPlainText()
        pxopen = open('close/closex','w+')
        pyopen = open('close/closey','w+')
        #global mB
        mBox = self.textEdit
        if len(px) == 0:
            mBox.insertHtml('<b>Ooops Please check your H Pointer</b><br>')
            return False
        if len(py) == 0:
            mBox.insertHtml('<b>Please check your V Pointer Value!</b><br>')
            return False
        else:
            pxopen.write(str(px))
            pyopen.write(str(py))
            mBox.insertPlainText('Close Values Saved')
            pxopen.close()
            pyopen.close()




######################## Pos Generator Property #####################
    def ListGetPositionsFunction(self):
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.LCFunction)
        box = self.textEdit
        box.append('Capturing in 5 Seconds....')
        self.timer.start(5000)
    def LCFunction(self):
        import time
        import win32api
        self.timerx = QtCore.QTimer()
        box = self.textEdit
        xbox = self.GetPosX
        xboxc = self.GetPosX.toPlainText()
        ybox = self.GetPosY
        x,y = win32api.GetCursorPos()
        box.append('Captured: H-'+str(x)+' V-'+str(y))
        xbox.insertHtml('<b>'+str(x)+'</b>')
        ybox.insertHtml('<b>'+str(y)+'</b>')

######################## Pos Generator Property #####################



    def OrderNowFunction(self):
        import os
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.OrderF)
        box = self.textEdit
        box.append('Starting Browser...')
        self.timer.start(1000)

    def OrderF(self):
        import subprocess
        #subprocess.call('ext/reg/reg.exe')
        QtCore.QProcess.startDetached('ext/don/don.exe') ##PROCCALL




    def UpgradeNowFunction(self):
        sbox = self.textEdit
        sbox.append('You are a Licensed User!\nHave a nice day from CoreSEC Software Development')


    def GetMainFunction(self):
        import os
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.GetMainFunctionX)
        box = self.textEdit
        box.clear
        box.append('Capturing in 5 Seconds...')
        self.timer.start(1000)
    def GetMainFunctionX(self):
        import time
        import win32api
        mx = self.MainXBox.toPlainText()
        my = self.MainYBox.toPlainText()
        mxb = self.MainXBox
        myb = self.MainYBox
        mbox = self.textEdit
        gmbox = self.textEdit.toPlainText()
        if len(str(mx)) > 0:
            if len(str(gmbox)) > 0:
                mbox.clear()
            mbox.append('It\'s not Empty!!')
            return False
        if len(str(my)) > 0:
            if len(str(gmbox)) > 0:
                mbox.clear()
            mbox.append('It\'s not Empty!!')
            return False
        else:
            self.timerx = QtCore.QTimer()
            x,y = win32api.GetCursorPos()
            mbox.append('Captured! '+str(x)+' '+str(y))
            time.sleep(3)
            mxb.insertPlainText(str(x))
            myb.insertPlainText(str(y))


    def GetPointFunction(self):
        import os
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.GetPointerX)
        box = self.textEdit
        box.clear
        box.append('Capturing in 5 Seconds...')
        self.timer.start(1000)


    def GetPointerX(self):
        import time
        import win32api
        mx = self.PointerXBox.toPlainText()
        my = self.PointerYBox.toPlainText()
        mxb = self.PointerXBox
        myb = self.PointerYBox
        mbox = self.textEdit
        gmbox = self.textEdit.toPlainText()
        if len(str(mx)) > 0:
            if len(str(gmbox)) > 0:
                mbox.clear()
            mbox.append('It\'s not Empty!!')
            return False
        if len(str(my)) > 0:
            if len(str(gmbox)) > 0:
                mbox.clear()
            mbox.append('It\'s not Empty!!')
            return False
        else:
            self.timerx = QtCore.QTimer()
            x,y = win32api.GetCursorPos()
            mbox.append('Captured! '+str(x)+' '+str(y))
            time.sleep(3)
            mxb.insertPlainText(str(x))
            myb.insertPlainText(str(y))


    def GetCloseFunction(self):
        import os
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.GetCloseX)
        box = self.textEdit
        box.clear
        box.append('Capturing in 5 Seconds...')
        self.timer.start(1000)



    def GetCloseX(self):
        import time
        import win32api
        mx = self.CloseXBox.toPlainText()
        my = self.CloseYBox.toPlainText()
        mxb = self.CloseXBox
        myb = self.CloseYBox
        mbox = self.textEdit
        gmbox = self.textEdit.toPlainText()
        if len(str(mx)) > 0:
            if len(str(gmbox)) > 0:
                mbox.clear()
            mbox.append('It\'s not Empty!!')
            return False
        if len(str(my)) > 0:
            if len(str(gmbox)) > 0:
                mbox.clear()
            mbox.append('It\'s not Empty!!')
            return False
        else:
            self.timerx = QtCore.QTimer()
            x,y = win32api.GetCursorPos()
            mbox.append('Captured! '+str(x)+' '+str(y))
            time.sleep(3)
            mxb.insertPlainText(str(x))
            myb.insertPlainText(str(y))



    def showMinimized(self):
        Form.showMinimized()
    def closeFunction(self):
        Form.close()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    app.processEvents()
    Form = QtGui.QWidget()
    Form.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.CustomizeWindowHint)

    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()

    sys.exit(app.exec_())

