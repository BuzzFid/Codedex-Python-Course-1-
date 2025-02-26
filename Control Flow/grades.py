
import random
grade = random.randint(0, 100)   # Generates a random number between 0 and 100
print(grade)

if grade >=55: 
	print('You passed.')
else:
	print('You failed.')