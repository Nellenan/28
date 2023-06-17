name = 'Давид'
salary = 200

print(f"У {name} зарплата составляет {salary} рублей.")


employee = {
    'name': 'Вадим',
    'salary': '199',
    'age': '16'
}

print(f'У {employee["name"]} зарплата составляет {employee["salary"]}')

employees_list = [
    {
        "name": 'Вадим',
        'salary': '199'
    },
    {
        "name": 'Сева',
        "salary": '200_000'
    },
    {
        'name': 'Данил',
        'salary': '244'
    }
]

for employee in employees_list:
    print(f'У {employee["name"]} зарплата составляет {employee["salary"]} рублей')


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


employee = Employee(name='Кто-то', salary=120)
print(f'У {employee.name} зарплата составляет {employee.salary}')
