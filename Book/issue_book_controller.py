from PyQt5 import QtWidgets, QtCore, QtGui, uic
from pathlib import Path
from destination import LIB_ROOT
from Book.book_data_class import Borrower
from Book.book_data_manager import BookDataManager
from datetime import datetime
from dateutil.relativedelta import relativedelta


class IssueBookController(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(IssueBookController, self).__init__(*args, **kwargs)
        uic.loadUi(str(Path(LIB_ROOT, 'Book/issue_book.ui')), self)

        # setup buttons
        self.issue_btn.clicked.connect(self.issue_btn_clicked)

    def issue_btn_clicked(self):
        book_data = BookDataManager()
        book_data.from_json()
        book_borrower = Borrower(self.fname_lineEdit.text(),
                                 self.lname_lineEdit.text(),
                                 int(self.mobno_lineEdit.text()),
                                 self.email_lineEdit.text())
        if book_data.issue_book(self.title_lineEdit.text(), book_borrower):
            book_data.to_json()
            self.issue_msg_lbl.setText("Book issued to borrower successfully")
            return_date_lbl = QtWidgets.QLabel()
            return_date_lbl.setText("Return Date: ")
            return_date = QtWidgets.QLabel()
            return_date.setText((datetime.today() + relativedelta(months=1)).strftime("%B %d, %Y"))
            self.horizontalLayout.addWidget(return_date_lbl)
            self.horizontalLayout.addWidget(return_date)
        else:
            self.issue_msg_lbl.setText("Book not issues. Please check book title for spelling errors.")
