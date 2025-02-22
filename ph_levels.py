ph = int(input('Enter a pH value (0-14): '))
if ph > 7:
    print("It's basic.")
elif ph < 7:
    print("It's acidic.")
else:
    print("It's neutral.")


