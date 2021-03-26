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


def count_floor(floor):
    total = 0
    for x in floor:
        for y in floor[x]:
            if floor[x][y]:
                total += 1
    print(total)

def main():
    floor = get_floor()
    count_floor(floor)



if __name__ == "__main__":
    main()