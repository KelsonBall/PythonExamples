dX = { 'R': 1, 'L': -1, 'U': 0, 'D' : 0 }
dY = { 'R': 0, 'L': 0, 'U': 1, 'D' : -1 }

with open("input.txt") as file:
    instructions = [line.strip().split(",") for line in file]

visited = { 0: set(), 1: set() }

for cable in range(2):
    x, y = 0, 0
    for instruction in instructions[cable]:
        direction, steps = instruction[0], int(instruction[1:])
        for i in range(steps):
            x += dX[direction]
            y += dY[direction]
            visited[cable].add((x, y))

intersections = visited[0] & visited[1]
distances = [abs(x) + abs(y) for x, y in intersections]
closest = min(distances)
print(closest)