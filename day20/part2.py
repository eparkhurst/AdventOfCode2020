import math

f = open('input.txt', 'r')
raw_tiles = f.read().strip().split('\n\n')
f.close()


def make_dict(tiles):
    tile_dict = {}
    for tile in tiles:
        lines = tile.split('\n')
        tile_id = lines[0].split(' ')[1][0:-1]
        tile_dict[tile_id] = {
            'borders': get_border(tile.split('\n')[1:]),
            'adjacent': [None, None, None, None, None, None, None, None],
            'raw': lines[1:],
            'id': tile_id
        }
    return tile_dict


def add_adjacent(tile_dict):
    for tile in tile_dict:
        for i, border in enumerate(tile_dict[tile]['borders']):
            for tile2 in tile_dict:
                if tile != tile2 and border in tile_dict[tile2]['borders'][0:4]:
                    tile_dict[tile]['adjacent'][i] = tile2


def get_border(tile_arr):
    left = []
    right = []
    for line in tile_arr:
        left.append(line[0])
        right.append(line[-1])
    return [tile_arr[0], ''.join(right), tile_arr[-1], ''.join(left), tile_arr[0][::-1], ''.join(right)[::-1], tile_arr[-1][::-1], ''.join(left)[::-1]]


def build_image(start_id, tile_dict):
    dict_list = [get_first_row(start_id, tile_dict)]
    width = int(math.sqrt(len(tile_dict)))
    # for i in range(int(width - 1)):
    for j in range(width):
        above = dict_list[0][j]
        print(above)
        next_id = above['adjacent'][2]
        current = tile_dict[next_id]
        print(current['adjacent'])
        print(current['adjacent'].index(above['id']))


def get_first_row(start_id, tile_dict):
    image = []
    width = math.sqrt(len(tile_dict))
    rotate_right(tile_dict[start_id], 1)
    image.append(tile_dict[start_id])

    next_id = tile_dict[start_id]['adjacent'][1]
    current_id = start_id
    for i in range(int(width - 1)):
        print(next_id)
        if current_id not in tile_dict[next_id]['adjacent'][0:4]:
            print(tile_dict[next_id]['adjacent'])
            return
        while tile_dict[next_id]['adjacent'][3] != current_id:
            rotate_right(tile_dict[next_id])
        image.append(tile_dict[next_id])
        current_id = next_id
        next_id = tile_dict[current_id]['adjacent'][1]
    return image


def join_image(raw, width=3):
    final = []
    for i, tile in enumerate(raw):
        for j, row in enumerate(tile):
            if i == 0:
                final.append([row])
            else:
                final[j].append(row)
    for i, arr in enumerate(final):
        final[i] = ''.join(final[i])
    return final


def rotate_right(raw_tile, n=1):
    final = raw_tile['raw']
    for turn in range(n):
        tile = []
        for i, line in enumerate(final):
            for j, char in enumerate(line):
                if i == 0:
                    tile.append([])
                tile[j].insert(0, char)
        for i, arr in enumerate(tile):
            tile[i] = ''.join(tile[i])
        final = tile
        front = raw_tile['adjacent'][0:4]
        back = raw_tile['adjacent'][4:]
        front.insert(0, front.pop())
        back.insert(0, back.pop())
        raw_tile['adjacent'] = front + back
    raw_tile['raw'] = final
    raw_tile['borders'] = get_border(final)

# def flip_v(tile):
#     tile['borders'][0] = tile['borders'][0][::-1]
#     tile['borders'][2] = tile['borders'][2][::-1]
#
# def flip_h(tile):
#     tile['borders'][1] = tile['borders'][1][::-1]
#     tile['borders'][3] = tile['borders'][3][::-1]


def print_to_console(arr):
    for line in arr:
        print(line)


def main():
    tile_dict = make_dict(raw_tiles)
    add_adjacent(tile_dict)
    for tile in tile_dict:
        sides = 0
        for i, adj in enumerate(tile_dict[tile]['adjacent']):
            if adj is not None:
                sides += 1
        if sides == 2:
            build_image(tile, tile_dict)
            return


if __name__ == "__main__":
    main()
