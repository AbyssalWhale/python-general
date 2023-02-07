# Create Custom Exception - must finish with word 'Error' and inherited from Exception
class InvalidAgeCustomError(Exception):
    pass


try:
    AGE = int(input("Age:"))
    X_FACTOR = 10 / AGE
# handling only ValueError type exceptions. Not all
except ValueError as ex:
    print(f"Unable to convert to a number. Error type:{type(ex)}")
# handling multiple types of exceptions
except (ValueError, ZeroDivisionError) as ex:
    print(f"Unable to convert to a number. Error type:{type(ex)}")
# handling any type of exceptions
except Exception as ex:
    print(f"Unable to convert to a number. Error type:{type(ex)}")
# executed if no exceptions
else:
    print("No Exceptions during data type conversion")
# always executed
finally:
    print("Executing finally")

print("Continue execution...")


print("--Custom Exceptions--")


def func_withException(age):
    if age <= 0:
        raise InvalidAgeCustomError(
            "Age can not be zero or less. Custom Exception1")
    return 10 / age


func_withException(0)
