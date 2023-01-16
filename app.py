# Variables
print("-" * 10)
print("Variables")
NUMBER = 1
MY_STRING = "my string "
MY_LIST_NUMBERS = [0, 1, 2, 3,]

# Boxing/Unboxing
print("-" * 10)
print("Boxing/Unboxing")
NUMBER_AS_STRING = str(NUMBER)

# String Operations
print("-" * 10)
print("String Operations")
MY_STRING = f"my string with \"Escape"
MY_STRING = f"my string with \nwith new line"
MY_STRING = f"my string with number {NUMBER}"

print(MY_STRING[0: 10])
print(len(MY_STRING))
print(MY_STRING.upper())
print(MY_STRING.lower())
print(MY_STRING.title())
print(
    f"rstrip remove white spaces at the end of the string: {MY_STRING.rstrip()}")
print(MY_STRING.replace("s", "S"))
print("my" in MY_STRING)
print("my" not in MY_STRING)

# Number Operations
print("-" * 10)
print("Number Operations")
# import math
# print(10 ** 3) - multiple X time on itself. 10 * 10 * 10
print(10 ** 3)
print(10 % 3)
print(10 // 3)

# Control Flow
print("-" * 10)
print("Control Flow")

# The closer letter to the end of alphabet then it's higher. M is higher than A
print("apple" > "microsoft")

# if
if (15 > 30):
    print("30")
elif (30 == 30):
    print(30)
else:
    print(0)

# Ternary
MY_STRING = "Hello" if 15 > 30 else "CHAO"

# Logical
HIGH_INCOME = True
GOOD_CREDIT = True
STUDENT = True

if not STUDENT:
    print("Can have credit")
else:
    print("NOT CREDIT FOR STUDENTS")

if (HIGH_INCOME or GOOD_CREDIT) and not STUDENT:
    print("Can have credit")
else:
    print("NOT CREDIT FOR STUDENTS")

if HIGH_INCOME or GOOD_CREDIT and STUDENT:
    print("Can have credit")
else:
    print("NOT CREDIT FOR STUDENTS")

AGE = 19

if 18 <= AGE < 65:
    print("Eligible")


for number in MY_LIST_NUMBERS:
    print(f"Loop number: {number}")
    if number == 0:
        break


def multiply(*numbers):
    result = 1
    for number in numbers:
        result = result * number
    return 1


print(multiply(1, 2, 3, 4))

# Scope

# xample Global Scope
myFirstName = "Oleh"


# Example Local Scope
def greet(name):
    myFirstName1 = ""
    print(name)
    print(myFirstName1)


print("Start")
print(greet(""))

myFirstName = "Keras"

print(myFirstName)


# Exercice

# 1. if number can be divided by 3 -> return 'Buzz'
# 2. if number can be divided by 5 -> return 'Fizz'
# 3. if number can be divided by 3 and 5 -> return 'FizzBuzz'
# 4. if number can NOT be divided by 3 and 5 -> return number


def FizzBuzz(number):
    result = ""
    if (number % 3 == 0 and number % 5 == 0):
        return "FizzBuzz"
    elif (number % 5 == 0):
        return "Fizz"
    elif (number % 3 == 0):
        return "Buzz"
    else:
        return number


print(f"Result: {FizzBuzz(3)}")
print(f"Result: {FizzBuzz(5)}")
print(f"Result: {FizzBuzz(15)}")
print(f"Result: {FizzBuzz(7)}")


#!!!!Keras!!!!!

# 1. if number can be divided by 3 -> return 'Buzz'

def FizzBuss(number):
    result = (number % 3) == 0
    if (result):
        return "Buzz"
    else:
        return number


print(FizzBuss(3))
print(FizzBuss(7))
