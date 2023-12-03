import re


def part_one(lines):
    answer = 0
    colors = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    for line in lines:
        game_id, game = line.replace(" ", "").split(":")

        counts = re.findall(r"(\d+)([red|blue|green]+)", game)

        for count, color in counts:
            if int(count) > colors[color]:
                break
        else:
            answer += int(re.sub(r"[^\d]", "", game_id))

    return answer


def part_two(lines):
    answer = 0
    colors = ["red", "green", "blue"]

    for line in lines:
        _, game = line.replace(" ", "").split(":")

        counts = re.findall(r"(\d+)([red|blue|green]+)", game)
        power = 1

        for color in colors:
            power *= max(
                [int(c[0]) for c in counts if c[1] == color]
            )

        answer += power

    return answer
