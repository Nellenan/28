# class Item:
#     def __init__(self, price, brand):
#         self.price = price
#         self.brand = brand
#
#     def __repr__(self):
#         return self.brand
#
#
# items_list = [
#     Item(1000, 'Apple'),
#     Item(1200, 'Apple'),
#     Item(900, 'Samsung'),
#     Item(700, "Samsung"),
#     Item(600, 'Xiaomi')
# ]
#
# result = list(filter(lambda x: x.brand == 'Samsung', items_list))
# print(result)





names_list = ['данил', 'артём', 'никита', 'влад']
result = [i.capitalize() for i in names_list]
print(result)



