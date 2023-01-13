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
