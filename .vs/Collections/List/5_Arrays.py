from array import array

# i - is type code -> python 3 typecode -> google
numbers = array("i", [1, 2, 3])

numbers.pop()
numbers.append(0)
numbers.insert(0, -1)
numbers.remove(1)

for number in numbers:
    print(number)
