class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def follow(H: Point, T: Point):
    aligned = T.x == H.x or T.y == H.y
    if T.y == H.y - 2:
        T.y += 1
        if not aligned:
            if T.x < H.x:
                T.x += 1
            elif T.x > H.x:
                T.x -= 1
    if T.x == H.x + 2:
        T.x -= 1
        if not aligned:
            if T.y < H.y:
                T.y += 1
            elif T.y > H.y:
                T.y -= 1
    if T.x == H.x - 2:
        T.x += 1
        if not aligned:
            if T.y < H.y:
                T.y += 1
            elif T.y > H.y:
                T.y -= 1
    if T.y == H.y + 2:
        T.y -= 1
        if not aligned:
            if T.x < H.x:
                T.x += 1
            elif T.x > H.x:
                T.x -= 1


inputs = []
with open("2022/input_files/day09") as f:
    for line in f:
        action, amount = line.rstrip().split()
        inputs.append([action, int(amount)])

visited = set()

# Part 1
# size_tail = 1
# Part 2
size_tail = 9

H = [Point(0, 0) for _ in range(size_tail + 1)]

for input in inputs:
    # print(f"{input=}")
    for i in range(input[1]):
        match input[0]:
            case "U":
                H[0].y += 1
            case "L":
                H[0].x -= 1
            case "R":
                H[0].x += 1
            case "D":
                H[0].y -= 1
        for j in range(1, size_tail + 1):
            follow(H[j - 1], H[j])
        visited.add((H[size_tail].x, H[size_tail].y))

        # display map:
        # for y in range(13, -14, -1):
        for y in range(size_tail, -1, -1):
            # for x in range(-13, 13):
            for x in range(0, size_tail):
                letter = "."
                for k in range(size_tail, -1, -1):
                    if H[k].x == x and H[k].y == y:
                        letter = str(k)
                # print(letter, end="")
            # print()
        # print()


nb_visited = len(visited)

print(f"{nb_visited=}")
