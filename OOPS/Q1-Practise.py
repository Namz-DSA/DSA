# 1st way
# class Student:
#     def __init__(self, name, eng_marks, sst_marks, sci_marks):
#         self.name = name
#         self.eng_marks = eng_marks
#         self.sst_marks = sst_marks
#         self.sci_marks = sci_marks
    
#     def avg_total(self):
#         return round((self.eng_marks + self.sst_marks + self.sci_marks)/3,2)
    

# s1 = Student("vapo", 93.8, 96.3, 35.7)

# print(s1.avg_total())


#2nd way

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def get_avg(self):
        sum = 0
        for mark in self.marks:
            sum += mark
        return round((sum/3),2)
    

s1 = Student("vapo", [93.8, 96.3, 35.7])

print(s1.get_avg())