import shelve,time

my_dict = {'Colorado': 'Rockies', 'Boston': 'Red Sox', 'Minnesota': 'Twins',
'Milwaukee': 'Brewers', 'Seattle': 'Mariners'}
a = shelve.open("save.db")

a['my_dict'] = my_dict
start = time.time()
print(my_dict)
end=time.time()
shelve_time = end-start
print("For shelve: {}\n\n".format(end-start))
a.close()


start = time.time()
print(my_dict)
end=time.time()
Dictionary_time = end-start
print("For Dictionary: {}\n\n".format(end-start))

if shelve_time>Dictionary_time:
    print("Dictionary is faster!!!")
else:
    print("Shelve is faster!!")




