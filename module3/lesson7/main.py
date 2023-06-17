class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __add__(self, other):
        if isinstance(other, Item):
            return self.price + other.price
        elif isinstance(other, int):
            return self.price + other

    def __radd__(self, other):
        if isinstance(other, Item):
            return self.price + other.price
        elif isinstance(other, int):
            return self.price + other

    def __sub__(self, other):
        if isinstance(other, Item):
            return self.price - other.price
        elif isinstance(other, int):
            return self.price - other

    def __rsub__(self, other):
        if isinstance(other, Item):
            return self.price - other.price
        elif isinstance(other, int):
            return self.price - other

    def __mul__(self, other):
        if isinstance(other, Item):
            return self.price * other.price
        elif isinstance(other, int):
            return self.price * other

    def __rmul__(self, other):
        if isinstance(other, Item):
            return self.price * other.price
        elif isinstance(other, int):
            return self.price * other

    def __floordiv__(self, other):
        if isinstance(other, Item):
            return self.price // other.price
        elif isinstance(other, int):
            return self.price // other

    def __rfloordiv__(self, other):
        if isinstance(other, Item):
            return self.price // other.price
        elif isinstance(other, int):
            return self.price // other


item1 = Item('Процессор ', 100_000, 0.2)
item2 = Item('Видеокарта', 200_000, 0.9)
item3 = Item('Оперативка', 10_000, 0.5)

# total_sum = item1 + 1000
# total_sum = 1000 + item1
operation_1 = item1 + item2 + item3
operation_2 = item2 - item1 - item3
operation_3 = item1 * item3 * item2
operation_4 = item2 // item1 // item3

print(operation_1)
print(operation_2)
print(operation_3)
print(operation_4)