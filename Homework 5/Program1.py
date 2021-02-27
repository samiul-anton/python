def my_range(start,end,iteration):
    while start <= end:
        yield start
        start += iteration

for i in my_range(0,10,2):
    print(i)