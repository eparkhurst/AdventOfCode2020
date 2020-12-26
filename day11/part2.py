f = open('input.txt', 'r')
input_data = f.read().strip().split('\n')
f.close()

input_data = [int(item) for item in input_data]


def get_paths(data, paths, n):
    s = 0
    for x in range(n-1, -1, -1):
        if data[n]-data[x] <= 3:
            s += paths[x]
        else:
            break
    return s


def find_combos(data):
    data.sort()
    data = [0] + data + [data[-1] + 3]
    paths = [1]
    for i in range(1, len(data)):
        paths.append(get_paths(data, paths, i))
    print(paths[-1])


def main():
    find_combos(input_data)


if __name__ == "__main__":
    main()
