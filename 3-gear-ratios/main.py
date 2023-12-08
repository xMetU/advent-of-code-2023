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
        gear_position_adjacent_numbers_map = {k: [] for k, v in position_symbol_map.items() if v == "*"}
        for position, number in position_number_map.items():
            is_part_number = False
            for r in range(position[0] - 1, position[0] + 2):
                for c in range(position[1] - 1, position[1] + len(number) + 1):
                    if (r, c) in position_symbol_map:
                        is_part_number = True
                    if (r, c) in gear_position_adjacent_numbers_map:
                        gear_position_adjacent_numbers_map[(r, c)].append(int(number))
            if is_part_number:
                part_one_total += int(number)
        print("Part One:", part_one_total)
        print("Part Two:", sum(nums[0] * nums[1] for nums in gear_position_adjacent_numbers_map.values() if len(nums) > 1))


if __name__ == "__main__":
    main()
