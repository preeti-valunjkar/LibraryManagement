from dataclasses import dataclass
from enum import Enum


class Genre(Enum):
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
    first_name: str = ""
    last_name: str = ""
    mobile_no: int = 0
    email: str = ""
    issue_date: str = ""
    return_date: str = ""


@dataclass
class BookData:
    title: str = ""
    author: str = ""
    genre: Genre = Genre.OTHER
    publish_year: int = 0
    borrower: Borrower = Borrower()

