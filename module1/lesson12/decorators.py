import time


def timer(func):
    def wrapper(a):
        
        start = time.time()
        result = func(a)
        print(time.time() - start)

        return result
    return wrapper

@timer
def hello(a):
    result = []
    for i in range(a):
        result.append(i)
    
    print(sum(result))
    



def hello_2():
    print('1')

hello(10000000)