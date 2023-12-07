CUBE_LIMITS = {"red": 12, "green": 13, "blue": 14}


def main() -> None:
    with open("input.txt") as file:
        game_information = file.read()
        part_one_total = 0
        part_two_total = 0
        for line in game_information.split("\n"):
            id_str, handfuls_str = line.split(": ")
            id = int(id_str[5:])
            is_possible = True
            min_cubes = {"red": 0, "green": 0, "blue": 0}
            for handful_str in handfuls_str.split("; "):
                for cube_str in handful_str.split(", "):
                    count_str, colour_str = cube_str.split(" ")
                    count = int(count_str)
                    if count > CUBE_LIMITS[colour_str]:
                        is_possible = False
                    if count > min_cubes[colour_str]:
                        min_cubes[colour_str] = count 
            if is_possible:
                part_one_total += int(id_str[5:])
            part_two_total += min_cubes["red"] * min_cubes["green"] * min_cubes["blue"]
        print("Part One:", part_one_total)
        print("Part Two:", part_two_total)


if __name__ == "__main__":
    main()
