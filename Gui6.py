# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gui6.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(487, 210)
        MainWindow.setStyleSheet("background-color:rgb(56, 56, 56)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.AllTab = QtWidgets.QTabWidget(self.centralwidget)
        self.AllTab.setGeometry(QtCore.QRect(0, 10, 371, 161))
        self.AllTab.setFocusPolicy(QtCore.Qt.NoFocus)
        self.AllTab.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.AllTab.setStyleSheet("background-color:rgb(3, 3, 3)")
        self.AllTab.setObjectName("AllTab")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.AllTab.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(0, 0, 361, 131))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../Image/Kali.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.AllTab.addTab(self.tab_2, "")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 30, 75, 23))
        self.pushButton_2.setStyleSheet("background-color:rgb(254, 238, 255)")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 487, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.AllTab.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.AllTab.setTabText(self.AllTab.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.AllTab.setTabText(self.AllTab.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.pushButton_2.setText(_translate("MainWindow", "Open"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())