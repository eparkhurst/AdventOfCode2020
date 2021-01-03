f = open('input.txt', 'r')
input_data = f.read().strip().split('\n')
f.close()


def run_program(input):
    print(input)
    return 7


def main():
    final = run_program('5 + (8 * 3 + 9 + 3 * 4 * 3)')
    print(final)


if __name__ == "__main__":
    main()