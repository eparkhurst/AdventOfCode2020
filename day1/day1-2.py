f = open('input.txt', 'r')
content = f.read().strip().split('\n')
f.close()

def convert(str):
    return int(str)

input = [int(i) for i in content]

def findPair(list):
    for i, expense in enumerate(list):
        for j in range(i, len(list)):
            for k in range(j, len(list)):
                if expense + list[j]+ list[k] == 2020:
                    print(expense)
                    print(list[j])
                    print(list[k])
                    return expense * list[j] * list[k]

print(findPair(input))
