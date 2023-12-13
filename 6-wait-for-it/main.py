durations, distances = ([int(s) for s in line.split()[1:] if s] for line in open("input.txt").read().split("\n"))


ways_to_win_product = 1
for duration, distance in zip(durations, distances):
    ways_to_win = 0
    for i in range(duration):
        if i * (duration - i) > distance:
            ways_to_win += 1
    ways_to_win_product *= ways_to_win


print("Part One:", ways_to_win_product)