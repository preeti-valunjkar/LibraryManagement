from PyQt5 import QtWidgets, QtCore, QtGui, uic
from pathlib import Path
from destination import LIB_ROOT
from Book.book_data_class import BookData, Genre
from Book.book_data_manager import BookDataManager


class BookManagementController(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(BookManagementController, self).__init__(*args, **kwargs)
        uic.loadUi(str(Path(LIB_ROOT, 'Book/book_management.ui')), self)

        # setup genre combo box
        genre_list = []
        for genre in Genre:
            genre_list.append(genre.name)
        self.genre_comboBox.addItems(genre_list)
        self.genre_comboBox.setCurrentText("OTHER")

        # setup buttons
        self.add_btn.clicked.connect(self.add_btn_clicked)
        self.remove_btn.clicked.connect(self.remove_btn_clicked)

    def add_btn_clicked(self):
        book_data = BookDataManager()
        book_data.from_json()
        new_book = BookData(self.title_lineEdit.text(),
                            self.author_lineEdit.text(),
                            self.__to_genre(self.genre_comboBox.currentText()),
                            self.pubyear_spinBox.value(),
                            self.rating_doubleSpinBox.value(),
                            self.desc_lineEdit.text())
        if book_data.add_book(new_book):
            self.add_msg_lbl.setText("New book added to collection successfully")
            book_data.to_json()
        else:
            self.add_msg_lbl.setText("Book not added. Please check for spelling errors in the title.")

    def remove_btn_clicked(self):
        book_data = BookDataManager()
        book_data.from_json()
        if book_data.remove_book(self.title_remove_lineEdit.text()):
            self.remove_msg_lbl.setText("Book removed from collection successfully")
            book_data.to_json()
        else:
            self.remove_msg_lbl.setText("Book not removed. Please check for spelling errors in the title.")

    def __to_genre(self, genre):
        """
        This function is used to convert genre strings in json to
        objects of data type Genre.
        :parameter genre: Str representing a book's genre
        :return: Object of data type Genre
        """
        if genre == "ROMANCE":
            return Genre.ROMANCE
        elif genre == "FICTION":
            return Genre.FICTION
        elif genre == "NONFICTION":
            return Genre.NONFICTION
        elif genre == "HORROR":
            return Genre.HORROR
        elif genre == "MYSTERY":
            return Genre.MYSTERY
        elif genre == "SCIFI":
            return Genre.SCIFI
        elif genre == "ACTION":
            return Genre.ACTION
        elif genre == "POETRY":
            return Genre.POETRY
        elif genre == "COMEDY":
            return Genre.COMEDY
        elif genre == "FANTASY":
            return Genre.FANTASY
        elif genre == "AUTOBIOGRAPHY":
            return Genre.AUTOBIOGRAPHY
        else:
            return Genre.OTHER