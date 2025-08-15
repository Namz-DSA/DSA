"""
A complex number is of the form ai + bj
functions like __add__ / __init__ / __sub__ are all called dunder functions
"""

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showcomplexNo(self):
        print(self.real, "i +", self.img, "j")
    
    def add(self, num2):
        newreal = self.real + num2.real
        newimg = self.img + num2.img
        return Complex(newreal,newimg)

c1 = Complex(1, 2)
c1.showcomplexNo()

c2 = Complex(3,5)
c2.showcomplexNo()

added_no = c1.add(c2)
added_no.showcomplexNo()



class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showcomplexNo(self):
        print(self.real, "i +", self.img, "j")
    
    def __add__(self, num2):
        newreal = self.real + num2.real
        newimg = self.img + num2.img
        return Complex(newreal,newimg)


c1 = Complex(1, 2)
c2 = Complex(3, 5)

c3 = c1 + c2