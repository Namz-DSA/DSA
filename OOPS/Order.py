class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, order2):
        return self.price > order2.price

od1 = Order("Lays", 95)
od2 = Order("Masala Lays", 50)

print(od1 > od2)