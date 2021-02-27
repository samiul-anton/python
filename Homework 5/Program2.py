def bunny_ears(num_bunnies):
	if(num_bunnies)==0:
		return 0
    elif num_bunnies%2==0:
	    return bunny_ears(num_bunnies-1)+2

    else:
        return bunny_ears(num_bunnies-1)+3

result = bunny_ears(10)
print("total ears {}".format(result))