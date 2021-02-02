f = open('input.txt', 'r')
rules_block, messages = f.read().strip().split('\n\n')
f.close()


master_defs = []

def build_rules(rules):
    rules = rules.split('\n')
    rule_dict = {}
    for rule in rules:
        num, eq = rule.split(':')
        eq = eq.strip()
        if '"' in eq:
            eq = eq[1:-1]
        else:
            rule = []
            options = eq.split('|')
            for option in options:
                rule.append(tuple(option.strip().split(' ')))
            eq = rule
        rule_dict[num] = eq
    return rule_dict


def test_message(message, rule_dict, rule_num='0', index=0):
    count = 0
    if len(message) == index:
        return index
    rule = rule_dict[rule_num]
    for rule_set in rule:
        temp_index = index
        for num in rule_set:
            if type(rule_dict[num]) is str:
                if message[temp_index] == rule_dict[num]:
                    temp_index += 1
                else:
                    break
            else:
                result = test_message(message, rule_dict, num, temp_index)
                if result:
                    if temp_index == result:
                        if rule_set == ('42', '31'):
                            return False
                        count += 1
                    temp_index = result
                else:
                    break
        else:
            return temp_index
    return False


def main():
    rule_dict = build_rules(rules_block)
    rule_dict['8'] = [('42',), ('42', '8')]
    rule_dict['11'] = [('42', '31'), ('42', '11', '31')]
    total = 0
    for message in messages.split('\n'):
        final_length = test_message(message, rule_dict)
        if final_length == len(message):
            total += 1
    print(total)


if __name__ == "__main__":
    main()

# 335 too high
# 235 too low