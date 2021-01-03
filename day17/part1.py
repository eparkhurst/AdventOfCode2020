f = open('input.txt', 'r')
input_data = f.read().strip().split('\n')
f.close()


def print_world(world):
    count = 0
    for z in world.keys():
        visible = ''
        for y in world[z].keys():
            for x in world[z][y].keys():
                alive = world[z][y][x]['alive']
                if alive: count += 1
                visible += '#' if alive else '.'
            visible += '\n'
    return count


def make_start_world(start_grid, iterations):
    world = {}
    for z in range(0 - iterations, 1 + iterations):
        world[z] = {}
        for y in range(0 - iterations, len(start_grid) + iterations):
            world[z][y] = {}
            for x in range(0 - iterations, len(start_grid[0]) + iterations):
                world[z][y][x] = {'alive': False}

    for y in range(len(start_grid)):
        for x in range(len(start_grid[y])):
            # world[y][x] = {'alive': False}
            world[0][y][x]['alive'] = start_grid[y][x] == '#'

    return world

def check_neighbors(z, y, x, world):
    dirs = [-1, 0, 1]
    neighbors = 0
    for dz in dirs:
        if dz + z not in world:
            continue
        for dy in dirs:
            if dy + y not in world[dz + z]:
                continue
            for dx in dirs:
                if dx == 0 and dy == 0 and dz == 0:
                    continue
                if dx + x not in world[dz + z][dy + y]:
                    continue
                if world[dz + z][dy + y][dx + x]['alive']:
                     neighbors += 1
    return neighbors


def run_program(start_grid, iterations):
    world = make_start_world(start_grid, iterations)
    for i in range(iterations):
        next_world = world.copy()
        for z in world.keys():
            next_world[z] = {}
            for y in world[z].keys():
                next_world[z][y] = {}
                for x in world[z][y].keys():
                    next_world[z][y][x] = {'alive': False}
                    neighbors = check_neighbors(z, y, x, world)
                    if world[z][y][x]['alive']:
                        if neighbors == 2 or neighbors == 3:
                            next_world[z][y][x]['alive'] = True
                    else:
                        if neighbors == 3:
                            next_world[z][y][x]['alive'] = True
        world = next_world
    return print_world(world)


def main():
    final = run_program(input_data, 6)
    print(final)


if __name__ == "__main__":
    main()
