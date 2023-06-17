# 1

# def my_func(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
#
# # my_func(10, 20, 30, 'Привет мир!', a=241)
# my_func(a=109, 20)


# 2
# age = 18
# criminal_record = False

# if age >= 18:
#     is_allow = 'Можно'
# else:
#     is_allow = 'Нельзя'
#
# print(is_allow)

# is_allow = 'Можно' if age >= 18 or not criminal_record else 'Нельзя'
#
# print(is_allow)

# 3

# a = True
# b = False
#
# c = a or b
#
# print(c)


# 4


# my_list =[]
#
# for i in range(2000):
#     if i % 5 == 0:
#         my_list.append(i)
#
# print(my_list)

# my_list = [i for i in range(1000) if i % 5 == 0]
my_list = [i if i % 5 == 0 else i * 5 for i in range(1000) if i % 3 == 0]
print(my_list)


# 5

# my_dict = {i: len(i) for i in ['первый', 'второй', 'третий'] if len(i) != 6}
# print(my_dict)


# 6

# my_list_1 = [1, 2]
# my_list_2 = [1, 2]
#
# a = 10
# b = 10
#
# print(my_list_1 == my_list_2)
# print(my_list_1 is my_list_2)
# print(a is b)

# 7


# my_tuple = (1, 2, 3, 4)
# print(my_tuple)
#
# element = my_tuple[2]
# print(element)
#
# my_dict = {
#     ('Сергеев', 'Никита'): '+79503149145'}
#
# print(my_dict)
# print(sorted(my_tuple))
#
# my_list = [1, 2, 3, 4]
# print(tuple(my_list))

# my_tuple = tuple(i for i in range(0, 1000))
# print(my_tuple)



















