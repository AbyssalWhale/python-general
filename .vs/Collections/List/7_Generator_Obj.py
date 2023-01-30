from sys import getsizeof

# Generator Expressions - to no store large object in memory. It generates each value in new iteration
MY_VALUES = [x * 2 for x in range(1000)]
print(type(MY_VALUES))
print(f"List obj size: {getsizeof(MY_VALUES)}")

# () in comprehensive expression let us know that reulst object is Generator Object
MY_GEN_OBJECT = (x * 2 for x in range(1000))
print(type(MY_GEN_OBJECT))
print(f"Generator obj size: {getsizeof(MY_GEN_OBJECT)}")
