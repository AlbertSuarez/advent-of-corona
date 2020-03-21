import os

from src import DATA_FOLDER


def phase_1():
    with open(os.path.join(DATA_FOLDER, 'day_1_1.txt')) as input_file:
        content_file = str(input_file.read())
    sequence = [int(i) for i in content_file.split()]
    maximum = current = 0
    for idx in range(0, len(sequence)):
        if idx == 0 or (sequence[idx] > sequence[idx - 1] and sequence[idx] % 2 != sequence[idx - 1] % 2):
            current += 1
        else:
            current = 0
        if current > maximum:
            maximum = current
    print(f'Solution: {maximum}')


if __name__ == '__main__':
    phase_1()
