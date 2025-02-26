# The Magic 8 Ball

import random

q1= ("Yes - definitely.")
q2= ("It is decidedly so.")
q3= ("Without a doubt.")
q4= ("Reply hazy, try again.")
q5= ("Ask again later.")
q6= ("Better not tell you now.")
q7= ("My sources say no.")
q8= ("Outlook not so good.")
q9= ("Very doubtful.")
responses = [q1, q2, q3, q4, q5, q6, q7, q8, q9]
m8 = random.choice(responses)
print("Enter your question")
q = input("Question: ")
print("Magic 8 Ball: ", m8)



# #Another way to do it:

# import random

# question = input('Question:      ')

# random_number = random.randint(1, 9)

# if random_number == 1:
#   answer = 'Yes - definitely'
# elif random_number == 2:
#   answer = 'It is decidedly so'
# elif random_number == 3:
#   answer = 'Without a doubt'
# elif random_number == 4:
#   answer = 'Reply hazy, try again'
# elif random_number == 5:
#   answer = 'Ask again later'
# elif random_number == 6:
#   answer = 'Better not tell you now'
# elif random_number == 7:
#   answer = 'My sources say no'
# elif random_number == 8:
#   answer = 'Outlook not so good'
# elif random_number == 9:
#   answer = 'Very doubtful'
# else:
#   answer = 'Error'
  
# print('Magic 8 Ball:  ' + answer)
