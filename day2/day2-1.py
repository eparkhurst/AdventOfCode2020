f = open('input.txt', 'r')
content = f.read().strip().split('\n')
f.close()

count = 0
for set in content:
    rule, pw = set.split(':')
    range, letter = rule.split(' ')
    start, stop = range.split('-')

    foundLetters = pw.count(letter)
    if int(start) <= foundLetters <= int(stop):
        count = count + 1

print(count)
