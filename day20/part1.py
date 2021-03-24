f = open('input.txt', 'r')
raw_tiles = f.read().strip().split('\n\n')
f.close()

def make_dict(tiles):
    tile_dict = {}
    for tile in tiles:
        tile_dict[tile.split('\n')[0]] = {
            'borders': get_border(tile),
            'adjacent': [None, None, None, None, None, None, None, None]
        }
    return tile_dict


def add_adjacent(tile_dict):
    for tile in tile_dict:
        for i, border in enumerate(tile_dict[tile]['borders']):
            for tile2 in tile_dict:
                if tile != tile2 and border in tile_dict[tile2]['borders']:
                    tile_dict[tile]['adjacent'][i] = tile2


def get_border(tile):
    tile_arr = tile.split('\n')[1:]
    left = []
    right = []
    for line in tile_arr:
        left.append(line[0])
        right.append(line[-1])
    return [tile_arr[0], ''.join(right), tile_arr[-1], ''.join(left), tile_arr[0][::-1], ''.join(right)[::-1], tile_arr[-1][::-1], ''.join(left)[::-1]]

# def flip_v(tile):
#     tile['borders'][0] = tile['borders'][0][::-1]
#     tile['borders'][2] = tile['borders'][2][::-1]
#
# def flip_h(tile):
#     tile['borders'][1] = tile['borders'][1][::-1]
#     tile['borders'][3] = tile['borders'][3][::-1]

def main():
    tile_dict = make_dict(raw_tiles)
    add_adjacent(tile_dict)
    total = 1
    for tile in tile_dict:
        sides = 0
        for i, adj in enumerate(tile_dict[tile]['adjacent']):
            if adj is not None:
                sides += 1
        if sides == 4:
            num = tile.split(' ')[1][0:-1]
            print(num)
            total *= int(num)
    print(total)

if __name__ == "__main__":
    main()
