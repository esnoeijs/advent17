import itertools

"""
 5 1 9 5
 7 5 3
 2 4 6 8
 The first row's largest and smallest values are 9 and 1, and their difference is 8.
 The second row's largest and smallest values are 7 and 3, and their difference is 4.
 The third row's difference is 6.
"""
def part1(text):
    return sum(abs(max(rowInts) - min(rowInts)) for rowInts in
               (list(map(int, row)) for row in
                (line.split() for line in text.split("\n"))))

"""
5 9 2 8
9 4 7 3
3 8 6 5
In the first row, the only two numbers that evenly divide are 8 and 2; the result of this division is 4.
In the second row, the two numbers are 9 and 3; the result is 3.
In the third row, the result is 2.
In this example, the sum of the results would be 4 + 3 + 2 = 9.

What is the sum of each row's result in your puzzle input?
"""
def part2(text):
    return int(sum(list(filter(lambda x: x.is_integer(), map(lambda pair: pair[0]/pair[1] if (pair[0]/pair[1]).is_integer() else pair[1]/pair[0], itertools.combinations(rowInts, 2))))[0] for rowInts in
            (list(map(int, row)) for row in
             (line.split() for line in text.split("\n")))))

with open("data/day2input.txt") as file:
    text = file.read()
    print(part1(text))
    print(part2(text))