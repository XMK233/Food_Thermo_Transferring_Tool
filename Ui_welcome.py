# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Users\XMK1\AnacondaProjects\animals\welcome.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WelcomWindow(object):
    def setupUi(self, WelcomWindow):
        WelcomWindow.setObjectName("WelcomWindow")
        WelcomWindow.resize(966, 657)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        WelcomWindow.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(WelcomWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.welcomePic = QtWidgets.QLabel(self.centralWidget)
        self.welcomePic.setGeometry(QtCore.QRect(0, 0, 971, 671))
        self.welcomePic.setText("")
        self.welcomePic.setPixmap(QtGui.QPixmap("新欢迎.jpg"))
        self.welcomePic.setScaledContents(True)
        self.welcomePic.setObjectName("welcomePic")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(420, 500, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        WelcomWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(WelcomWindow)
        QtCore.QMetaObject.connectSlotsByName(WelcomWindow)

    def retranslateUi(self, WelcomWindow):
        _translate = QtCore.QCoreApplication.translate
        WelcomWindow.setWindowTitle(_translate("WelcomWindow", "食物热量换算工具"))
        self.pushButton.setText(_translate("WelcomWindow", "进入系统"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WelcomWindow = QtWidgets.QMainWindow()
    ui = Ui_WelcomWindow()
    ui.setupUi(WelcomWindow)
    WelcomWindow.show()
    sys.exit(app.exec_())

