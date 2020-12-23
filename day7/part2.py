import re

f = open('input.txt', 'r')
content = f.read().strip().split('\n')
f.close()


dict = {}

def recur(bag):
    if bag in dict.keys() and dict[bag]:
        count = 0
        for ib in dict[bag]:
            count +=  int(ib[0]) + (int(ib[0])* recur(ib[1].strip()))
        return count
    else:
        return 0

def createDict(raw):

    for rule in raw:
        [outer, inner] = rule.split('bags contain')
        inners = re.findall(r'(\d)(.*?)(?:bag)', inner)
        dict[outer.strip()] = inners
    final = recur('shiny gold')
    print(final)

createDict(content)

# 4758 low
# 56935 high
