f = open('input.txt', 'r')
content = f.read().strip().split('\n\n')
f.close()

def removeSpace(group):
    return group.split('\n')
cleaned = map(removeSpace, content)

def getCommon(group):
    inAll = group[0]
    for person in group:
        afterCheck = []
        for letter in inAll:
            if letter in person:
                afterCheck.append(letter)
        inAll = afterCheck
    return len(set(afterCheck))

def getCount(cleaned):
    count = 0
    for group in cleaned:
        count += getCommon(group)
    print(count)

getCount(cleaned)
