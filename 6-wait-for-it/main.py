durations, distances = ([s for s in line.split()[1:] if s] for line in open("input.txt").read().split("\n"))


def product_of_ways_to_win(duration_distance_pairs: list[tuple[int, int]]) -> int:
    prod = 1
    for dur, dist in duration_distance_pairs:
        prod *= len([0 for vel in range(dur) if vel * (dur - vel) > dist])
    return prod


print("Part One:", product_of_ways_to_win(zip([int(d) for d in durations], [int(d) for d in distances])))
print("Part Two:", product_of_ways_to_win([(int(''.join(durations)), int(''.join(distances)))]))