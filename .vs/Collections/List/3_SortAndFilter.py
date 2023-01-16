from collections import deque

# SORTING
name = "SORT"
print(f"-{name}-")

MY_NUMBERS = [1, 2, 3, 4, 5, 6]
MY_NUMBERS.sort(reverse=True)
print(MY_NUMBERS)
print(sorted(MY_NUMBERS))

# LAMDA
name = "LAMDA"
print(f"-{name} - list sorting with lambda usage-")
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
print(f"-{name} - filter list-")
PRODUCT_ITEMS = [
    ("PRODUCT 1", 10),
    ("PRODUCT 2", 101),
    ("PRODUCT 3", 1)
]
# takes function and iterable object. Return prices higher than 10
FILTERED_PRICES = list(filter(lambda item: item[1] >= 10, PRODUCT_ITEMS))
print(FILTERED_PRICES)

# COMPREHENSION
name = "COMPREHENSION - filter and sort lists"
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

# ZIP
name = "ZIP"
print(f"-{name} - Combine lists-")

LIST_1 = [1, 2, 30]
LIST_2 = [1, 2, 30]

COMBINED_TUPLES = list(zip(LIST_1, LIST_2))
COMBINED_TUPLES = list(zip("ABC", LIST_1, LIST_2))
print(COMBINED_TUPLES)

# if list not empty
LIST_1 = []


def print_last_item(items):
    if items:
        print(f"last item: {items[-1]}")
    else:
        print("List is empty")


print_last_item(LIST_1)
print_last_item(LIST_2)

# DEQUE
name = "DEQUE"
print(f"-{name} - FIFO - remove first item and shift all list object to left-")

DEQUE_LIST = deque([1, 2, 30])
DEQUE_LIST.popleft()
print(DEQUE_LIST)
if not DEQUE_LIST:
    print("DEQUE_LIST is empty")
else:
    print("DEQUE_LIST is NOT empty")
