f = open('input.txt', 'r')
rules, your_ticket, nearby_tickets = f.read().strip().split('\n\n')
f.close()


def v_factory(rule):
    content = rule.split(': ')[1]
    p1, p2 = content.split(' or ')
    p1 = p1.split('-')
    p2 = p2.split('-')
    def temp(num):
        return int(p1[0]) <= int(num) <= int(p1[1]) or int(p2[0]) <= int(num) <= int(p2[1])
    return temp


def get_funcs():
    verifiers = []
    split_rules = rules.split('\n')
    for rule in split_rules:
        verifiers.append(v_factory(rule))
    return verifiers

def get_positions(verifiers, valid_tickets):
    mold = [True] * len(verifiers)
    matrix = []
    for i in range(len(verifiers)):
        matrix.append(mold.copy())
        for ticket in valid_tickets:
            for j in range(len(ticket)):
                if verifiers[i](ticket[j]) is False:
                    matrix[i][j] = False
    split_rules = rules.split('\n')
    split_rules = [rule.split(':')[0] for rule in split_rules]

    positions = {}
    done = 0
    while done < len(matrix[0]):
        for i in range(len(matrix)):
            if matrix[i].count(True) == 1:
                index = matrix[i].index(True)
                positions[split_rules[i]] = index
                done += 1
                for line in matrix:
                    line[index] = False
    return positions

def run_program():
    verifiers = get_funcs()
    tickets = nearby_tickets.split('\n')[1:]
    tickets = [t.split(',') for t in tickets]

    valid_tickets = []
    for ticket in tickets:
        valid_ticket = True
        for num in ticket:
            ok = False
            for v in verifiers:
                if v(num) is True:
                    ok = True
            if ok is False:
                valid_ticket = False
        if valid_ticket is True:
            valid_tickets.append(ticket)
    positions = get_positions(verifiers, valid_tickets)

    my_ticket = your_ticket.split('\n')[1]
    my_ticket = my_ticket.split(',')
    total = 1
    for field in positions.keys():
        if 'departure' in field:
            total *= int(my_ticket[positions[field]])
    return total


def main():
    final = run_program()
    print(final)

if __name__ == "__main__":
    main()

# 762 is too low