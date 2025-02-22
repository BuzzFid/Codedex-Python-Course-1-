#Food Ratings

print("Enter the rating of the food:")
rating = float(input())

if  5 >= rating >= 4.5:
    print("Extraordinary")
elif 4.5 > rating >= 4.0:
    print("Excellent")
elif 4.0 > rating >= 3.0:
    print("Good")
elif 3.0 > rating >= 2.0:
    print("Fair")
elif 2.0 > rating >=0.0: 
    print("Poor")
else:
    print("Invalid rating")

