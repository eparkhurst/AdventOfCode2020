f = open('input.txt', 'r')
content = f.read().strip().split('\n\n')
f.close()

def removeSpace(group):
    return group.replace('\n','')
cleaned = map(removeSpace, content)

def getCount(cleaned):
    count = 0
    for group in cleaned:
        num = len(set(group))
        count += num
    print(count)

getCount(cleaned)
