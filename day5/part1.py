import math
import re

f = open('input.txt', 'r')
content = f.read().strip().split('\n')
f.close()

def narrow(letter, range):
    min, max = range
    diff = math.floor((max - min)/2)
    if letter in ('F','L'):
        max = min + diff
    elif letter in( 'B','R'):
        min = max - diff
    return (min, max)

def getSeatId(bsp):
    rows = bsp[0:7]
    columns = bsp[7:10]

    range = (0,127)
    for letter in rows:
        range = narrow(letter, range)

    cRange = (0,7)
    for letter in columns:
        cRange = narrow(letter, cRange)
    return (range[0] * 8) + cRange[0]

def checkAll(content):
    highest = 0
    for bsp in content:
        nextId = getSeatId(bsp)
        if nextId > highest:
            highest = nextId
    print(highest)

checkAll(content)
# narrow('F', (32, 63))
