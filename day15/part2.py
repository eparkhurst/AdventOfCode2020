f = open('input.txt', 'r')
input_data = f.read().strip().split(',')
f.close()


past_nums = {}


def run_program(data):
    running_list = data.copy()
    for i in range(len(running_list) - 1):
        past_nums[int(running_list[i])] = i
    last_num = int(running_list[-1])
    for i in range(len(data), 30000000):
        if last_num in past_nums.keys():
            temp = past_nums[last_num]
            past_nums[last_num] = i -1
            last_num = i - temp -1
        else:
            past_nums[last_num] = i -1
            last_num = 0
    return last_num


def main():
    final = run_program(input_data)
    print(final)


if __name__ == "__main__":
    main()
