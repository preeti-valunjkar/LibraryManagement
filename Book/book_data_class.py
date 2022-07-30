from dataclasses import dataclass
from enum import Enum


class Genre(Enum):
    """
    Class Genre defines the different types of genres for books
    as an Enum.
    """
    ROMANCE = 1
    FICTION = 2
    NONFICTION = 3
    HORROR = 4
    MYSTERY = 5
    SCIFI = 6
    ACTION = 7
    POETRY = 8
    COMEDY = 9
    FANTASY = 10
    AUTOBIOGRAPHY = 11
    OTHER = 12


@dataclass
class Borrower:
    """
    Class Borrower defines useful data of a borrower such as name,
    contact details, issue and return date.
    """
    first_name: str = ""
    last_name: str = ""
    mobile_no: int = 0
    email: str = ""
    issue_date: str = ""
    return_date: str = ""


@dataclass
class BookData:
    """
    Class Book stores data of a book, including the details of a member
    who has issued the book.
    """
    title: str = ""
    author: str = ""
    genre: Genre = Genre.OTHER
    publish_year: int = 0
    rating: float = 0.0
    description: str = ""
    borrower: Borrower = Borrower()
