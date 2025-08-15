class Circle:
    PI = 3.14159265359
    def __init__(self, r):
        self.r = r
    
    def area(self):
        return self.PI * pow(self.r,2)
    
    def perimeter(self):
        return 2 * self.PI * self.r

c1 = Circle(5)
print(f"Area for radius {c1.r} is : {c1.area()}")
print(f"Perimeter for radius {c1.r} is : {c1.perimeter()}")