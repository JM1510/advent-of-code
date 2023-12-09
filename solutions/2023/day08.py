import re
import math


def part_one(lines, content):
    instructions = lines.pop(0)

    nodes = _create_nodes(lines)

    counter = 0
    current_position = "AAA"

    while current_position != "ZZZ":
        instruction = instructions[counter % len(instructions)]

        current_position = nodes[current_position][instruction]

        counter += 1

    return counter


def part_two(lines, *args):
    instructions = lines.pop(0)

    nodes = _create_nodes(lines)

    initial_nodes = [key for key in nodes.keys() if key[-1] == "A"]
    counters = []

    for node in initial_nodes:
        counter = 0
        position = node

        while position[-1] != 'Z':
            instruction = instructions[counter % len(instructions)]

            position = nodes[position][instruction]

            counter += 1

        counters.append(counter)

    return math.lcm(*counters)


def _create_nodes(lines):
    nodes = {}
    for line in lines:
        node_data = re.match(
            r'(?P<value>[\w]+)=\((?P<left>[\w]+),(?P<right>[\w]+)\)',
            line.replace(' ', '')
        )

        # # Create all nodes
        nodes[node_data.group("value")] = {
            "L": node_data.group("left"),
            "R": node_data.group("right")
        }

    return nodes
