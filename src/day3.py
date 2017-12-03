import math


def position_formula(step):
    """
    https://math.stackexchange.com/questions/163080/on-a-two-dimensional-grid-is-there-a-formula-i-can-use-to-spiral-coordinates-in
    """
    k = math.ceil((math.sqrt(step) - 1) / 2)
    t = 2 * k + 1
    m = int(math.pow(t, 2))
    t = t - 1

    if step >= m - t:  return k - (m - step), -k
    m = m - t
    if step >= m - t:  return -k, -k + (m - step)
    m = m - t
    if step >= m - t:  return -k + (m - step), k
    return k, k - (m - step - t)


def part1(digit):
    """
    17  16  15  14  13
    18   5   4   3  12
    19   6   1   2  11
    20   7   8   9  10
    21  22  23---> ...

    Data from square 1 is carried 0 steps, since it's at the access port.
    Data from square 12 is carried 3 steps, such as: down, left, left.
    Data from square 23 is carried only 2 steps: up twice.
    Data from square 1024 must be carried 31 steps.
    """
    return sum(map(abs, position_formula(digit)))


def part2(maximum):
    """"
    147  142  133  122   59
    304    5    4    2   57
    330   10    1    1   54
    351   11   23   25   26
    362  747  806--->   ...
    """

    grid = {}
    for steps in range(1, maximum):
        """
        build the grid up to x steps
        """
        for step in range(1, steps + 1):
            location = position_formula(step)
            if location not in grid:
                neighbours = (
                    (location[0] + 1, location[1] - 1),
                    (location[0] + 1, location[1]),
                    (location[0] + 1, location[1] + 1),

                    (location[0], location[1] - 1),
                    (location[0], location[1] + 1),

                    (location[0] - 1, location[1] - 1),
                    (location[0] - 1, location[1]),
                    (location[0] - 1, location[1] + 1),
                )

                grid[location] = max(sum(grid[neighbour] for neighbour in neighbours if neighbour in grid), 1)

        loc = position_formula(steps)
        score = grid[loc] if loc in grid else 0
        if score > maximum:
            return score


for i in (1, 12, 23, 1024, 361527):
    print("%s: part1: %s  part2: %s" % (i, part1(i), part2(i)))
