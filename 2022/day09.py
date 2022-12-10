class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def get_closer(H: Point, T: Point, axis: str, aligned: bool) -> bool:
    diff = getattr(T, axis) - getattr(H, axis)
    if abs(diff) == 2:
        get_closer_by_1(H, T, axis)
        if not aligned:
            get_closer_by_1(H, T, "y" if axis == "x" else "x")
        return True
    return False


def get_closer_by_1(H: Point, T: Point, axis):
    setattr(
        T, axis, getattr(T, axis) + (1 if getattr(H, axis) > getattr(T, axis) else -1)
    )


def follow(H: Point, T: Point):
    aligned = T.x == H.x or T.y == H.y
    if not get_closer(H, T, "y", aligned):
        get_closer(H, T, "x", aligned)


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
