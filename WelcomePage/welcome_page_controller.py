from welcome_page_ui import Ui_WelcomePage
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from Staff.Login.staff_login_controller import StaffLoginController
from Member.member_main_window_controller import MemberMainWindowController


class WelcomePageController(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(WelcomePageController, self).__init__(parent)
        self.ui = Ui_WelcomePage()
        self.ui.setupUi(self)

        # setup buttons
        self.ui.staff_btn.clicked.connect(self.staff_btn_clicked)
        self.ui.member_btn.clicked.connect(self.member_btn_clicked)

        # setup subsequent screens
        self.staff_main_window = StaffLoginController()
        self.member_main_window = MemberMainWindowController()

    def staff_btn_clicked(self):
        self.staff_main_window.show()

    def member_btn_clicked(self):
        self.member_main_window.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = WelcomePageController()
    window.show()
    sys.exit(app.exec_())
