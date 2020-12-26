f = open('input.txt', 'r')
input_data = f.read().strip().split('\n')
f.close()

input_data = [int(item) for item in input_data]


def find_joltage(data):
    data.sort()
    one_diff = 1
    three_diff = 1
    for i in range(1, len(data)):
        if data[i] - data[i-1] == 1:
            one_diff += 1
        elif data[i] - data[i-1] == 3:
            three_diff += 1
        else:
            print(data[i])
            print(data[i] - data[i-1])
    print(one_diff * three_diff)


def main():
    find_joltage(input_data)


if __name__ == "__main__":
    main()
