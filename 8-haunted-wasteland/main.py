from math import lcm

instructions, network = open("input.txt").read().split("\n\n")
network = {key: tuple(value.replace("(", "").replace(")", "").split(", "))
           for key, value in (line.split(" = ") for line in network.split("\n"))}


def next_node(node: str, step: str) -> str:
    return network[node][0] if step == "L" else network[node][1]


step_count = 0
cur_node = "AAA"
while cur_node != "ZZZ":
    cur_node = next_node(cur_node, instructions[step_count % (len(instructions))])
    step_count += 1
print("Part One:", step_count)


step_count = 0
cur_nodes = [node for node in network.keys() if node[-1] == "A"]
step_counts = []
while cur_nodes:
    index = instructions[step_count % (len(instructions))]
    cur_nodes = [next_node(node, index) for node in cur_nodes]
    step_count += 1
    step_counts.extend(step_count for node in cur_nodes if node[-1] == "Z")
    cur_nodes = [node for node in cur_nodes if node[-1] != "Z"]
print("Part Two:", lcm(*step_counts))