f = open('input.txt', 'r')
input_data = f.read().strip().split('\n')
f.close()


def run_program(lines):
    return lines

def main():
    final = run_program(input_data)
    print(final)


if __name__ == "__main__":
    main()