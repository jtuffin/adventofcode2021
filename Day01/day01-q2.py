import requests

# https://adventofcode.com/2021/day/1
# Consider sums of a three-measurement sliding window. 
# How many sums are larger than the previous sum?

class NumberSet:

    def __init__ (self, id):
        self.id = id
        self.__nx = []

    def add_number(self, n):
        if len(self.__nx) < 3:
            self.__nx.append(n)

    def count(self):
        return (len(self.__nx))
    def nxx(self,x):
        return (self.__nx[x])

    def sum(self):
        if len(self.__nx) == 3:
#            print (f"{self.__nx[0]} + {self.__nx[1]} + {self.__nx[2]}")
            return (self.__nx[0] + self.__nx[1] + self.__nx[2])


with open('Day02/challenge.txt', 'r') as file:  # Use file to refer to the file object
    challenge_source = file.readlines()

sets = 0
workout = []

for c in challenge_source:
    item = int(c.strip())
    sets = sets + 1
    workout.append(NumberSet(sets))
    workout[sets - 1].add_number(item)
    if sets > 1:
        workout[sets - 2].add_number(item)
    if sets > 2:
        workout[sets - 3].add_number(item)



loopCount = 0
answerCount = 0

rng = range(0,len(workout) -1,1)
for i in rng:
#    print(f"{i}  {workout[i].sum()}")
    try:
        item = int(workout[i].sum())
        if loopCount == 0:
            previous = item
            loopCount = loopCount + 1
        if item > previous:
            answerCount = answerCount + 1
            print(f"{answerCount}: {item} is greater than {previous}")
            previous = item
        else:
            previous = item
    except:
        print("Error")

print(f"Answer: {answerCount}")

# 1805
