from collections import deque
import llist

def make_pretty(dict):
    next = 1
    string = ''
    for i in range(len(dict)):
        temp = dict[next]
        string += str(temp)
        next = temp
    return string

def move_cups(dict, max):
    current = 7
    last = len(dict)
    for i in range(max):
        f_o = dict[current]
        m_o = dict[dict[current]]
        l_o = dict[dict[dict[current]]]

        dict[current] = dict[l_o]

        dest = current -1
        while True:
            if dest == 0:
                dest = last
            if dest == f_o or dest == m_o or dest == l_o:
                dest -= 1
            else: break
        temp = dict[dest]
        dict[dest] = f_o
        dict[l_o] = temp
        current = dict[current]

    first = dict[1]
    second = dict[dict[1]]
    print(first)
    print(second)
    print(first*second)


def main():
    cup_labels = '716892543'
    num_cups = 1000000
    iterations = 10000000

    dict = {}
    length = len(cup_labels)
    first = int(cup_labels[0])
    for i, num in enumerate(cup_labels):
        if i == length -1:
            dict[int(num)] = 10
        else:
            dict[int(num)] = int(cup_labels[i+1])
    for num in range(10, num_cups + 1):
        if num == num_cups:
            dict[num] = first
        else:
            dict[num] = num + 1
    move_cups(dict, iterations)

if __name__ == "__main__":
    main()