f = open('input.txt', 'r')
raw_decks = f.read().strip().split('\n\n')
f.close()


def string_round(d1, d2):
    string_d1 = [str(int) for int in d1]
    string_d2 = [str(int) for int in d2]
    round = 'd1'+ ''.join(string_d1)+ 'd2'+ ''.join(string_d2)
    return round

def play(deck1, deck2):
    d1 = deck1.copy()
    d2 = deck2.copy()
    pastRounds = []

    while True:
        round = string_round(d1,d2)
        if round in pastRounds:
            return ([1,2,3], [])
        else:
            pastRounds.append(round)

        c1 = d1.pop(0)
        c2 = d2.pop(0)

        if c1 >= len(d1) or c2 >= len(d2):
            if c1 > c2:
                d1 = d1 + [c1, c2]
            else:
                d2 = d2 + [c2, c1]
        else:
            r_d1 = d1[:c1]
            r_d2 = d2[:c2]
            sub_result = play(r_d1, r_d2)
            if len(sub_result[0]) > 1:
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
    print(ans)
    if len(ans[0]) > 1:
        get_score(ans[0])
    else:
        get_score(ans[1])


if __name__ == "__main__":
    main()
