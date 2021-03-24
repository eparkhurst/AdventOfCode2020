

def mixCups(cups):
    current_cup = cups[0]
    out = cups[1:4]
    del cups[1:4]
    dest_cup = current_cup - 1
    while True:
        if dest_cup < 1: dest_cup = 9
        if dest_cup in cups:
            index = cups.index(dest_cup)
            break
        dest_cup -= 1
    cups[index+1:index+1] = out
    first = cups.pop(0)
    cups.append(first)
    print(cups)
    return cups

def main():
    cup_labels = '716892543'
    cup_list = [int(i) for i in cup_labels]

    for i in range(100):
        cup_list = mixCups(cup_list)

    one_index = cup_list.index(1)
    l = cup_list[one_index+1:]
    f = cup_list[:one_index]
    final_list = l + f
    f = ''
    final = [str(i) for i in final_list]
    print(''.join(final))

if __name__ == "__main__":
    main()