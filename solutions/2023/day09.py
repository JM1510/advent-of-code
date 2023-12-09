import functools


def part_one(lines, *args):
    answer = 0

    for line in lines:
        answer += functools.reduce(
            lambda a, b: a + b, [list[-1] for list in _get_all_lists(line)]
        )

    return answer


def part_two(lines, *args):
    answer = 0

    for line in lines:
        answer += functools.reduce(
            lambda a, b: b - a, [list[0] for list in _get_all_lists(line)]
        )

    return answer


def _calculate_differences(input_list):
    result = []
    for i in range(len(input_list) - 1):
        result.append(input_list[i+1] - input_list[i])

    return result


def _get_all_lists(line):
    values = list(map(int, line.split()))
    all_lists = [values]
    current_list = values

    while True:
        new_list = _calculate_differences(current_list)
        all_lists.insert(0, new_list)
        current_list = new_list

        tmp_set = set(current_list)
        if len(tmp_set) == 1 and 0 in tmp_set:
            break

    return all_lists
