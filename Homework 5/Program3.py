import time
def measure(func):
    def inner(*args):
        start = time.time()
        a = func(*args)
        end = time.time()
        print(end - start)
        return a
    return inner

@measure
#def myfunc(a, b, c):
 #   return a+b+c
#a = myfunc(5, 2, 90)
#print(a)
def my_range(start,end,iteration):
    while start <= end:
        yield start
        start += iteration

for i in my_range(0,10,2):
    print(i)