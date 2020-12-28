f = open('input.txt', 'r')
input_data = f.read().strip().split(',')
f.close()


def run_program(data):
    return 'hey'


def main():
    final = run_program(input_data)
    print(final)


if __name__ == "__main__":
    main()
