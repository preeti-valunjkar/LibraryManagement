import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from Staff.Login.staff_login_ui import Ui_StaffLogin
from Staff.staff_main_window_controller import StaffMainWindowController
from Staff.staff_data_manager import StaffDataManager
from Staff.staff_data_classes import StaffLoginCredentials
from pathlib import Path
from destination import LIB_CSS


class StaffLoginController(QtWidgets.QWidget):
    redirect_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(StaffLoginController, self).__init__(parent)
        self.ui = Ui_StaffLogin()
        self.ui.setupUi(self)

        # setup css
        main_css = str(Path(LIB_CSS, 'main_pages.css'))
        with open(main_css, "r") as fh:
            self.setStyleSheet(fh.read())

        # setup buttons
        self.ui.login_btn.clicked.connect(self.login_btn_clicked)
        self.ui.diff_user_btn.clicked.connect(self.redirect_btn_clicked)

        # setup main window
        self.staff_main_window = StaffMainWindowController()

        # setup signals
        self.staff_main_window.clear_credentials_signal.connect(self.clear_credentials)

    def login_btn_clicked(self):
        staff_data = StaffDataManager()
        staff_data.from_json()
        uname = self.ui.username_lineEdit.text()
        upass = self.ui.password_lineEdit.text()
        if uname == "" or upass == "":
            self.ui.message_lbl.setText("Incorrect Username or Password")
        elif staff_data.validate_pass(StaffLoginCredentials(uname, upass)):
            self.hide()
            self.staff_main_window.set_staff_name(staff_data.get_staff_name(uname))
            self.staff_main_window.show()
        else:
            self.ui.message_lbl.setText("Incorrect Username or Password")

    def redirect_btn_clicked(self):
        self.close()
        self.redirect_signal.emit()

    def clear_credentials(self):
        self.ui.username_lineEdit.clear()
        self.ui.password_lineEdit.clear()
        self.ui.message_lbl.clear()
        self.show()
