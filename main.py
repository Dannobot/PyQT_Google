from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys


app = QApplication([])
win = uic.loadUi('main.ui')

win.show()
sys.exit(app.exit())