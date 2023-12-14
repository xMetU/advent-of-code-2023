CARD_STRENGTHS = {"2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7,
                  "9": 8, "T": 9, "J": 10, "Q": 11, "K": 12, "A": 13}
CARD_STRENGTHS_WITH_JOKER = {**CARD_STRENGTHS, "J": 0}


hand_bid_pairs = [(hand, int(bid)) for hand, bid in [line.split() for line in open("input.txt").read().split("\n")]]


def get_strength(hand: str, card_strengths: dict[str, int] = CARD_STRENGTHS) -> tuple[int, tuple[int, int, int, int, int]]:
    match sorted([hand.count(c) for c in card_strengths.keys() if c in hand]):
        case [5]: hand_strength = 6
        case [1, 4]: hand_strength = 5
        case [2, 3]: hand_strength = 4
        case [1, 1, 3]: hand_strength = 3
        case [1, 2, 2]: hand_strength = 2
        case [1, 1, 1, 2]: hand_strength = 1
        case _: hand_strength = 0
    return (hand_strength, tuple(card_strengths[c] for c in hand))


def get_strength_with_jokers(hand: str) -> tuple[int, tuple[int, int, int, int, int]]:
    if "J" not in hand:
        return get_strength(hand)
    counts = {c: hand.count(c) for c in hand if c != "J"}
    candidate = max([k for k, v in counts.items() if v == max(counts.values())],
                     key=CARD_STRENGTHS_WITH_JOKER.get) if counts else "A"
    return (get_strength(hand.replace("J", candidate))[0], get_strength(hand, CARD_STRENGTHS_WITH_JOKER)[1])
    

hand_bid_pairs = sorted(hand_bid_pairs, key=lambda hbp: get_strength(hbp[0]))
print("Part One:", sum((rank + 1) * bid for rank, (_, bid) in enumerate(hand_bid_pairs)))

hand_bid_pairs = sorted(hand_bid_pairs, key=lambda hbp: get_strength_with_jokers(hbp[0]))
print("Part Two:", sum((rank + 1) * bid for rank, (_, bid) in enumerate(hand_bid_pairs)))
