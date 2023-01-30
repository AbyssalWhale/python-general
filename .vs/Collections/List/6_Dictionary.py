# key - only immutable types - string or int
# key - are unique. Duplicates will be ignored

POINTS = {"x": 1, "y": 2}
POINTS_FUNC = dict(x=1, y=2)

print(POINTS)
print(POINTS_FUNC)
print(POINTS["x"])
POINTS_FUNC["l"] = 3
print(POINTS_FUNC["l"])

if "l" in POINTS_FUNC:
    print("L exist in dic:", POINTS_FUNC["l"])

# Return None if not found or default value can be specified
DEFAULT_VALUE = 0
FIND_ELEMENT = POINTS_FUNC.get("S", DEFAULT_VALUE)
print(FIND_ELEMENT)

# Remove
print(POINTS_FUNC)
del POINTS_FUNC["l"]
print(POINTS_FUNC)

# Withour items() iterates by key
for record in POINTS.items():
    print(record)

for key, value in POINTS.items():
    print(f"KEY: {key} VALUE: {value}")

# Use comprehension to create dictionary from list
MY_LIST = range(5)
MY_DIC = {x: x * 2 for x in MY_LIST}
print(MY_DIC)
