foundNummber = 0
for x in range(1, 10):
    # print(f"{x % 2} number {x}")
    if (x % 2) == 0:
        print(x)
        foundNummber = foundNummber + 1
print(f"We have {foundNummber} even numbers")
