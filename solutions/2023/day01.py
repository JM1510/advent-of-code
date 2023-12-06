import re


def part_one(lines, *args):
    answer = 0

    for line in lines:
        extracted_numbers = re.sub(r'[^\d]', '', line)
        answer += int(extracted_numbers[0] + extracted_numbers[-1])

    return answer


def part_two(lines, *args):
    answer = 0

    numbers = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e"
    }

    for line in lines:
        for key, value in numbers.items():
            line = line.replace(key, value)
        extracted_numbers = re.sub(r'[^\d]', '', line)
        number = extracted_numbers[0] + extracted_numbers[-1]
        answer += int(number)

    return answer
