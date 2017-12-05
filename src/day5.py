
def part1(sequence):
    idx = 0
    steps = 0
    maximum = len(sequence)
    while idx < maximum:
        steps += 1
        nextIdx = sequence[idx]
        sequence[idx] += 1
        idx += nextIdx

    return steps


def part2(sequence):
    idx = 0
    steps = 0
    maximum = len(sequence)
    while idx < maximum:
        steps += 1
        nextIdx = sequence[idx]
        sequence[idx] += 1 if sequence[idx] < 3 else -1
        idx += nextIdx

    return steps

with open("data/day5input.txt") as file:
    text = list(map(int, file.read().split("\n")))
    print("p1: , p2: %s" % ( part2(text)))
