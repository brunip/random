from random import randrange
with open('contestants.txt') as f:
    lines = f.read().splitlines()	
print lines[randrange(0,len(lines))]