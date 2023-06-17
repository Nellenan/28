import sys

class ThreadRedirect:
    def __init__(self):
        self.stdout = sys.stdout

    def __enter__(self):
        sys.stdout = open('new_stdout.txt', 'w', encoding='utf-8')
        # sys.stdout = sys.stderr

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout = self.stdout

with ThreadRedirect():
    print('Hello, World!')