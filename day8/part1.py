f = open('input.txt', 'r')
content = f.read().strip().split('\n')
f.close()

def runCode(code):
    gA = 0
    loc = 0
    previous = []
    while loc < len(code):
        if loc in previous:
            return previous

        previous.append(loc)

        [cmd, direction] = code[loc].split(' ')

        if cmd == 'nop':
            pass
        elif cmd == 'jmp':
            loc += int(direction.strip())
            continue
        elif cmd == 'acc':
            gA += int(direction.strip())
        loc += 1
    print(gA)
    return True

def main():
    processing = True
    while processing:
        result = runCode()
        if type(result) is list


runCode(content)
# 560 too high
