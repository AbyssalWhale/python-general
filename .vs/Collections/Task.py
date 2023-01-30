from pprint import pprint

# find the most repetable letter
SENTENCE = "This is a common interview question"

MY_RESULT_LEETERS_DIC = {x.lower(): 0 for x in SENTENCE}
MY_RESULT_LEETERS_DIC.pop(" ")


for letter in SENTENCE:
    if letter in MY_RESULT_LEETERS_DIC:
        MY_RESULT_LEETERS_DIC[letter.lower(
        )] = MY_RESULT_LEETERS_DIC[letter.lower()] + 1

print(MY_RESULT_LEETERS_DIC)


def getHigher(MY_DIC):
    resultCounter = 0
    resultLetter = "0"
    for key, value in MY_DIC.items():
        if (value > resultCounter):
            resultLetter = key
            resultCounter = value
    return {resultLetter, resultCounter}


print(getHigher(MY_RESULT_LEETERS_DIC))


# Seconds
print("-Second Solution-")

CHAR_FREQ = {}
for char in SENTENCE:
    if char in CHAR_FREQ:
        CHAR_FREQ[char] += 1
    else:
        CHAR_FREQ[char] = 1
# pprint(CHAR_FREQ, width=1)

# Sorting by value in reverse order
CHAR_FREQ_SORTED = sorted(
    CHAR_FREQ.items(), key=lambda kv: kv[1], reverse=True)
print(CHAR_FREQ_SORTED[0])
