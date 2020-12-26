f = open('input.txt', 'r')
input_data = f.read().strip().split('\n')
f.close()

input_data = [int(item) for item in input_data]


def check_sums(start, data, target):
    set_sum = 0
    nums = []
    for i in range(start, len(data)):
        set_sum += data[i]
        nums.append(data[i])
        if set_sum == target:
            return nums
        if set_sum > target:
            return False


def find_weakness(data, target):
    for i in range(len(data)):
        result = check_sums(i, data, target)
        if result is not False:
            print(min(result) + max(result))
            return
    print('not found')


def main():
    find_weakness(input_data, 530627549)


if __name__ == "__main__":
    main()
