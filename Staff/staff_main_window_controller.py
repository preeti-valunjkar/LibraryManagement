import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from Staff.staff_main_window_ui import Ui_StaffMainWindow
from Staff.staff_management_controller import StaffManagementController


class StaffMainWindowController(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(StaffMainWindowController, self).__init__(parent)
        self.ui = Ui_StaffMainWindow()
        self.ui.setupUi(self)

        self.manage_staff = StaffManagementController()
        self.ui.stackedWidget.addWidget(self.manage_staff)

        # setup buttons
        self.ui.manage_staff_btn.clicked.connect(self.manage_staff_btn_clicked)

    def manage_staff_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def set_staff_name(self, staff_name):
        self.ui.welcome_msg_lbl.setText("Welcome, " + staff_name)
