def palindrome(s):
    return s[::-1] == s


while True:
    s = input("Введите слово: ")
    if palindrome(s):
        print('True')
    else:
        print('False')
