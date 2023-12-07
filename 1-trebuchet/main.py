DIGITS_MAP = {
    "oneight": "18",
    "twone": "21",
    "threeight": "38",
    "fiveight": "58",
    "sevenine": "79",
    "eightwo": "82",
    "eighthree": "83",
    "nineight": "98",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8", 
    "nine": "9"
}


def extract_digits(line: str) -> int:
    left_digit = None
    right_digit = None
    for i in range(len(line)):
        if left_digit and right_digit:
            break
        if not left_digit and line[i].isdigit():
            left_digit = line[i]
        if not right_digit and line[-i - 1].isdigit():
            right_digit = line[-i - 1]
    return int(left_digit + right_digit)


def main() -> None:
    with open("input.txt") as file:
        calibration_document = file.read()
        part_one_total = 0
        part_two_total = 0
        for line in calibration_document.split("\n"):
            part_one_total += extract_digits(line)
            for digit in DIGITS_MAP:
                line = line.replace(digit, DIGITS_MAP[digit])
            part_two_total += extract_digits(line)
        print("Part One:", part_one_total)
        print("Part Two:", part_two_total)


if __name__ == "__main__":
    main()
