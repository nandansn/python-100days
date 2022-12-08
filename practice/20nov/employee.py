from person import Person

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name,age)
        self.salary = salary

    def getSalary(self):
        return self.salary






      