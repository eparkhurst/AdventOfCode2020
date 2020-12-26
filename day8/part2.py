f = open('input.txt', 'r')
content = f.read().strip().split('\n')
f.close()


def run_code(code):
    g_a = 0
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
            g_a += int(direction.strip())
        loc += 1
    print(g_a)
    return True


def main():
    stack = run_code(content)
    stack.reverse()
    for loc in stack:
        print(loc)
        action, location = content[loc].split(' ')
        if action == 'jmp':
            test_code = content.copy()
            test_code[loc] = 'nop ' + location
            if run_code(test_code) is True:
                return
        if action == 'nop':
            test_code = content.copy()
            test_code[loc] = 'jmp ' + location
            if run_code(test_code) is True:
                return


if __name__ == "__main__":
    main()
