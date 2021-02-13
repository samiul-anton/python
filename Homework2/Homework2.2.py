word = input("Type word for shuffle = ")
num = []
for i in range(0,len(word)):
	num.append(i)
print("enter", len(word)-1 ,"numbers for shuffle including 0")
shuffled_numbers = []
for j in range(0,len(word)):
	o = input(f'Enter {j}no. input= ')
	shuffled_numbers.append(int(o))

l = list(word)

output = [''*len(word)]
for m in range(0,len(shuffled_numbers)):
	output[shuffled_numbers[m]] = word[m]
print("".join(output))