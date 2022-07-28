from Book.book_data_class import *
from destination import LIB_BOOK_DB
from pathlib import Path
import json


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
                    new_book = BookData(temp_dict[book]['title'],
                                        temp_dict[book]['author'],
                                        temp_dict[book]['genre'],
                                        temp_dict[book]['publish_year'])
                    new_book.Borrower(temp_dict[book]['first_name'],
                                      temp_dict[book]['last_name'],
                                      temp_dict[book]['mobile_no'],
                                      temp_dict[book]['email'],
                                      temp_dict[book]['issue_date'],
                                      temp_dict[book]['return_date'])
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
                               'genre': str(book_det.genre.name),
                               'publish_year': book_det.publish_year,
                               'first_name': book_det.Borrower().first_name,
                               'last_name': book_det.Borrower().last_name,
                               'mobile_no': book_det.Borrower().mobile_no,
                               'email': book_det.Borrower().email,
                               'issue_date': book_det.Borrower().issue_date,
                               'return_date': book_det.Borrower().return_date}
        with open(self.__JSON_PATH, "w") as json_file:
            json.dump(temp_dict, json_file)

    def create_temp_book(self):
        """
        Creates a temporary book entry when the file is newly created.
        Details are:
        Title- "newbook", Author- "newauthor"
        (All other information is blank)
        :return: None
        """
        self.__book_data["newbook"] = BookData("newbook", "newauthor")
        self.__book_data["newbook"].Borrower()
        temp_dict = dict()
        temp_dict["newbook"] = {'title': self.__book_data["newbook"].title,
                                'author': self.__book_data["newbook"].author,
                                'genre': str(self.__book_data["newbook"].genre.name),
                                'publish_year': self.__book_data["newbook"].publish_year,
                                'first_name': self.__book_data["newbook"].Borrower().first_name,
                                'last_name': self.__book_data["newbook"].Borrower().last_name,
                                'mobile_no': self.__book_data["newbook"].Borrower().mobile_no,
                                'email': self.__book_data["newbook"].Borrower().email,
                                'issue_date': self.__book_data["newbook"].Borrower().issue_date,
                                'return_date': self.__book_data["newbook"].Borrower().return_date}
        if not Path(LIB_BOOK_DB).exists():
            Path.mkdir(LIB_BOOK_DB, exist_ok=True)
        with open(self.__JSON_PATH, "w") as json_file:
            json.dump(temp_dict, json_file)


if __name__ == "__main__":
    book_data = BookDataManager()
    book_data.from_json()
