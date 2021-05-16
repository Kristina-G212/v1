from specialization import *


class HospitalDepartment:
    __name: str
    __specialization: Specialization
    __wards: int

    def __init__(self, name_of_department: str, specialization_of_department: Specialization, wards_of_department=1):
        self.__name = name_of_department
        self.__specialization = specialization_of_department
        self.__wards = wards_of_department

    def __str__(self):
        return f"{self.__name}, {self.__specialization}, wards: {self.__wards}"
