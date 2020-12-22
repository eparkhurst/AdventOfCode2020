f = open('input.txt', 'r')
content = f.read().strip().split('\n')
f.close()

def checkRule(set):
    rule, pw = set.split(':')
    range, letter = rule.split(' ')
    start, stop = range.split('-')

    # the code below works without subtracting 1 for the index because each pw starts with a space
    one = pw[int(start)] == letter
    two = pw[int(stop)] == letter

    # essentially return the xor of the two values
    return bool(one) != bool(two)

count = 0
for pwrule in content:
    if checkRule(pwrule):
        count += 1



print(count)
