class Student:
    name = "Anonymous"

    @classmethod
    def change_name(cls, name):
        cls.name = name
    

print(Student.name)
Student.change_name("Chirag")
print(Student.name)


class Student:
    name = "Anonymous"
    
    def change_name(self, name):
        Student.name = name

s1 = Student()
print(s1.name)

s1.change_name("Shilpa")
print(s1.name)


class Student:
    name = "Anonymous"
    
    def change_name(self, name):
        self.__class__.name = name


s1 = Student()
print(s1.name)

s1.change_name("Anurag")
print(s1.name)