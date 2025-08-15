# class Student:
#     name = 'Gigi'

# s1 = Student()
# print(s1)
# print(s1.name)

# class Student:
#     def __init__(self):
#         print('Adding name to the database...')
    
#     def __init__(self, fullname, total_marks):
#         self.name = fullname
#         self.marks = total_marks
    
# s1 = Student('Gigi', 97)
# s2 = Student('Hadid', 100)

# print(s1.name, s1.marks)
# print(s2.name, s2.marks)


# class Student:
#     college_name = 'AIT College'
#     def __init__(self):
#         print('Adding name to the database...')
    
#     def __init__(self, fullname, total_marks):
#         self.name = fullname
#         self.marks = total_marks
    
# s1 = Student('Gigi', 97)
# print(s1.name, s1.marks, Student.college_name, s1.college_name)
# print(Student.college_name)


class Student:
    college_name = 'AIT College'
    def __init__(self):
        print('Adding name to the database...')
    
    def __init__(self, fullname, total_marks):
        self.name = fullname
        self.marks = total_marks
    
    def hello(self):
        print(f'Hello - {self.name}')
    
    def get_mark(self):
        return self.marks
    
s1 = Student('Gigi', 97)
print(s1.hello())
print(s1.get_mark())
s1.hello()