# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: black;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #說話按鈕
        self.speackbtn = QtWidgets.QPushButton(self.centralwidget)
        self.speackbtn.setGeometry(QtCore.QRect(50, 460, 181, 71))
        self.speackbtn.setStyleSheet("background-color: white;")
        self.speackbtn.setObjectName("speackbtn")
        #動畫區域
        self.graphicsView = QtWidgets.QLabel(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 10, 1200, 192))
        self.graphicsView.setObjectName("graphicsView")
        self.movie = QMovie("uisound.gif")
        self.graphicsView.setMovie(self.movie)
        self.movie.start()
        self.graphicsView.setVisible(False)
        #使用者輸入
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(240, 460, 351, 71))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("background-color: white;")
        #輸入按鈕
        self.enterbtn = QtWidgets.QPushButton(self.centralwidget)
        self.enterbtn.setGeometry(QtCore.QRect(610, 460, 131, 71))
        self.enterbtn.setStyleSheet("background-color: white;")
        self.enterbtn.setObjectName("enterbtn")
        #結果區域
        self.resulttext = QtWidgets.QTextEdit(self.centralwidget)
        self.resulttext.setGeometry(QtCore.QRect(10, 220, 781, 221))
        self.resulttext.setReadOnly(True)
        self.resulttext.setObjectName("resulttext")
        self.resulttext.setStyleSheet("background-color: white;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.speackbtn.setText(_translate("MainWindow", "Speack"))
        self.enterbtn.setText(_translate("MainWindow", "輸入"))

    def playGif(self):
        self.graphicsView.setVisible(True)


    def hideGif(self):
        self.graphicsView.setVisible(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
