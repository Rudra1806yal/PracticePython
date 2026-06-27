#Making a Password Generator by using to import a random and string

import random
import string

print("Welcome to the password generating site")

characters = (
    string.ascii_lowercase + 
    string.ascii_uppercase + 
    string.digits +
    string.punctuation
)

length = int(input("Enter the length of a password = "))

password = " "

for i in range(length):
    password += random.choice(characters)

print("Generated Password = ", password)


