import re
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
    if len(message) <= index:
        print('hit')
        return index
    rule = rule_dict[rule_num]
    for rule_set in rule:
        temp_index = index
        for i, num in enumerate(rule_set):
            if type(rule_dict[num]) is str:
                if message[temp_index] == rule_dict[num]:
                    temp_index += 1
                else:
                    break
            else:
                result = test_message(message, rule_dict, num, temp_index)
                if result:
                    temp_index = result
                else:
                    break
        else:
            return temp_index
    return False


def main():
    rule_dict = build_rules(rules_block)
    total = 0
    for message in messages.split('\n'):
        final_length = test_message(message, rule_dict)
        if len(message) == final_length:
            total += 1
    print(total)


if __name__ == "__main__":
    main()