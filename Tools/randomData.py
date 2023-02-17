import random
import string

print(random.random())
print(random.randint(1, 10))
print(random.choice([1, 10, 8]))
print(random.choices([1, 10, 8, 0, 11], k=2))
print(random.shuffle([1, 10, 8, 0, 11]))
print(random.choices(string.ascii_letters, k=4))
