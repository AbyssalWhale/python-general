# Add and Remove
print("-Add and Remove From List-")
MY_LETTERS = ["A", "B"]

# Added to the end
MY_LETTERS.append("C")
print(MY_LETTERS)

MY_LETTERS.insert(0, "----")
print(MY_LETTERS)

# Remove nd return item. Last by default or specify index
MY_LETTERS.pop()
print(MY_LETTERS)

# Remove first match only
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
