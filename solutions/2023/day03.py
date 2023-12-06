import re
from operator import mul


def part_one(lines, *args):
    matrix = [list(line) for line in lines]
    parts = []

    for i, line in enumerate(lines):
        for match in re.finditer(r"[^\d.]", line):
            adjacent_numbers = get_all_adjacent_numbers(
                i, match.start(), matrix
            )

            parts.extend(adjacent_numbers)

    return sum(parts)


def part_two(lines, *args):
    answer = 0
    matrix = [list(line) for line in lines]

    for i, line in enumerate(lines):
        for match in re.finditer(r"[\*]", line):
            adjacent_numbers = get_all_adjacent_numbers(
                i, match.start(), matrix
            )

            if len(adjacent_numbers) == 2:
                answer += mul(*adjacent_numbers)

    return answer


def get_all_adjacent_numbers(row, column, matrix):
    adjacent_numbers = set()

    cells = get_adjacent_cells(row, column, len(matrix), len(matrix[row]))

    for row, column in cells:
        value = matrix[row][column]

        if value.isdigit():
            adjacent_numbers.add(
                get_number(row, column, matrix[row])
            )

    return adjacent_numbers


def get_adjacent_cells(row, column, m, n):
    result = []

    for r, c in [
        (row + dx, column + dy)
        for dx in (-1, 0, 1)
        for dy in (-1, 0, 1)
        if dx != 0 or dy != 0
    ]:
        if 0 <= r < m and 0 <= c < n:
            result.append((r, c))

    return result


def get_number(row, column, line):
    number = ''

    # Find the beginning of the number
    for i in range(column, -1, -1):
        if line[i].isdigit():
            number = line[i] + number
        else:
            break

    # Find the end of the number
    for i in range(column + 1, len(line)):
        if line[i].isdigit():
            number = number + line[i]
        else:
            break

    return int(number)
