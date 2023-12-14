card_strengths = {"2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7,
                  "9": 8, "T": 9, "J": 10, "Q": 11, "K": 12, "A": 13}

hand_bid_pairs = [(hand, int(bid)) for hand, bid in [line.split() for line in open("input.txt").read().split("\n")]]


def get_strength(hand: str) -> tuple[int, tuple[int, int, int, int, int]]:
    match sorted([hand.count(c) for c in card_strengths.keys() if c in hand]):
        case [5]: hand_strength = 6
        case [1, 4]: hand_strength = 5
        case [2, 3]: hand_strength = 4
        case [1, 1, 3]: hand_strength = 3
        case [1, 2, 2]: hand_strength = 2
        case [1, 1, 1, 2]: hand_strength = 1
        case _: hand_strength = 0
    return (hand_strength, tuple(card_strengths[c] for c in hand))


print("Part One:", sum((rank + 1) * bid for rank, (_, bid)
                       in enumerate(sorted(hand_bid_pairs, key=lambda hbp: get_strength(hbp[0])))))
