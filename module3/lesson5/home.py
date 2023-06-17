# 1

# class MyFIle:
#     def __init__(self, file_name, mode, encoding = 'utf-8'):
#         self.file_name = file_name
#         self.mode = mode
#         self.encoding = encoding
#
#     def __enter__(self):
#         self.file = open(self.file_name, self.mode, encoding=self.encoding)
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
#
#
# # Записать в файл
# with MyFIle('file.txt', 'w', encoding='utf-8') as file:
#     content = file.write('Hello, World!')
#
#
# # Вывести в консоль из файла
# with MyFIle('file.txt', 'r', encoding='utf-8') as file:
#     content = file.read()
#     print(content)



# 2


class InfinityIterator:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        return self.start - 1


my_iterator = InfinityIterator(0)

for i in my_iterator:
    print(i)



