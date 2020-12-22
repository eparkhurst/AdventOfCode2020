f = open('input.txt', 'r')
content = f.read().strip().split('\n')
f.close()

count = 0

for y in range(len(content)):
    x = (y * 3) % 31
    if content[y][x] == '#':
        count += 1

print(count)
