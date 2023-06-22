print("Приветствую! Это программа создана для проверки слова  на палиндром.")

while True:
    s = input("Введите слово:")


    def palindrome(s):
        h = len(s) // 2
        return s[:h] == s[:len(s) - h - 1:-1]


    print(palindrome(s))
