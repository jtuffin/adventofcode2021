import requests

# https://adventofcode.com/2021/day/2


with open('day02/challenge.txt', 'r') as file:  # Use file to refer to the file object
    challenge_source = file.readlines()

horizpos = 0
depth = 0
aim = 0

for instr in challenge_source:
    (command, value) = instr.split(" ")
    if command == "forward":
        horizpos = horizpos + int(value)
        depth = depth + (aim * int(value))
    if command == "up":
        aim = aim - int(value)
    if command == "down":
        aim = aim + int(value)

print (f"Horiz pos: {horizpos}")
print (f"Depth: {depth}")
print (f"Horiz pos * depth: {horizpos*depth}")

# 1813062561
