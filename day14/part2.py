import re

f = open('input.txt', 'r')
input_data = f.read().strip().split('\n')
f.close()


addresses = []


def recur(mask):
    for i in range(len(mask)):
        if mask[i] == 'X':
            recur(mask[:i] + '1' + mask[i + 1:])
            recur(mask[:i] + '0' + mask[i + 1:])
            return
    addresses.append(int(mask, 2))
    return


def get_addresses(mask):
    addresses.clear()
    recur(mask)
    return addresses


def run_program(data):
    memory = {}
    current_mask = ''
    for command in data:
        loc, val = command.split(' = ')
        if loc == 'mask':
            current_mask = val
            continue
        m = re.findall(r"\[(.*)\]", loc)[0]
        bit32 = format(int(m), '036b')
        for i in range(len(current_mask)):
            if current_mask[i] == '0':
                continue
            bit32 = bit32[:i] + current_mask[i] + bit32[i + 1:]
        addresses_to_assign = get_addresses(bit32)
        for a in addresses_to_assign:
            memory[a] = val

    final = 0
    for val in memory.values():
       final += int(val)
    return final


def main():
    final = run_program(input_data)
    print(final)


if __name__ == "__main__":
    main()
