def palindrome(s):
    h = len(s) // 2
    print(s[:h] == s[:len(s) - h - 1:-1])


palindrome('лессел')  # Ввод слова для проверки на палиндром