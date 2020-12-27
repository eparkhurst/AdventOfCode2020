f = open('input.txt', 'r')
input_data = f.read().strip().split('\n')
f.close()


compass = {
    'N': 0,
    'E': 90,
    'S': 180,
    'W': 270,
}
inv_compass = {v: k for k, v in compass.items()}


def find_manhattan(data):
    current_dir = 'E'
    # x, y
    ship_pos = [0, 0]
    waypoint_pos = [10, 1]
    for com in data:
        direction = com[0]
        distance = int(com[1:])
        if direction == 'F':
            ship_pos[0] = ship_pos[0] + (distance * waypoint_pos[0])
            ship_pos[1] = ship_pos[1] + (distance * waypoint_pos[1])
        if direction == 'N':
            waypoint_pos[1] += distance
        if direction == 'S':
            waypoint_pos[1] -= distance
        if direction == 'E':
            waypoint_pos[0] += distance
        if direction == 'W':
            waypoint_pos[0] -= distance
        if com == 'R90' or com == 'L270':
            waypoint_pos = [waypoint_pos[1], -waypoint_pos[0]]
        if com == 'R270' or com == 'L90':
            waypoint_pos = [-waypoint_pos[1], waypoint_pos[0]]
        if com == 'R180' or com == 'L180':
            waypoint_pos = [-waypoint_pos[0], -waypoint_pos[1]]
    print(ship_pos)
    return abs(ship_pos[0]) + abs(ship_pos[1])


def main():
    final = find_manhattan(input_data)
    print(final)


if __name__ == "__main__":
    main()

# 799 too high