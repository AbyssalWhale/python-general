from timeit import timeit

CODE_1 = """

def func_withException(age):
    if age <= 0:
        raise ValueError("Age can not be zero or less")
    return 10 / age


try:
    func_withException(0)
except ValueError as ex:
    print(f"Error during calculate age. Ex type: {type(ex)}")

"""

CODE_2 = """

def func_withException(age):
    if age <= 0:
        return None
    return 10 / age


X_FACTOR = func_withException(0)
if X_FACTOR == None:
    print("Number is equal or less than 0")
else:
    print(f"x factor: {X_FACTOR}")

"""

# number - amount of time to execute code
# print("CODE_1 = ", timeit(CODE_1, number=50000))
print("CODE_2 = ", timeit(CODE_2, number=50000))
