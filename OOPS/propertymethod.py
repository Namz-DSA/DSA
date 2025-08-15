class Marks:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chemistry = chem
        self.maths = math

    
    @property
    def percentage(self):
        return str((self.phy + self.chemistry + self.maths)/3)

m1 = Marks(98,99,97)
print(m1.percentage)

m1.phy = 93
print(m1.percentage)