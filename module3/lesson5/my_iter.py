import random


class RandomIter:
    def __init__(self, limit):
        self.limit = limit
        self.__reload = limit
    def __iter__(self):
        self.limit = self.__reload
        return self

    def __next__(self):
        if self.limit == 0:
            raise StopIteration
        self.limit -= 1

        return random.randint(1, 100)


random_iterartor = RandomIter(10)

for i in RandomIter(10):
    print(i)

for i in random_iterartor:
    print(i)







# my_list = [1, 2, 3]
# for i in my_list:
#     print(i)

# iterator = iter(my_list)

# for i in iterator:
#     print(i)
#
# iterator = iter(my_list)
#
# for i in iterator:
#     print(i)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))


































