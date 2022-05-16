class Pilot:

    increase = 1.10

    def __init__(self, name, lastname, salary):
        self.name = name
        self.lastname = lastname
        self.salary = salary

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.name, self.lastname)

    @property
    def full_name(self):
        return '{} {}'.format(self.name, self.lastname)

    def increase_salary(self):
        self.salary += float(self.salary * self.increase)
        return self.salary