def convert_func(user):
    celsius = (user - 32) / 1.8
    print("{}F = {}C".format(user, celsius))

user = int(input("Enter Farenheit to convert Celsius = "))
convert_func(user)