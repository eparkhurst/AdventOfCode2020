f = open('input.txt', 'r')
content = f.read().strip().split('\n\n')
f.close()

content = [pp.replace('\n', ' ') for pp in content]
print(len(content))
requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def checkFields(pp):
     for field in requiredFields:
        key = field + ':'
        if key not in pp:
            return False
     return True

count = 0
for pp in content:
    if checkFields(pp):
        count += 1

print(count)
