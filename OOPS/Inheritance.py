#Multi-Level Inheritance
class Car:
    @staticmethod
    def start():
        print("Car Started...")
    
    @staticmethod
    def stop():
        print("Car Stopped.")
    
class ToyotaCar(Car):
    def __init__(self, Type):
        self.Type = Type

class Fortuner(ToyotaCar):
    def __init__(self, color, Type):
        super().__init__(Type)
        self.color = color

f1 = Fortuner("Black","Petrol")

print(f1.color)
print(f1.Type)
f1.start()
f1.stop()


#Multiple Inheritance

class A:
    varA = "Hello, class A"

class B:
    varB = "Hello, class B"

class C (A,B):
    varC = "Hello, class C"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)



class Car:
    def start(self):
        print("Car is starting...")

    def stop(self):
        print("Car is stopping...")

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self, brand, color):
        super().__init__(brand)
        self.color = color

    def start(self):
        super().start()  # Call Car's version first
        print(f"{self.brand} Fortuner in {self.color} color is now in Sport Mode 🚀")

    def stop(self):
        print("Activating brake assist...")
        super().stop()


f1 = Fortuner("Toyota", "Black")
f1.start()
f1.stop()