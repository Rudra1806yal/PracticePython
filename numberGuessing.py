#Making a number guessing game in the console based
import random

select_number = random.randint(1,100)

guess = int(input("Guess the number between 1 to 100 = "))

if(select_number < guess):
    print("Low", select_number)
elif(select_number > guess):
    print("High", select_number)
else:
    print("Excellent", select_number)
