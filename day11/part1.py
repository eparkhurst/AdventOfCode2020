f = open('input.txt', 'r')
input_data = f.read().strip().split('\n')
f.close()


def get_occupancy(pos, lobby):
    current = lobby[pos[0]][pos[1]]
    if current == '.':
        return '.'
    directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    surroundings = 0
    for dir in directions:
        y = pos[0] + dir[0]
        x = pos[1] + dir[1]
        if y < 0 or y >= len(lobby):
            continue
        if x < 0 or x >= len(lobby[y]):
            continue
        spot = lobby[y][x]
        if spot == '#':
            surroundings += 1
    if current == 'L' and surroundings == 0:
        return '#'
    elif current == '#' and surroundings > 3:
        return 'L'
    return current


def find_stability(data):
    lobby = data.copy()
    while True:
        new_lobby = []
        for y in range(len(lobby)):
            for x in range(len(lobby[y])):
                if x == 0:
                    new_lobby.append([])
                new_lobby[y].append(get_occupancy((y, x), lobby))
        if new_lobby == lobby:
            return new_lobby
        else:
            lobby = new_lobby.copy()


def main():
    final = find_stability(input_data)
    final_count = 0
    for row in final:
        for seat in row:
            if seat == '#':
                final_count += 1
    print(final_count)


if __name__ == "__main__":
    main()
