import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import QtWidgets
from Gui6 import Ui_MainWindow
from GuiForm6 import Ui_Form
                                      
class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        #Khai Bao Nut Mo Tab Moi
        self.uic.pushButton_2.clicked.connect(self.OpenTab)
    def OpenTab(self):  #Open Tab 2
        #Lênh mở màn hình thứ2
        self.main_win1 = QtWidgets.QMainWindow()
        self.uic1 = Ui_Form()
        self.uic1.setupUi(self.main_win1)
        self.main_win1.show()


    def show(self):
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())