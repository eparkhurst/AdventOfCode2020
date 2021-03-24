f = open('input.txt', 'r')
raw_decks = f.read().strip().split('\n\n')
f.close()


def play(d1, d2):
    while True:
        c1 = d1.pop(0)
        c2 = d2.pop(0)
        if c1 > c2:
            d1 = d1 + [c1, c2]
        else:
            d2 = d2 + [c2, c1]
        if len(d1) < 1 or len(d2) < 1:
            return (d1, d2)


def get_score(deck):
    deck.reverse()
    final = 0
    for i, num in enumerate(deck):
        final += (i + 1) * num
    print(final)


def main():
    deck1 = [ int(x) for x in raw_decks[0].split('\n')[1:] ]
    deck2 = [ int(x) for x in raw_decks[1].split('\n')[1:] ]

    ans = play(deck1, deck2)
    if len(ans[0]) > 1:
        get_score(ans[0])
    else:
        get_score(ans[1])


if __name__ == "__main__":
    main()
