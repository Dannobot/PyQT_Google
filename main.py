from PyQt5 import QtWidgets, QtGui, QtCore
from mainUI import Ui_MainWindow
import sys

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label.setText("None")
        self.ui.button.clicked.connect(self.btnClick)
    def btnClick(self):
        lable_text = self.ui.label.text()
        if lable_text == "None":
            self.ui.label.setText("Clicked")
        else:
            self.ui.label.setText("None")


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    app_main = MyWindow()
    app_main.show()
    sys.exit(app.exec_())