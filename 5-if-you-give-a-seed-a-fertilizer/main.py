SUBJECT_NAMES = ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]

def main() -> None:
    with open("input.txt") as file:
        almanac: dict[str, dict[tuple[int, int], tuple[int, int]]] = {}
        subjects = file.read().split("\n\n")
        seeds = [int(s) for s in subjects.pop(0).split(": ")[1].split(" ")]
        for subject in subjects:
            name, src_dest_maps_str = subject.split(" map:\n")
            almanac[name] = {}
            for src_dest_map_str in src_dest_maps_str.split("\n"):
                dest, src, length = (int(s) for s in src_dest_map_str.split(" "))
                almanac[name][(src, src + length - 1)] = (dest, dest + length - 1)
        locations = []
        for seed in seeds:
            src_val = seed
            for i in range(len(SUBJECT_NAMES) - 1):
                for src_range, dest_range in almanac[SUBJECT_NAMES[i] + "-to-" + SUBJECT_NAMES[i + 1]].items():
                    if src_range[0] <= src_val <= src_range[1]:
                        src_val = dest_range[0] + src_val - src_range[0]
                        break
            locations.append(src_val)
        print("Part One:", min(locations))


if __name__ == "__main__":
    main()