f = open('input.txt', 'r')
input_data = f.read().strip().split('\n')
f.close()


def print_world(world):
    count = 0
    for w in world.keys():
        for z in world[w].keys():
            visible = ''
            for y in world[w][z].keys():
                for x in world[w][z][y].keys():
                    alive = world[w][z][y][x]['alive']
                    if alive: count += 1
                    visible += '#' if alive else '.'
                visible += '\n'
    return count


def make_start_world(start_grid, iterations):
    world = {}
    for w in range(0 - iterations, 1 + iterations):
        world[w] = {}
        for z in range(0 - iterations, 1 + iterations):
            world[w][z] = {}
            for y in range(0 - iterations, len(start_grid) + iterations):
                world[w][z][y] = {}
                for x in range(0 - iterations, len(start_grid[0]) + iterations):
                    world[w][z][y][x] = {'alive': False}

    for y in range(len(start_grid)):
        for x in range(len(start_grid[y])):
            world[0][0][y][x]['alive'] = start_grid[y][x] == '#'

    return world

def check_neighbors(w, z, y, x, world):
    dirs = [-1, 0, 1]
    neighbors = 0
    for dw in dirs:
        if dw + w not in world:
            continue
        for dz in dirs:
            if dz + z not in world[dw + w]:
                continue
            for dy in dirs:
                if dy + y not in world[dw + w][dz + z]:
                    continue
                for dx in dirs:
                    if dx == 0 and dy == 0 and dz == 0 and dw == 0:
                        continue
                    if dx + x not in world[dw + w][dz + z][dy + y]:
                        continue
                    if world[dw + w][dz + z][dy + y][dx + x]['alive']:
                        neighbors += 1
    return neighbors


def get_next_world(old_world):
    next_world = old_world.copy()
    for w in old_world.keys():
        next_world[w] = {}
        for z in old_world[w].keys():
            next_world[w][z] = {}
            for y in old_world[w][z].keys():
                next_world[w][z][y] = {}
                for x in old_world[w][z][y].keys():
                    next_world[w][z][y][x] = {'alive': False}
                    neighbors = check_neighbors(w, z, y, x, old_world)
                    if old_world[w][z][y][x]['alive']:
                        if neighbors == 2 or neighbors == 3:
                            next_world[w][z][y][x]['alive'] = True
                    else:
                        if neighbors == 3:
                            next_world[w][z][y][x]['alive'] = True
    return next_world


def run_program(start_grid, iterations):
    world = make_start_world(start_grid, iterations)
    for i in range(iterations):
        world = get_next_world(world)
    return print_world(world)


def main():
    final = run_program(input_data, 6)
    print(final)


if __name__ == "__main__":
    main()
