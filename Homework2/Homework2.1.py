top = 1
bottom = 100
total_guesses = []
guess = (top+bottom)//2
total_guesses.append(guess)
correct_guess = input("is it " +(str(guess))+"? ")

while correct_guess == "no":
	correct_guess = input("Is the number larger than"+(str(guess))+"? ")
	while correct_guess == "yes":
		guess = (guess+bottom)//2
		total_guesses.append(guess)
		correct_guess = input("Is the number larger than" + (str(guess)) + "? ")
	while correct_guess == "no":
		guess = (total_guesses[-1] + total_guesses [-2])//2
		total_guesses.append(guess)
		correct_guess = input("is it "+(str(guess))+"? ")
		if correct_guess == "yes":
			print("yeey! I got in " , len(total_guesses)+1 , " tries!")
			correct_guess=input("Do you want to play more? ")
			if correct_guess == "yes":
				correct_guess = "no"
			else:
				print("Bye-bye")




