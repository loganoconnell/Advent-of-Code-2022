import sys

start_pos, end_pos = (0, 0), (0, 0)
map, unvisited = [], []
history = dict()
width, height = 0, 0

# taken from /r/adventofcode - b/c why reinvent the wheel?
class Dijkstra:
    def __init__(self, unvisited, start_node, end_node, node_map):
        self.unvisited = unvisited
        self.visited = []
        self.start_node = start_node
        self.end_node = end_node
        self.node_map = node_map
        self.node_distance = dict(zip(unvisited, [sys.maxsize] * (height * width)))
        self.node_distance[start_node] = 0

    def visit(self, current_node):
        for node in self.node_map[current_node]:
            if node not in self.visited:
                if self.node_distance[current_node] + 1 < self.node_distance[node]:
                    self.node_distance[node] = self.node_distance[current_node] + 1
        self.unvisited.remove(current_node)
        self.visited.append(current_node)

    def run(self):
        while self.end_node not in self.visited:
            current_node = min(self.unvisited, key=self.node_distance.get)
            self.visit(current_node)
        return self.node_distance[self.end_node]

class Dijkstra2:
    def __init__(self, unvisited, start_node, end_nodes, node_map):
        self.unvisited = unvisited
        self.visited = []
        self.start_node = start_node
        self.end_nodes = end_nodes
        self.node_map = node_map
        self.node_distance = dict(zip(unvisited, [sys.maxsize] * (height * width)))
        self.node_distance[start_node] = 0

    def visit(self, current_node):
        for node in self.node_map[current_node]:
            if node not in self.visited:
                if self.node_distance[current_node] + 1 < self.node_distance[node]:
                    self.node_distance[node] = self.node_distance[current_node] + 1
        self.unvisited.remove(current_node)
        self.visited.append(current_node)

    def run(self):
        while not set(self.end_nodes).issubset(set(self.visited)):
            current_node = min(self.unvisited, key=self.node_distance.get)
            self.visit(current_node)
        return self.node_distance

def char_int(char):
    return ord(char) - ord('a')

with open("day12.txt") as file:
    for i, line in enumerate(file.readlines()):
        curr = line.strip()

        map.append([])

        for j, char in enumerate(curr):
            if char == "S":
                map[i].append(char_int("a"))
                start_pos = (i, j)
            elif char == "E":
                map[i].append(char_int("z"))
                end_pos = (i, j)
            else:
                map[i].append(char_int(char))

            unvisited.append((i, j))

width = len(map[0])
height = len(map)

for i in range(height):
    for j in range(width):
        to_visit = []

        for m in [-1, 0, 1]:
            for n in [-1, 0, 1]:
                if i + m in range(0, height) and j + n in range(0, width) and abs(n) + abs(m) == 1:
                    # will only execute when [m, n] = [-1, 0], [1, 0], [0, -1], [0, 1]
                    # AKA up, down, left, right
                    if map[i + m][j + n] - map[i][j] <= 1:
                        # if step is <= 1 char value
                        to_visit.append((i + m, j + n))

        history[(i, j)] = to_visit

graph = Dijkstra(unvisited, start_pos, end_pos, history)
print(f"PART 1: {graph.run()}")

# reset
start_pos = (0, 0)
map, unvisited, end_nodes = [], [], []
history = dict()
width, height = 0, 0

with open("day12.txt") as file:
    for i, line in enumerate(file.readlines()):
        curr = line.strip()

        map.append([])

        for j, char in enumerate(curr):
            if char == "S" or char == "a":
                map[i].append(char_int("a"))
                end_nodes.append((i, j))
            elif char == "E":
                map[i].append(char_int("z"))
                start_pos = (i, j)
            else:
                map[i].append(char_int(char))

            unvisited.append((i, j))

width = len(map[0])
height = len(map)

for i in range(height):
    for j in range(width):
        to_visit = []

        for m in [-1, 0, 1]:
            for n in [-1, 0, 1]:
                if i + m in range(0, height) and j + n in range(0, width) and abs(n) + abs(m) == 1:
                    # will only execute when [m, n] = [-1, 0], [1, 0], [0, -1], [0, 1]
                    # AKA up, down, left, right
                   if map[i + m][j + n] - map[i][j] >= -1:
                        # inverse of previous case since we're working backwords
                        to_visit.append((i + m, j + n))

        history[(i, j)] = to_visit

result = Dijkstra2(unvisited, start_pos, end_nodes, history).run()
x = result[min(end_nodes, key=result.get)]
print(f"PART 2: {x}")