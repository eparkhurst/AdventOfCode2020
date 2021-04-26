import math
import find_monster
f = open('day20/input.txt', 'r')
# f = open('input.txt', 'r')
raw = f.read()
orig_tiles = raw.strip().split('\n\n')
f.close()


def make_dict(tiles):
    tile_dict = {}
    for tile in tiles:
        lines = tile.split('\n')
        tile_id = lines[0].split(' ')[1][0:-1]
        tile_dict[tile_id] = {
            # 'borders': get_border(tile.split('\n')[1:])
            'borders': [],
            'adjacent': [None, None, None, None, None, None, None, None],
            'raw': lines[1:],
            'id': tile_id
        }
    return tile_dict


def add_adjacent(tile_dict):
    for tile in tile_dict:
        tile_dict[tile]['adjacent'] = [None, None, None, None, None, None, None, None]
        for i, border in enumerate(tile_dict[tile]['borders']):
            for tile2 in tile_dict:
                if tile != tile2 and border in tile_dict[tile2]['borders'][4:]:
                    tile_dict[tile]['adjacent'][i] = tile2

def add_borders(tile_dict):
    for tile in tile_dict:
        tile_dict[tile]['borders'] = get_border(tile_dict[tile]['raw'])

def get_border(tile_arr):
    left = []
    right = []
    for line in tile_arr:
        left.append(line[0])
        right.append(line[-1])
    return [tile_arr[0], ''.join(right), tile_arr[-1][::-1], ''.join(left)[::-1], tile_arr[0][::-1], ''.join(right)[::-1], tile_arr[-1], ''.join(left)]


def build_image(start_id, tile_dict):
    dict_list = [get_first_row(start_id, tile_dict)]
    width = int(math.sqrt(len(tile_dict)))
    # for i in range(int(width - 1)):
    dict_list.append([])
    for j in range(width):
        above = dict_list[0][j]
        next_id = above['adjacent'][2]
        current = tile_dict[next_id]
        while tile_dict[next_id]['adjacent'][0] != above['id']:
            rotate_right(tile_dict[next_id])
            fill_dict(tile_dict)
        dict_list[1].append(tile_dict[next_id])

    dict_list.append([])
    for j in range(width):
        above = dict_list[1][j]
        next_id = above['adjacent'][2]
        current = tile_dict[next_id]
        while tile_dict[next_id]['adjacent'][0] != above['id']:
            rotate_right(tile_dict[next_id])
        dict_list[2].append(tile_dict[next_id])
    return make_image(dict_list)

def make_image(dict_list):
    image = [[],[],[]]
    final = ''
    for i, row in enumerate(dict_list):
        for j, tile in enumerate(row):
            for k, line in enumerate(tile['raw']):
                if k == 0 or k == 9:
                    continue
                if j == 0:
                    image[i].append(line[1:9])
                else:
                    image[i][k-1] += line[1:9]
                if j == 2:
                    final += image[i][k-1] +'\n'
    return final


def get_first_row(start_id, tile_dict):
    image = []
    width = math.sqrt(len(tile_dict))
    image.append(tile_dict[start_id])

    next_id = tile_dict[start_id]['adjacent'][1]
    current_id = start_id
    for i in range(int(width - 1)):
        if current_id not in tile_dict[next_id]['adjacent'][0:4]:
            print(tile_dict[next_id]['adjacent'])
            return
        while tile_dict[next_id]['adjacent'][3] != current_id:
            rotate_right(tile_dict[next_id])
        image.append(tile_dict[next_id])
        current_id = next_id
        next_id = tile_dict[current_id]['adjacent'][1]
    return image

def rotate_right(orig_tile, n=1):
    final = orig_tile['raw']
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
        front = orig_tile['adjacent'][0:4]
        back = orig_tile['adjacent'][4:]
        front.insert(0, front.pop())
        back.insert(0, back.pop())
        orig_tile['adjacent'] = front + back
    orig_tile['raw'] = final
    orig_tile['borders'] = get_border(final)


def fill_dict(tile_dict):
    add_borders(tile_dict)
    add_adjacent(tile_dict)

def check_adjacent(adjacent):
    for ad in adjacent:
        if ad is not None:
            return True
    return False

def flip_tile(orig_tile):
    raw = orig_tile['raw']
    next_raw = []
    for line in raw:
        next_raw.append(line[::-1])
    orig_tile['raw'] = next_raw

def organize_tiles(tile_dict):
    for tile in tile_dict:
        sides = 0
        for i, adj in enumerate(tile_dict[tile]['adjacent']):
            if adj is not None:
                sides += 1
        if sides == 2:
            if tile_dict[tile]['adjacent'][1] is not None and tile_dict[tile]['adjacent'][2] is not None:
                return build_image(tile, tile_dict)


def check_none(tile_dict):
    for tile in tile_dict:
        if not check_adjacent(tile_dict[tile]['adjacent'][0:4]):
            flip_tile(tile_dict[tile])
            fill_dict(tile_dict)
            return False
    return True
def main():
    tile_dict = make_dict(orig_tiles)
    fill_dict(tile_dict)
    done = False
    while not done:
        done = check_none(tile_dict)

    image = organize_tiles(tile_dict)
    find_monster.get_chop(image)




if __name__ == "__main__":
    main()
