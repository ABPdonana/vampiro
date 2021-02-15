class Item:
    def __init__(self, nombre, usable):
        self.__nombre = nombre
        self.__usable = usable
    def nombre(self):
        return self.__nombre
    def usable(self):
        return self.__usable
    def set_objeto(self, nombre):
        self.__nombre = nombre
