def part_one(lines, content):
    seeds, *category_maps = content.split('\n\n')

    seeds = list(map(int, seeds.split(":")[1].split()))

    for category_map in category_maps:
        ranges = [
            list(map(int, range))
            for range in [
                line.split() for line in category_map.split("\n")[1:] if line
            ]
        ]

        for i in range(len(seeds)):
            for dst_start, src_start, range_length in ranges:
                src_end = src_start + range_length - 1
                if src_start < seeds[i] and src_end > seeds[i]:
                    seeds[i] = dst_start + seeds[i] - src_start
                    break

    return min(seeds)


def part_two(lines, content):
    input_ranges, *category_maps = content.split('\n\n')
    input_ranges = list(map(int, input_ranges.split(":")[1].split()))

    seeds = []
    for i in range(0, len(input_ranges), 2):
        seeds.append(
            (input_ranges[i], (input_ranges[i] + input_ranges[i+1] - 1))
        )

    for category_map in category_maps:
        category_ranges = [
            list(map(int, range))
            for range in [
                line.split() for line in category_map.split("\n")[1:] if line
            ]
        ]

        tmp_seeds = []
        while seeds:
            seed_start, seed_end = seeds.pop()

            for dst_start, src_start, range_length in category_ranges:
                src_end = src_start + range_length - 1
                has_overlap, overlap = _has_overlap(
                    src_start, src_end, seed_start, seed_end
                )
                if has_overlap:
                    shift = dst_start - src_start
                    tmp_seeds.append(
                        (overlap[0] + shift, overlap[1] + shift)
                    )
        seeds = tmp_seeds

    return min(seeds)[0]


def _has_overlap(a1, a2, b1, b2):
    overlap = None

    overlap_start = max(a1, b1)
    overlap_end = min(a2, b2)

    if overlap_start < overlap_end:
        overlap = (overlap_start, overlap_end)

    return overlap_start < overlap_end, overlap
