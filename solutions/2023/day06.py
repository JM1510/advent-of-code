def part_one(lines, *args):
    times = list(map(int, lines[0].split(":")[1].split()))
    distances = list(map(int, lines[1].split(":")[1].split()))

    answer = 1

    for time, distance in zip(times, distances):
        victory_count = 0
        for i in range(time):
            if (time - i) * i > distance:
                victory_count += 1
        answer *= victory_count

    return answer


def part_two(lines, *args):
    time = int(lines[0].split(":")[1].replace(' ', ''))
    distance = int(lines[1].split(":")[1].replace(' ', ''))

    answer = 1

    victory_count = 0
    for i in range(time):
        if (time - i) * i > distance:
            victory_count += 1
    answer *= victory_count

    return answer
