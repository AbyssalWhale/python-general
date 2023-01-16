# List

nyStringsList = ["K", "E", "R", "A", "S"]
myNumbersList = [0] * 100
print(nyStringsList + myNumbersList)

myNumberRange = range(20)
myListNumber = list(myNumberRange)
print(myListNumber)


phraseList = list("Hello World")
print(f"Phrase to list: {phraseList}")
print(f"List length: {len(phraseList)}")

# Accessing Items
print("-Accessing Items-")
myLetters = ["a", "b", "c", "d"]
print(f"zero item{myLetters[0]}")
print(f"zero and next item{myLetters[0:1]}")
print(f"next item{myLetters[:1]}")
print(f"{list(range(20))[::2]}")
print(f"\nreverse order{list(range(20))[::-1]}")

# List Unpacking
print("\n-Last Unpacking-")
myLastUnpackingNumber = [1, 2, 3]
first, second, third = myLastUnpackingNumber
print(first)
print(second)
print(third)

myLastUnpackingNumber = [1, 2, 3, 4, 5, 6]
first, second, *restItems = myLastUnpackingNumber
print(f"\n{first}")
print(second)
print(restItems)

myLastUnpackingNumber = [1, 2, 3, 4, 5, 6]
first, *restItems, last = myLastUnpackingNumber
print(f"\nFirst: {first}")
print(f"Last: {last}")
print(restItems)

# Add and Remove
print("-Add and Remove From List-")
MY_LETTERS = ["A", "B"]

# Added to the end
MY_LETTERS.append("C")
print(MY_LETTERS)

MY_LETTERS.insert(0, "----")
print(MY_LETTERS)

# Remove item. Last by default or specify index
MY_LETTERS.pop()
print(MY_LETTERS)

# Remove first match
MY_LETTERS.remove("A")
print(MY_LETTERS)

# Delete range
MY_LETTERS = ["A", "B", "C"]
del MY_LETTERS[0:1]
print(MY_LETTERS)

# Add and Remove
name = "Finding items in list"
print(f"-{name}-")

MY_LETTERS = ["A", "B", "C"]
# Not existed item will throw error
LETTER_TO_FIND = "B"
if LETTER_TO_FIND in MY_LETTERS:
    print(MY_LETTERS.index(LETTER_TO_FIND))

print(MY_LETTERS.count(LETTER_TO_FIND))

# SORTING
name = "SORT"
print(f"-{name}-")

MY_NUMBERS = [1, 2, 3, 4, 5, 6]
MY_NUMBERS.sort(reverse=True)
print(MY_NUMBERS)
print(sorted(MY_NUMBERS))

# LAMDA
name = "LAMDA"
print(f"-{name}-")
# sorting tuples
PRODUCT_ITEMS = [
    ("PRODUCT 1", 10),
    ("PRODUCT 2", 101),
    ("PRODUCT 3", 1)
]
# key=lambda item: item[1] - returns item 1 of each record from list - 1, 10, 101
PRODUCT_ITEMS.sort(key=lambda item: item[1])
print(PRODUCT_ITEMS)

# MAP
name = "MAP"
print(f"-{name}-")
# sorting tuples
PRODUCT_ITEMS = [
    ("PRODUCT 1", 10),
    ("PRODUCT 2", 101),
    ("PRODUCT 3", 1)
]

# accpet lamda and apply to each item of list. - returns item 1 of each record from list - 1, 10, 101
PRICES = list(map(lambda item: item[1], PRODUCT_ITEMS))
print(PRICES)


# FILTER
name = "FILTER"
print(f"-{name}-")
PRODUCT_ITEMS = [
    ("PRODUCT 1", 10),
    ("PRODUCT 2", 101),
    ("PRODUCT 3", 1)
]
# takes function and iterable object. Return prices higher than 10
FILTERED_PRICES = list(filter(lambda item: item[1] >= 10, PRODUCT_ITEMS))
print(FILTERED_PRICES)

# FILTER
name = "COMPREHENSION"
print(f"-{name}-")
PRODUCT_ITEMS = [
    ("PRODUCT 1", 10),
    ("PRODUCT 2", 101),
    ("PRODUCT 3", 1)
]

# Equals map - list(map(lambda item: item[1], PRODUCT_ITEMS)) - iterate through PRODUCT_ITEMS and returns item 1 of each record
PRICES = [item[1] for item in PRODUCT_ITEMS]
print(PRICES)

# Equal list - list(filter(lambda item: item[1] >= 10, PRODUCT_ITEMS))
FILTERED_PRICES = [item for item in PRODUCT_ITEMS if item[1] > 10]
print(FILTERED_PRICES)

# return bool for each item from PRODUCT_ITEMS. Check if item 1 of each record >= 10
FILTERED_PRICES = [item[1] >= 10 for item in PRODUCT_ITEMS]
print(FILTERED_PRICES)
