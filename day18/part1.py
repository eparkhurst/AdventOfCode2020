f = open('input.txt', 'r')
input_data = f.read().strip().split('\n')
f.close()


def evaluate(expression):
    arr = expression.split(' ')
    count = []
    for c in arr:
        try:
            int(c)
            count.append(c)
            if len(count):
                exp = ' '.join(count)
                count.clear()
                count.append(str(eval(exp)))
        except:
            count.append(c)
    return count[0]



def solve_line(expression):
    inside = ''
    next_exp = '%s' % expression
    while '(' in next_exp:
        for char in expression:
            if len(inside):
                if char == ')':
                    paren = inside + char
                    new_num = evaluate(inside[1:])
                    next_exp = next_exp.replace(paren, new_num)
                if char == '(':
                    inside = char
                    continue
                inside += char
            elif char == '(':
                inside += char
        expression = next_exp
    return evaluate(expression)


def run_program(lines):
    count = 0
    for line in lines:
        count += int(solve_line(line))
    return count


def main():
    final = run_program(input_data)
    print(final)


if __name__ == "__main__":
    main()
