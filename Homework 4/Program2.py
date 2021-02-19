def count_frequency(mylist):
    dict = {}
    for word in mylist:
        if word in dict:
            dict[word] = dict[word] +1
        else:
            dict[word] = 1

    for key in list(dict.keys()):
        print(key, ":", dict[key])

mylist = ["one", "two","eleven",  "one", "three", "two", "eleven", "three", "seven", "eleven"]
count_frequency(mylist)