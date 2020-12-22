f = open('input.txt', 'r')
content = f.read().strip().split('\n')
f.close()

def convert(str):
    return int(str)

input = [int(i) for i in content]

def findPair(list):
    for i, expense in enumerate(list):
        for j in range(i, len(list)):
            if expense + list[j] == 2020:
                print(expense)
                print(list[j])
                return expense * list[j]

print(findPair(input))
