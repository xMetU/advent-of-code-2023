instructions, network = open("input.txt").read().split("\n\n")
network = {key: tuple(value.replace("(", "").replace(")", "").split(", "))
           for key, value in (line.split(" = ") for line in network.split("\n"))}


count = 0
current = "AAA"
while current != "ZZZ":
    current = network[current][0] if instructions[count % (len(instructions))] == "L" else network[current][1]
    count += 1


print("Part One:", count)
