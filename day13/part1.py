import math
f = open('input.txt', 'r')
input_data = f.read().strip().split('\n')
f.close()


def find_bus(data):
    arrival = int(data[0])
    buses = data[1].split(',')
    closest = ['x', 1000000]
    for bus in buses:
        if bus == 'x':
            continue
        interval = int(bus)
        if interval/arrival % 1 == 0:
            return bus
        next_bus = (math.floor(arrival/interval) + 1) * int(bus)
        if next_bus - arrival < closest[1]:
            closest = [bus, next_bus - arrival]
    return int(closest[0]) * closest[1]

def main():
    final = find_bus(input_data)
    print(final)


if __name__ == "__main__":
    main()

# 799 too high