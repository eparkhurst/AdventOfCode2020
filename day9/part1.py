f = open('input.txt', 'r')
input_data = f.read().strip().split('\n')
f.close()

input_data = [int(item) for item in input_data]


def check_sum(preamble, num):
    for i in range(len(preamble)):
        for j in range(i, len(preamble)):
            if preamble[i] + preamble[j] == num:
                return True
    return False


def find_fault(p_length, data):
    for i in range(p_length, len(data)):
        if not check_sum(data[i - p_length: i], data[i]):
            print(data[i])
            return


def main():
    find_fault(25, input_data)


if __name__ == "__main__":
    main()
