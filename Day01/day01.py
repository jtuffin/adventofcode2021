import requests

# https://adventofcode.com/2021/day/1
# How many measurements are larger than the previous measurement?

with open('challenge.txt', 'r') as file:  # Use file to refer to the file object
    challenge_source = file.readlines()

loopCount = 0
answerCount = 0
for c in challenge_source:
    item = int(c.strip())
    if loopCount == 0:
        previous = item
        loopCount = loopCount + 1
    if item > previous:
        answerCount = answerCount + 1
        print(f"{answerCount}: {item} is greater than {previous}")
        previous = item
    else:
        previous = item


print(f"Answer: {answerCount}")

# 1759    
