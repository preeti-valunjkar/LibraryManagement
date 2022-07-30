from PyQt5 import QtWidgets, QtCore, QtGui, uic
from pathlib import Path
from destination import LIB_ROOT
from Book.book_data_manager import BookDataManager


class ReturnBookController(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(ReturnBookController, self).__init__(*args, **kwargs)
        uic.loadUi(str(Path(LIB_ROOT, 'Book/return_book.ui')), self)

        # setup buttons
        self.return_btn.clicked.connect(self.return_btn_clicked)

    def return_btn_clicked(self):
        book_data = BookDataManager()
        book_data.from_json()
        if book_data.return_book(self.title_lineEdit.text()):
            book_data.to_json()
            self.return_msg_lbl.setText("Book returned successfully")
        else:
            self.return_msg_lbl.setText("Book not returned. Please check book title for spelling errors.")
