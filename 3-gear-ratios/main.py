def main() -> None:
    with open("input.txt") as file:
        engine_schematic = file.read()
        position_number_map: dict[tuple[int, int], str] = {}
        position_symbol_map: dict[tuple[int, int], str] = {}
        current_number = ""
        for index, char in enumerate(engine_schematic):
            if char.isdigit():
                current_number += char
            elif current_number:
                position_number_map[(index // 141, (index % 141) - len(current_number))] = current_number
                current_number = ""
            if char in "@#$%&*-+=/":
                position_symbol_map[(index // 141, index % 141)] = char
        part_one_total = 0
        for position, number in position_number_map.items():
            for r in range(position[0] - 1, position[0] + 2):
                for c in range(position[1] - 1, position[1] + len(number) + 1):
                    if (r, c) in position_symbol_map:
                        part_one_total += int(number)
                        break
                else:
                    continue
                break
        print("Part One:", part_one_total)


if __name__ == "__main__":
    main()
