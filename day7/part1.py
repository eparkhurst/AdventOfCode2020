import re

f = open('input.txt', 'r')
content = f.read().strip().split('\n')
f.close()

def createDict(raw):
    dict = {}
    for rule in raw:
        [outer, inner] = rule.split('bags contain')
        inners = re.findall(r'(?:\d)(.*?)(?:bag)', inner)
        for bag in inners:
            if bag.strip() in dict.keys():
                dict[bag.strip()].add(outer.strip())
            else:
                dict[bag.strip()] = set([outer.strip()])
    current = dict['shiny gold']
    finalBags = current.copy()
    while current:
        next = current.pop()
        if next in dict.keys():
            current.update(dict[next])
            finalBags.update(dict[next])

    print(len(finalBags))

createDict(content)

# 560 too high
