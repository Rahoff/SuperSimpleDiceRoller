import random
print("\033c")

def rollit():
	print ("How many sides are on your die? ")
	sides = int(input(''))
	print ("")
	print ("How many times would you like to roll it? ")
	numdice = int(input(''))
	print("")
	print("Enter your die modifier: ")
	modifier = int(input(''))
	total = 0
	count = 0

	print ("")
	print (f"Rolling {numdice}, {sides} siders plus {modifier} per die....")
	for count in range(0,numdice):
		result = random.randrange(1, sides+1)
		if modifier != 0:
			total += result + modifier
			print (f"Roll number {count+1}: {result} + {modifier} = {result+modifier}")
		else:
			total += result
			print (f"Roll number {count}: {result}")
		count += 1
	

	print("")
	print (f"Your total is: {total}")
	print("")

while True:
	print ("Would you like to roll some dice?")
	print ("Enter 'y' to roll, any other key to quit.")
	use = input('')
	if use =='y':
		print("Great, lets do it..")
		print("")
		rollit()
	else:
		print("")
		print ("Thanks for playing.")
		break



