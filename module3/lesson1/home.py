class Employee:
    def __init__(self, name, salary, on_vacation, is_good_employee):
        self.name = name
        self.salary = salary
        self.on_vacation = on_vacation
        self.is_good_employee = is_good_employee


employees_list = []
bad_employees_list = []

employees_list.append(Employee(name='Вася', salary=100000, on_vacation=True, is_good_employee=True))
employees_list.append(Employee(name='Коля', salary=200010, on_vacation=False, is_good_employee=True))
employees_list.append(Employee(name='Данил', salary=255000, on_vacation=False, is_good_employee=True))
employees_list.append(Employee(name='Миша', salary=99999, on_vacation=False, is_good_employee=False))
employees_list.append(Employee(name='Рома', salary=100000, on_vacation=True, is_good_employee=True))


print('Список всех сотрудников')
print(employees_list[0].name)
print(employees_list[1].name)
print(employees_list[2].name)
print(employees_list[3].name)
print(employees_list[4].name)


for employee in employees_list:
    if employee.is_good_employee == False:
        bad_employees_list.append(employee)
        employees_list.remove(employee)


print('Список хороших сотрудников')
print(employees_list[0].name)
print(employees_list[1].name)
print(employees_list[2].name)
print(employees_list[3].name)


print('Список плохих сотрудников')
print(bad_employees_list[0].name)




# print(f"Работник {employee.name}")
# print(f'Зарплата составляет {employee.salary} рублей')
#
# if employee.on_vacation == True:
#     print('Сотрудник находится в отпуске')
# else:
#     print('Сотрудник не в отпуске')

