def main() -> None:
    with open("input.txt") as file:
        scratchcards = []
        for index, line in enumerate(file.read().split("\n")):
            winning_nums_str, my_nums_str = line.split(": ")[1].split(" | ")
            winning_nums = [int(x) for x in filter(lambda x: x, winning_nums_str.split(" "))]
            my_nums = [int(x) for x in filter(lambda x: x, my_nums_str.split(" "))]
            matching_nums = [num for num in my_nums if num in winning_nums]
            scratchcards.append(1 * (2 ** (len(matching_nums) - 1) if matching_nums else 0,
                                list(range(index + 1, index + len(matching_nums) + 1))))
        total_points = sum(scratchcard[0] for scratchcard in scratchcards)
        total_scratchcards = 0
        queue = list(range(len(scratchcards)))
        while queue:
            index = queue.pop()
            total_scratchcards += 1
            queue.extend(scratchcards[index][1])
        print("Part One:", total_points)
        print("Part Two:", total_scratchcards)
            

if __name__ == "__main__":
    main()
