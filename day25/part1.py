f = open('input.txt', 'r')
keys = f.read().strip().split('\n')
f.close()

def get_loop_size(sub_num, final):
    value = 1
    i = 1
    while i < 10000000:
        temp = value * sub_num
        value = temp % 20201227
        if value == final:
            return i
        i += 1
    print('didn\'t hit')


def do_loop(sub_num, loop):
    value = 1
    for i in range(loop):
        temp = value * sub_num
        value = temp % 20201227
    return value

def main():
    card_pub_key, door_pub_key = keys

    card_loop_size = get_loop_size(7, int(card_pub_key))

    print(card_loop_size)

    print(do_loop(int(door_pub_key), card_loop_size))



if __name__ == "__main__":
    main()