from head_physician import *
from hospital_department import *


class Hospital:
    __name: str
    __head_physician: HeadPhysician
    __departments: HospitalDepartment

    def __init__(self, name: str, name_of_head_physician: HeadPhysician, departments: HospitalDepartment):
        self.__name = name
        self.__head_physician = name_of_head_physician
        self.__departments = departments

    def __str__(self):
        a = []
        res = f"Hospital {self.__name}, The head physician is {self.__head_physician}"
        for department in self.__departments:
            a.append(str(department))
            #print(department)

        return res + "\n" + ";\n".join(map(str, set(a)))
