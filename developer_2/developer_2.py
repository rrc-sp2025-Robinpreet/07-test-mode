class Book:

    """
    Book:  Maintains the title and author attributes of a book.
 
    Attributes:
        _title (str): The title of the book.
        _author (str): The author of the book.

    """

    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def __str__(self):
        return f"Title: {self.__title}, Author {self.__author}"
