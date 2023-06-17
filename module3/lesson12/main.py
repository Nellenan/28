# def factorial(number: int):
#     if number == 1:
#         return number
#     return number * factorial(number - 1)
#
#
# print(factorial(5))



import os

current_path = os.path.abspath(__file__)
parent_path = os.path.join(current_path, '..')
parent_parent_path = os.path.join(parent_path, '..')


def get_all_paths(path, filename=None):
    for i_file in os.listdir(path):
        new_path = os.path.join(path, i_file)
        if os.path.isdir(new_path) and i_file != 'venv':
            file = open(i_file, 'a', encoding='utf-8')
            file.close()
            print('Директория --->', new_path)
            get_all_paths(new_path, filename)
        else:
            if filename:
                with open(filename, 'a', encoding='utf-8') as f:
                    f.write(i_file)
            print('\t -', i_file)


get_all_paths(parent_parent_path)
