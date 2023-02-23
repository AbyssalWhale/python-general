# Used for large multi dimensional arrays

import numpy as np

# 2 dimension array
NP_ARRAY = np.array([[1, 2, 3], [4, 5, 6]])
print(NP_ARRAY)

# Print out amoun of records in each dimension. Return as tupple
print(NP_ARRAY.shape)

# Create new array from provided size
NEW_ARRAY = np.zeros((3, 4), dtype=str)
print(f"zeros: {NEW_ARRAY}")
NEW_ARRAY = np.ones((3, 4))
print(f"ones: {NEW_ARRAY}")
NEW_ARRAY = np.full((3, 4), 5)
print(f"full: {NEW_ARRAY}")
NEW_ARRAY = np.random.random((3, 4))
print(f"random: {NEW_ARRAY}")

print(
    f"combined arrays: {np.array([[1, 2, 3], [4, 5, 6]]) + np.array([[1, 2, 3], [4, 5, 6]])}")
