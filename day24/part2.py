import copy
f = open('input.txt', 'r')
instructions = f.read().strip().split('\n')
f.close()


def get_floor():
    floor = {}
    for tile in instructions:
        x = 0
        y = 0
        i = 0
        while i < len(tile):
            if tile[i] == 'e':
               x += 1
               i += 1
            elif tile[i] == 'w':
                x -= 1
                i += 1
            elif tile[i] == 'n':
                y += 1
                if tile[i+1] == 'w':
                    x -= 0.5
                if tile[i+1] == 'e':
                    x += 0.5
                i += 2
            elif tile[i] == 's':
                y -= 1
                if tile[i+1] == 'w':
                    x -= 0.5
                if tile[i+1] == 'e':
                    x += 0.5
                i += 2
        if x in floor:
            if y in floor[x]:
                floor[x][y] = not floor[x][y]
            else:
                floor[x][y] = True
        else:
            floor[x] = {}
            floor[x][y] = True
    return floor


def check_neighbors(x, y, floor, next_floor):
    total = 0
    neighbors = [(x+1, y), (x-1, y), (x+0.5, y+1), (x+0.5, y-1), (x-0.5, y+1), (x-0.5, y-1)]
    for neighbor in neighbors:
        n_x, n_y = neighbor
        if n_x in floor:
            if n_y in floor[n_x]:
                if floor[n_x][n_y]:
                    total += 1
            else:
                next_floor[n_x][n_y] = False
        else:
            if n_x in next_floor:
                next_floor[n_x][n_y] = False
            else:
                next_floor[n_x] = {}
                next_floor[n_x][n_y] = False

    return total


def count_floor(floor):
    total = 0
    for x in floor:
        for y in floor[x]:
            if floor[x][y]:
                total += 1
    print(total)


def process_floor(floor):
    next_floor = copy.deepcopy(floor)
    for x in floor:
        for y in floor[x]:
            living_neighbors = check_neighbors(x, y, floor, next_floor)

            if floor[x][y] and (living_neighbors > 2 or living_neighbors == 0):

                next_floor[x][y] = False
            elif not floor[x][y] and living_neighbors == 2:

                next_floor[x][y] = True
            else:

                next_floor[x][y] = floor[x][y]
    return next_floor


def run_simulation(floor):
    for day in range(100):
        floor = process_floor(floor)
    count_floor(floor)

def fill_floor(floor):
    filled_floor = copy.deepcopy(floor)
    for x in floor:
        for y in floor[x]:
            check_neighbors(x, y, floor, filled_floor)
    return filled_floor


def main():
    floor_1 = get_floor()

    filled_floor = fill_floor(floor_1)

    count_floor(filled_floor)
    run_simulation(filled_floor)


if __name__ == "__main__":
    main()
