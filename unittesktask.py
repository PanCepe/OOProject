class Employee :
    def __init__(self, age, name, salary, email, first_name="Alex", last_name="Lamar", gmail=None):
        self.age = age
        self.name = name
        self.salary = salary
        self.first_name = first_name
        self.last_name = last_name
        self.email = f"{first_name}{last_name}"@gmail.com


class Manager (Employee):
    def __init__(self, hair_colour, year_of_birth):
        self.hair_colour = hair_colour
        self.year_of_birth = year_of_birth


