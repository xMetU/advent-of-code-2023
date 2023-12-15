histories = [[int(s) for s in line.split()] for line in open("input.txt").read().split("\n")]


def get_next_value(history: list[int]) -> int:
    sequences = [history]
    while not all(n == 0 for n in sequences[-1]):
        sequences.append([sequences[-1][i + 1] - sequences[-1][i] for i in range(len(sequences[-1]) - 1)])
    for i in range(len(sequences) - 2, -1, -1):
        sequences[i].append(sequences[i][-1] + sequences[i + 1][-1])
    return sequences[0][-1]


def get_prev_value(history: list[int]) -> int:
    sequences = [history]
    while not all(n == 0 for n in sequences[-1]):
        sequences.append([sequences[-1][i + 1] - sequences[-1][i] for i in range(len(sequences[-1]) - 1)])
    for i in range(len(sequences) - 2, -1, -1):
        sequences[i] = [sequences[i][0] - sequences[i + 1][0]] + sequences[i]
    return sequences[0][0]


print("Part One:", sum(get_next_value(history) for history in histories))
print("Part Two:", sum(get_prev_value(history) for history in histories))
