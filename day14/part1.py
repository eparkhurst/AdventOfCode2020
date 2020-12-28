import re
f = open('input.txt', 'r')
input_data = f.read().strip().split('\n')
f.close()


def get_mask(mask):
    mask_pos = []
    ml = len(mask)
    for i in range(ml - 1, -1, -1):
        if mask[i] != 'X':
            mask_pos.append((ml -1 - i, mask[i]))
    return mask_pos


def main():
    memory = {}
    mask_pos = []
    for command in input_data:
        loc, val = command.split(' = ')
        if loc == 'mask':
            mask_pos = get_mask(val)
            continue
        m = re.findall(r"\[(.*)\]", loc)[0]
        bit32 = format(int(val), '036b')
        for diff in mask_pos:
            pos = len(bit32) - diff[0] - 1
            bit32 = bit32[:pos] + diff[1] + bit32[pos + 1:]
        memory[m] = int(bit32, 2)

    final = 0
    for val in memory.values():
        final += int(val)
    print(final)


if __name__ == "__main__":
    main()

# 2985188059952418168305 too high
# 7784919768449 too low