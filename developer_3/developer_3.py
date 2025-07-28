class Car:
    def __init__(self, make, model):
        self.__make = make
        self.__model = model

    def __str__(self):
        return f"Make: {self.__make}, Model: {self.__model}"
