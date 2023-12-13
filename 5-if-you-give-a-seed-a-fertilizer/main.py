seeds, *almanac = open("input.txt").read().split("\n\n")
seeds = [int(s) for s in seeds.split()[1:]]
almanac = {name: {(int(src), int(src) + int(length) - 1): int(dest) - int(src)
                  for dest, src, length in (map.split() for map in maps.split("\n") if map)}
           for mapping in almanac for name, maps in [mapping.split(" map:\n")]}


def get_location_single(seed: int) -> int:
    for mappings in almanac.values():
        for (m_st, m_ed), diff in mappings.items():
            if m_st < seed < m_ed:
                seed += diff
                break
    return seed


def get_location_range(seed: tuple[int, int]) -> int:
    ranges = {seed}
    for (m_st, m_ed), diff in {mapping: difference for mappings in almanac.values()
                               for mapping, difference in mappings.items()}.items():
        new_ranges = set()
        while ranges:
            s_st, s_ed = ranges.pop()
            before = (s_st, min(s_ed, m_st))
            inter = (max(s_st, m_st), min(s_ed, m_ed))
            after = (max(s_st, m_ed), s_ed)
            if before[1] >= before[0]:
                new_ranges.add(before)
            if inter[1] >= inter[0]:
                new_ranges.add((inter[0] + diff, inter[1] + diff))
            if after[1] >= after[0]:
                new_ranges.add(after)
        if new_ranges:
            ranges = new_ranges
    return min(st for st, _ in ranges)


print("Part One", min(get_location_single(seed) for seed in seeds))
print("Part Two", min(get_location_range((seeds[i], seeds[i] + seeds[i + 1])) for i in range(len(seeds) - 1)))
