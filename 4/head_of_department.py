from specialization import *


class InvalidSymbolsInNameOfHeadOfDepartmentException(Exception):
    __symbols: str

    def __init__(self, symbols):
        self.__symbols = symbols

    def __get_symbols(self):
        return self.__symbols

    symbols = property(__get_symbols)


class HeadOfDepartment:
    __first_name: str
    __surname: str
    __last_name: str
    __specialization: Specialization

    def __init__(self, fname: str, lname: str, specialization: Specialization, sname=""):
        self.__specialization = specialization
        self.__first_name = fname
        self.__surname = sname
        self.__last_name = lname

        invalid_symbols = "+()1234567890"

        for c in fname:
            if c in invalid_symbols:
                raise InvalidSymbolsInNameOfHeadOfDepartmentException(fname)

        for c in lname:
            if c in invalid_symbols:
                raise InvalidSymbolsInNameOfHeadOfDepartmentException(lname)

        for c in sname:
            if c in invalid_symbols:
                raise InvalidSymbolsInNameOfHeadOfDepartmentException(sname)

    def __str__(self):
        return f"{self.__specialization} {self.__first_name} {self.__surname} {self.__last_name}"
