# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'A:\Documents\Python Programs\Cards_Downloading\GUI Source\convert\MainGUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("YGOPics Downloader")
        MainWindow.resize(807, 355)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(100, 10, 591, 71))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(36)
        self.title.setFont(font)
        self.title.setAutoFillBackground(True)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.downloadBtn = QtWidgets.QPushButton(self.centralwidget)
        self.downloadBtn.setGeometry(QtCore.QRect(140, 100, 381, 111))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.downloadBtn.setFont(font)
        self.downloadBtn.setObjectName("downloadBtn")
        self.psBtn = QtWidgets.QPushButton(self.centralwidget)
        self.psBtn.setEnabled(True)
        self.psBtn.setGeometry(QtCore.QRect(540, 100, 111, 111))
        #icon = QtGui.QIcon()
        #icon.addPixmap(QtGui.QPixmap("pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #icon.addPixmap(QtGui.QPixmap("play.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        #self.psBtn.setIcon(icon)
        #self.psBtn.setIconSize(QtCore.QSize(16, 16))
        self.psBtn.setText("Cancel")
        self.psBtn.setCheckable(False)
        self.psBtn.setAutoDefault(False)
        self.psBtn.setDefault(False)
        self.psBtn.setFlat(False)
        self.psBtn.setObjectName("psBtn")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(40, 230, 731, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.progressBar.setFont(font)
        self.progressBar.setMouseTracking(False)
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressLabel = QtWidgets.QLabel(self.centralwidget)
        self.progressLabel.setGeometry(QtCore.QRect(40, 280, 621, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.progressLabel.setFont(font)
        self.progressLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.progressLabel.setObjectName("progressLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 807, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "YGOPics Downloader"))
        self.downloadBtn.setText(_translate("MainWindow", "Download Now !"))
        self.progressLabel.setText(_translate("MainWindow", "Standby..."))
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

