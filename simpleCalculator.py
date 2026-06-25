#functions to make the simple calculator
def addNumber():
    return num_1+num_2

def subtractNumber():
    if(num_1 > num_2):
        return num_1 - num_2
    else:
        return num_1 - num_2

def multiplyNumber():
    return num_1 * num_2

def divideNumber():
    if(num_2 == 0):
        return "The Denominator is zero. so, It is invalid!"
    elif(num_1 > num_2):
        return num_1 / num_2
    else:
        return num_2 / num_1

def divideWithRemainder():
    if(num_2 == 0):
        return "The Denominator is zero. so, It is invalid!"
    elif(num_1 < num_2):
        return num_1 // num_2
    else:
        return num_2 // num_1

    #Main Program to make a fully functional calculator
print("\n ====== Welcome to My Python Calculator ===== \n")

num_1 = int(input("Enter the first number  = "))
num_2 = int(input("Enter the second number  = "))

print("Choose the following\n1.)Addition(+)\n2.)Subtraction(-)\n3.)Multiplication(*)\n4.)Division(/)\n5.)Division(Remainder)(//)\n")
choice = input("Enter the mathematical operations that you wanted to do to perform = ")

if(choice == '+'):
    print("Addition of the two numbers = ", addNumber())
elif(choice == '-'):
    print("Subtraction of the two numbers = ", subtractNumber())
elif(choice == '*'):
    print("Multiplication of the two numbers = ", multiplyNumber())
elif(choice == '/'):
    print("Divide of the two numbers = ", divideNumber())
elif(choice == '//'):
    print("Divide(remainder) of the two numbers = ",divideWithRemainder())
else:
    print("Invalid choice!")




