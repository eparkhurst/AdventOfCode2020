import re


def get_chop(image):
    print(image.count('#'))
    print(image)
    k = 24
    monsters = 0
    i = 0
    while monsters < 1:
        if i > 8:
            print('failed')
            return
        if i == 4:
            image = flip_tile(image)
        monsters = len(re.findall('#..{'+str(k-19)+'}#.{4}##.{4}##.{4}###.{'+str(k-19)+'}.#.{2}#.{2}#.{2}#.{2}#.{2}#.{3}', image, re.DOTALL))
        image = rotate_right(image)
        i += 1
    print(monsters)
    answer = image.count('#')-(monsters*15)
    print(image)

    # list_image = image.split('\n')
    # found = check_rotation(list_image)
    # if found: 
    #     print('got it')
    #     return True
    # else:
    #     flipped = flip_tile(list_image)
    #     check_rotation(flipped)

def check_for_monsters(image):
    print('run')
    for i, row in enumerate(image):
        m = re.search('#....##....##....###', row)
        if(m):
            first = re.search('..................#.', row)
            third = re.search('.#..#..#..#..#..#',image[i+1])
            print(first.span())
            print(m.span())
            print(third.span())
            print('\n'.join(image))
            return True
    return False

def check_rotation(image):
    for i in range(4):
            x = check_for_monsters(image)
            if(x):
                print('yeah')
                return True
            else:
                image = rotate_right(image)
    return False

def rotate_right(image):
    tile = []
    list_image = image.split('\n')
    for i, line in enumerate(list_image):
        for j, char in enumerate(line):
            if i == 0:
                tile.append('')
            tile[j] = char + tile[j]
    return '\n'.join(tile)

def flip_tile(orig_tile):
    list_image = orig_tile.split('\n')
    next_raw = []
    for line in list_image:
        next_raw.append(line[::-1])
    return '\n'.join(next_raw)

#273 too low
#288 too low
#303 too low
