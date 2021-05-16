from hospital import *
from hospital_department import *
from head_physician import *
from head_of_department import *
from specialization import *

try:
    name_of_hospital = "Princeton–Plainsboro"
    head_physician = HeadPhysician("Lisa", "Cuddy")
    specialization = Specialization("Diagnostics")
    specialization1 = Specialization("Surgery")
    specialization2 = Specialization("Oncology")
    specialization3 = Specialization("Traumatology")
    specialization4 = Specialization("Neurology")
    head_of_department = HeadOfDepartment("Gregory", "House", specialization)
    hospital_departments = [HospitalDepartment("Department of diagnostics", specialization, 1),
                            HospitalDepartment("Surgery department", specialization1, 3),
                            HospitalDepartment("Oncology department", specialization2, 2),
                            HospitalDepartment("Traumatology department", specialization3, 3),
                            HospitalDepartment("Department of neurology ", specialization4, 3)]
    h = Hospital(name_of_hospital, head_physician, hospital_departments)
except InvalidSymbolsInNameOfHeadPhysicianException as err:
    print("Недопустимые символы в ФИО", err.symbols)
except InvalidSymbolsInNameOfHeadOfDepartmentException as err:
    print("Недопустимые символы в ФИО", err.symbols)
except InvalidSpecializationException as err:
    print("Недопустимые символы в специализации", err.name)
except EmptySpecialization as err:
    print("Нет специализации")
else:
    print(h)
