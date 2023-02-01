print('-Unpacking Container-')
# Allow to take each item like individual value
NUMBERS = [1, 2, 3]
NUMBERS_SECOND = [6, 5, 4]
print(NUMBERS)
print(*NUMBERS)
# Can combine
print(*NUMBERS, *"Hello")
print(*NUMBERS, *NUMBERS_SECOND)

# For Dictionaries. If two dictioraies have the same key - last key value will be used
FIRST_DIC = {"x": 1}
SECOND_DIC = {"x": 10, "y": 20}
COMBO = {**FIRST_DIC, **SECOND_DIC, "L": 30}
print(COMBO)
