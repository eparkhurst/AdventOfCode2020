import re
f = open('input.txt', 'r')
content = f.read().strip().split('\n\n')
f.close()

content = [pp.replace('\n', ' ') for pp in content]

def checkByr(input):
    return 1920 <= int(input) <= 2002

def checkIyr(input):
    return 2010 <= int(input) <= 2020

def checkEyr(input):
    return 2020 <= int(input) <= 2030

def checkHgt(input):
    hgtCM = re.findall(r'(\d+)(?:cm)', input )
    if hgtCM:
        if 150 <= int(hgtCM[0]) <= 193:
            return True
        else:
            return False
    hgtIN = re.findall(r'(\d+)(?:in)', input )
    if hgtIN:
        if 59 <= int(hgtIN[0]) <= 76:
            return True
    return False

def checkHcl(input):
    hcl = re.findall(r'(?:#)([a-f0-9]+)', input)
    if not hcl:
        return False
    if len(hcl[0]) == 6:
        return True
    return False

def checkEcl(input):
    if any(input in s for s in ['amb' 'blu' 'brn' 'gry' 'grn' 'hzl' 'oth']):
        return True
    return False

def checkPid(input):
    nums = re.search(r'^[0-9]+$', input)
    if nums is None:
        return False
    return len(nums.group(0)) == 9

requiredFields = [('byr', checkByr), ('iyr', checkIyr),('eyr', checkEyr),('hgt', checkHgt),('hcl', checkHcl),('ecl', checkEcl), ('pid', checkPid)]

def checkFields(pp):
    for field in requiredFields:
        key = field[0] + ':'
        if key not in pp:
            return False
        match = re.findall(r'(?:'+key+')(\S+)', pp)
        func = field[1]
        if func(match[0]) is False:
            return False
    return True

count = 0
for pp in content:
    if checkFields(pp):
        count += 1
checkFields(content[0])
print(count)
# print(checkHcl('#f6brna'))
