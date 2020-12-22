f = open('input.txt', 'r')
content = f.read().strip().split('\n')
f.close()

def getTreeCount(xRate, yRate):
    count = 0
    for i in range(len(content)):
        y = i * yRate
        x = (i * xRate) % 31
        if y > len(content):
            break
        if content[y][x] == '#':
            count += 1
    return count

a = getTreeCount(1,1)
b = getTreeCount(3,1)
c = getTreeCount(5,1)
d = getTreeCount(7,1)
e = getTreeCount(1,2)


print( a * b * c * d *  e)
