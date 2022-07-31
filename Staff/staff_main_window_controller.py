import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from Staff.staff_main_window_ui import Ui_StaffMainWindow
from Staff.staff_management_controller import StaffManagementController
from Book.book_management_controller import BookManagementController
from Book.issue_book_controller import IssueBookController
from Book.return_book_controller import ReturnBookController
from Staff.staff_profile_controller import StaffProfileController


class StaffMainWindowController(QtWidgets.QMainWindow):
    clear_credentials_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(StaffMainWindowController, self).__init__(parent)
        self.ui = Ui_StaffMainWindow()
        self.ui.setupUi(self)
        self.staff_name = ""

        self.manage_staff = StaffManagementController()
        self.ui.stackedWidget.addWidget(self.manage_staff)
        self.manage_books = BookManagementController()
        self.ui.stackedWidget.addWidget(self.manage_books)
        self.issue_book = IssueBookController()
        self.ui.stackedWidget.addWidget(self.issue_book)
        self.return_book = ReturnBookController()
        self.ui.stackedWidget.addWidget(self.return_book)
        self.staff_profile = StaffProfileController()
        self.ui.stackedWidget.addWidget(self.staff_profile)

        # setup buttons
        self.ui.manage_staff_btn.clicked.connect(self.manage_staff_btn_clicked)
        self.ui.manage_books_btn.clicked.connect(self.manage_books_btn_clicked)
        self.ui.issue_book_btn.clicked.connect(self.issue_book_btn_clicked)
        self.ui.return_book_btn.clicked.connect(self.return_book_btn_clicked)

        # setup triggers
        self.ui.actionLogout.triggered.connect(self.logout_action_triggered)
        self.ui.actionProfile.triggered.connect(self.profile_action_triggered)

    def manage_staff_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def manage_books_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def issue_book_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def return_book_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def logout_action_triggered(self):
        self.clear_credentials_signal.emit()
        self.close()

    def profile_action_triggered(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        self.staff_profile.setup(self.staff_name)

    def set_staff_name(self, staff_name):
        self.staff_name = staff_name
        self.ui.welcome_msg_lbl.setText("Welcome, " + staff_name)
