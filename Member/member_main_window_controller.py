from Member.member_main_window_ui import Ui_MainWindow
import sys
from PyQt5 import QtWidgets, QtCore, QtGui


class MemberMainWindowController(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MemberMainWindowController, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
