class Book:

    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def __str__(self):
        return f"Title: {self.__title}, Author {self.__author}"
