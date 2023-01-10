foundNummber = 0
name = "Oleh"

for x in range(1, 10):
    # print(f"{x % 2} number {x}")
    if (x % 2) == 0:
        print(x)
        foundNummber = foundNummber + 1
print(f"We have {foundNummber} even numbers")

# Create a function that gives a personalized greeting. This function takes two parameters: name and owner.


def greet(name, owner):
    if (name.lower() == owner.lower()):
        return 'Hello boss'
    else:
        return 'Hello guest'

# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.
#   Return your answer as a number.


def sum_mix(arr):
    result = 0
    for number in arr:
        result = result + int(number)
    return result


print(sum_mix([9, 3, '7', '3']))

#The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.

def century(year):
    centruy = int(str(year)[0:1]) if year < 1000 else int(str(year)[0:2])
    lastNumber = year % 10
    nummberBeforeLast = int(str(year))

    return centruy if (year % 10) == 0 else centruy + 1

print(f"Year: {century(2023)}")
