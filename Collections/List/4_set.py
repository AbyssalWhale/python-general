# Can contains only unique items?
# Unordered collection
# No access by index

NUMBERS = [1, 1, 2, 2, 3, 4, 2]
FIRST_SET = set(NUMBERS)
print(FIRST_SET)

SECOND_SET = {1, 4, 6}

# Combine Sets
print(FIRST_SET | SECOND_SET)

# Returns that exist in both Sets
print(FIRST_SET & SECOND_SET)

# Returns items of FIRST_SET that does not exist in SECOND_SET
print(FIRST_SET - SECOND_SET)

# Returns unique items of both sets (simmetrix)
print(SECOND_SET ^ FIRST_SET)

if 1 in FIRST_SET:
    print("Number one exist in set")
