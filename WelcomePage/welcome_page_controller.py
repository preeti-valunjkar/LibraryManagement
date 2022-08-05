from welcome_page_ui import Ui_WelcomePage
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from Staff.Login.staff_login_controller import StaffLoginController
from Member.member_main_window_controller import MemberMainWindowController
from destination import LIB_CSS
from pathlib import Path


class WelcomePageController(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(WelcomePageController, self).__init__(parent)
        self.ui = Ui_WelcomePage()
        self.ui.setupUi(self)

        # setup css
        main_css = str(Path(LIB_CSS, 'opening_pages.css'))
        with open(main_css, "r") as fh:
            self.setStyleSheet(fh.read())

        # setup buttons
        self.ui.staff_btn.clicked.connect(self.staff_btn_clicked)
        self.ui.member_btn.clicked.connect(self.member_btn_clicked)

        # setup subsequent screens
        self.staff_main_window = StaffLoginController()
        self.member_main_window = MemberMainWindowController()

        # setup redirect signals
        self.staff_main_window.redirect_signal.connect(self.reopen_signal)

    def staff_btn_clicked(self):
        self.hide()
        self.staff_main_window.show()

    def member_btn_clicked(self):
        self.hide()
        self.member_main_window.show()

    def reopen_signal(self):
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = WelcomePageController()
    window.show()
    sys.exit(app.exec_())
