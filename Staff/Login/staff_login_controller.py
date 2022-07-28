import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from Staff.Login.staff_login_ui import Ui_StaffLogin
from Staff.staff_main_window_controller import StaffMainWindowController
from Staff.staff_data_manager import StaffDataManager
from Staff.staff_data_classes import StaffLoginCredentials


class StaffLoginController(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(StaffLoginController, self).__init__(parent)
        self.ui = Ui_StaffLogin()
        self.ui.setupUi(self)

        # setup buttons
        self.ui.login_btn.clicked.connect(self.login_btn_clicked)

        # setup main window
        self.staff_main_window = StaffMainWindowController()

    def login_btn_clicked(self):
        staff_data = StaffDataManager()
        staff_data.from_json()
        uname = self.ui.username_lineEdit.text()
        upass = self.ui.password_lineEdit.text()
        if uname == "" or upass == "":
            self.ui.message_lbl.setText("Incorrect Username or Password")
        elif staff_data.validate_pass(StaffLoginCredentials(uname, upass)):
            self.close()
            self.staff_main_window.set_staff_name(staff_data.get_staff_name(uname))
            self.staff_main_window.show()
        else:
            self.ui.message_lbl.setText("Incorrect Username or Password")
