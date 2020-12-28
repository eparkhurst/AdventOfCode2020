f = open('input.txt', 'r')
input_data = f.read().strip().split(',')
f.close()


def get_latest_index(li, x, current):
    for i in reversed(range(len(li) -1)):
        if li[i] == x:
            return current - i - 1
    return 0

def run_program(data):
    running_list = data.copy()
    running_list = [int(num) for num in running_list]
    for i in range(len(data), 30000000):
        last =  running_list[-1]
        next = get_latest_index(running_list, last, i)
        running_list.append(next)
    return running_list[-1]


def main():
    final = run_program(input_data)
    print(final)


if __name__ == "__main__":
    main()
