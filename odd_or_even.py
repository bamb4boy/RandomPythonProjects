name = input("What is your name: ")
age = int(input("Please enter your age: "))
#print("Your name is: " + name + "\nYour age is: " + str(age))
#print("Your age is: " + str(age))
if age > 17:
    print("Hey " + name + " You can see R rated movie")
elif age < 17 and age > 12:
    print("Hey " + name + " You can see PG-13 rated movie")
else:
    print(("Hey " + name + " You can see PG rated movie"))