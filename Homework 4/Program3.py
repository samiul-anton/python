def two_sum(num):
    for n in range(0,len(num)):
        for l in range(0,len(num)):
            if num[n] + num[l] == target:
                print("output: [{},{}]".format(n, l))
                break
num = list(map(int,input("Enter the numbers with spaces : ").strip().split()))
target = int(input("target: "))
two_sum(num)