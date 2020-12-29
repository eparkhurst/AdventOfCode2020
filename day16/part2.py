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


def get_funcs(rules):
    verifiers = []
    rules = rules.split('\n')
    for rule in rules:
        verifiers.append(v_factory(rule))
    return verifiers

def get_positions(verifiers, valid_tickets):
    for i in range(len(verifiers)):
        for ticket in valid_tickets:
            if verifiers[i](ticket[i]) is False




def run_program():
    verifiers = get_funcs(rules)
    tickets = nearby_tickets.split('\n')[1:]
    tickets = [t.split(',') for t in tickets]

    print(len(tickets))
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
    print(len(valid_tickets))
    return 'hey'


def main():
    run_program()


if __name__ == "__main__":
    main()
