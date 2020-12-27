import math
f = open('input.txt', 'r')
input_data = f.read().strip().split('\n')
f.close()


def get_inverse(x, mod):
    return pow(x, -1, mod)

def chinese_remainder_theorem(inputs, big_n):
    sum_bnx = 0
    for tup in inputs:
        n_i = (big_n // tup[1])
        temp = (tup[1] - tup[0]) * n_i * get_inverse(n_i, tup[1])
        sum_bnx = sum_bnx + temp
    return sum_bnx % big_n

def get_lowest(data):
    all_relevant = []
    big_n = 1
    for i in range(len(data)):
        if data[i] != 'x':
            big_n = big_n * int(data[i])
            all_relevant.append((i, int(data[i])))
    return chinese_remainder_theorem(all_relevant, big_n)


def main():
    final = get_lowest(input_data[1].split(','))
    print(final)


if __name__ == "__main__":
    main()