from Book.book_data_class import *
from destination import LIB_BOOK_DB
from pathlib import Path
from Book.book_data_class import BookData
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta


class BookDataManager:
    def __init__(self):
        self.__JSON_PATH = Path.joinpath(LIB_BOOK_DB, 'book_data.json')
        self.__book_data = {}

    def from_json(self):
        """
        Obtains information from the book_data.json file if such a file
        exists in the directory. If not, then creates the directory and
        adds an initial book to it.
        :return: None
        """
        if Path(self.__JSON_PATH).exists():
            with open(self.__JSON_PATH) as json_file:
                temp_dict = json.load(json_file)
                for book in temp_dict:
                    new_borrower = Borrower(temp_dict[book]['first_name'],
                                            temp_dict[book]['last_name'],
                                            temp_dict[book]['mobile_no'],
                                            temp_dict[book]['email'],
                                            temp_dict[book]['issue_date'],
                                            temp_dict[book]['return_date'])
                    new_book = BookData(temp_dict[book]['title'],
                                        temp_dict[book]['author'],
                                        self.__to_genre(temp_dict[book]['genre']),
                                        int(temp_dict[book]['publish_year']),
                                        new_borrower)
                    self.__book_data[book] = new_book
        else:
            self.create_temp_book()

    def to_json(self):
        """
        The to_json function must be called when the user wishes to write
        the changes made to the local variable book_data into the json file.
        This function makes changes to the book_data.json file.
        :return: None
        """
        temp_dict = dict()
        for book in self.__book_data:
            book_det = self.__book_data[book]
            temp_dict[book] = {'title': book_det.title,
                               'author': book_det.author,
                               'genre': book_det.genre.name,
                               'publish_year': book_det.publish_year,
                               'first_name': book_det.borrower.first_name,
                               'last_name': book_det.borrower.last_name,
                               'mobile_no': book_det.borrower.mobile_no,
                               'email': book_det.borrower.email,
                               'issue_date': book_det.borrower.issue_date,
                               'return_date': book_det.borrower.return_date}
        with open(self.__JSON_PATH, "w") as json_file:
            json.dump(temp_dict, json_file)

    def add_book(self, new_book):
        """
        Adds the given book to the book database. Changes are made only
        to the local variable book_data. Book may not be added if the
        book title already exists in database.
        :parameter new_book: Object of data type BookData
        :return: Bool (True if book can be added, False otherwise)
        """
        if not new_book.title in self.__book_data:
            self.__book_data[new_book.title] = new_book
            return True
        else:
            return False

    def remove_book(self, title):
        """
        Removes the given book from the database. Changes are made only
        to the local variable book_data.
        :parameter title: Str representing the book's title
        :return: Bool (True if removed successfully, False otherwise)
        """
        if title in self.__book_data:
            del self.__book_data[title]
            return True
        else:
            return False

    def issue_book(self, title, book_borrower):
        """
        Issues a book with the given title to a borrower. Changes are
        made only to the local variable book_data.
        :parameter title: Str representing the book's title
        :parameter book_borrower: Object of data type Borrower
        :return: Bool (True if successfully issued, False otherwise)
        """
        if title in self.__book_data:
            issue_date = datetime.today().strftime("%B %d, %Y")
            return_date = (datetime.today() + relativedelta(months=1)).strftime("%B %d, %Y")
            self.__book_data[title].borrower = Borrower(first_name=book_borrower.first_name,
                                                        last_name=book_borrower.last_name,
                                                        mobile_no=book_borrower.mobile_no,
                                                        email=book_borrower.email,
                                                        issue_date=issue_date,
                                                        return_date=return_date)
            return True
        else:
            return False

    def return_book(self, title):
        """
        Returns a book to the library by setting the borrower details
        to null. Changes are made only to the local variable book_data.
        :parameter title: Str representing book's title
        :return: Bool (True if successfully returned, False otherwise)
        """
        if title in self.__book_data:
            self.__book_data[title].borrower = Borrower()
            return True
        else:
            return False

    def create_temp_book(self):
        """
        Creates a temporary book entry when the file is newly created.
        Details are:
        Title- "newbook", Author- "newauthor"
        (All other information is blank)
        :return: None
        """
        self.__book_data["newbook"] = BookData("newbook", "newauthor")
        temp_dict = dict()
        temp_dict["newbook"] = {'title': self.__book_data["newbook"].title,
                                'author': self.__book_data["newbook"].author,
                                'genre': str(self.__book_data["newbook"].genre.name),
                                'publish_year': self.__book_data["newbook"].publish_year,
                                'first_name': self.__book_data["newbook"].borrower.first_name,
                                'last_name': self.__book_data["newbook"].borrower.last_name,
                                'mobile_no': self.__book_data["newbook"].borrower.mobile_no,
                                'email': self.__book_data["newbook"].borrower.email,
                                'issue_date': self.__book_data["newbook"].borrower.issue_date,
                                'return_date': self.__book_data["newbook"].borrower.return_date}
        if not Path(LIB_BOOK_DB).exists():
            Path.mkdir(LIB_BOOK_DB, exist_ok=True)
        with open(self.__JSON_PATH, "w") as json_file:
            json.dump(temp_dict, json_file)

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
