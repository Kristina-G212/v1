class EmptySpecialization(Exception):
    pass


class InvalidSpecializationException(Exception):
    __specialization: str

    def __init__(self, specialization):
        self.__specialization = specialization

    def __get_specialization(self):
        return self.__specialization

    name = property(__get_specialization)


class Specialization:
    __name: str

    def __init__(self, specialization: str):
        if specialization == "":
            raise EmptySpecialization()

        invalid_symbols = "+()-1234567890"

        for c in invalid_symbols:
            if c in specialization:
                raise InvalidSpecializationException(specialization)

        self.__name = specialization

    def __str__(self):
        return self.__name
