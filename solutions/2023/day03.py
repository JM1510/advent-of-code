import re
from operator import mul


def part_one(lines):
    matrix = [list(line) for line in lines]
    m = len(matrix)
    parts = []

    for i, line in enumerate(lines):
        for match in re.finditer(r"[^\d.]", line):
            adjacent_numbers = set()

            cells = get_adjacent_cells(i, match.start(), m, len(line))

            for row, column in cells:
                value = matrix[row][column]

                if value.isdigit():
                    adjacent_numbers.add(
                        get_adjacent_number(row, column, matrix[row])
                    )

            parts.extend(adjacent_numbers)

    return sum(parts)


def part_two(lines):
    answer = 0
    matrix = [list(line) for line in lines]
    m = len(matrix)

    for i, line in enumerate(lines):
        for match in re.finditer(r"[\*]", line):
            adjacent_numbers = set()

            cells = get_adjacent_cells(i, match.start(), m, len(line))

            for row, column in cells:
                value = matrix[row][column]

                if value.isdigit():
                    adjacent_numbers.add(
                        get_adjacent_number(row, column, matrix[row])
                    )

            if len(adjacent_numbers) == 2:
                answer += mul(*adjacent_numbers)

    return answer


def get_adjacent_cells(r, c, m, n):
    result = []

    for x, y in [
        (r + i, c + j)
        for i in (-1, 0, 1)
        for j in (-1, 0, 1)
        if i != 0 or j != 0
    ]:
        if 0 <= x < m and 0 <= y < n:
            result.append((x, y))

    return result


def get_adjacent_number(r, c, line):
    n = len(line)
    number = ''

    # Find the beginning of the number
    for i in range(c, -1, -1):
        if line[i].isdigit():
            number = line[i] + number
        else:
            break

    # Find the end of the number
    for i in range(c + 1, n):
        if line[i].isdigit():
            number = number + line[i]
        else:
            break

    return int(number)
