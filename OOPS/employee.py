class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary
    
    def showDetails(self):
        print(f"The role is : {self.role}")
        print(f"The department is : {self.department}")
        print(f"The salary is : {self.salary}")
    
class Engineer(Employee):
    def __init__(self, name, age, role, department, salary):
        self.name = name
        self.age = age
        super().__init__(role, department, salary)
    
    def showDetails(self):
        print(f"My name is : {self.name} and I am {self.age} years old.")
        super().showDetails()

e1 = Engineer("Saurabh", 27, "Engineer", "DE", 100000)
e1.showDetails()