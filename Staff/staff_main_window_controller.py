import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from Staff.staff_main_window_ui import Ui_StaffMainWindow
from Staff.staff_management_controller import StaffManagementController
from Book.book_management_controller import BookManagementController
from Book.issue_book_controller import IssueBookController
from Book.return_book_controller import ReturnBookController


class StaffMainWindowController(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(StaffMainWindowController, self).__init__(parent)
        self.ui = Ui_StaffMainWindow()
        self.ui.setupUi(self)

        self.manage_staff = StaffManagementController()
        self.ui.stackedWidget.addWidget(self.manage_staff)
        self.manage_books = BookManagementController()
        self.ui.stackedWidget.addWidget(self.manage_books)
        self.issue_book = IssueBookController()
        self.ui.stackedWidget.addWidget(self.issue_book)
        self.return_book = ReturnBookController()
        self.ui.stackedWidget.addWidget(self.return_book)

        # setup buttons
        self.ui.manage_staff_btn.clicked.connect(self.manage_staff_btn_clicked)
        self.ui.manage_books_btn.clicked.connect(self.manage_books_btn_clicked)
        self.ui.issue_book_btn.clicked.connect(self.issue_book_btn_clicked)
        self.ui.return_book_btn.clicked.connect(self.return_book_btn_clicked)

    def manage_staff_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def manage_books_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def issue_book_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def return_book_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def set_staff_name(self, staff_name):
        self.ui.welcome_msg_lbl.setText("Welcome, " + staff_name)
