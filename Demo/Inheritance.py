class Person:
    def __init__(self, name, birhtdate):
        self.name = name
        self.birhtdate = birhtdate
        self.surname = ''

    def full_name(self):
        return f'{self.name} {self.surname}'


class Employee(Person):
    def __init__(self, name, birthdate, salary):
        super().__init__(name, birthdate)
        self.salary = salary

    def full_name(self):
        return f'{super().full_name()} {self.salary}'

class Client(Person):
    def __init__(self, name, birthdate, account_number):
        super().__init__(name, birthdate)
        self.account_number = account_number




employee = Employee('test', '2000-01-01', 1000)
