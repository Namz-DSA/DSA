class Student:
    
    @staticmethod
    def college_name():
        print('ABC college')
    
    def __init__(self, name): 
        self.name = name
    
    def hello(self):
        return f"hello : {self.name}"

s1 = Student("Aabharan")

Student.college_name()      # Static method
print(s1.hello())           # Instance method
print(Student.hello(s1))    # Calling instance method via class
s1.college_name()