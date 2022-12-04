total_priorities = 0
with open("2022/input_files/day03") as f:
    while True:
        data = []
        data.append(f.readline().strip())
        if not data[0]:
            break
        data.append(f.readline().strip())
        data.append(f.readline().strip())

        print(f"data = {data}")
        common_item = list(
            set(data[0]).intersection(set(data[1]).intersection(set(data[2])))
        )[0]
        # Equivalent to:
        # for item in data[0]:
        #     if item in data[1] and item in data[2]:
        #         common_item = item
        print(f"Common item: {common_item}")
        priority = 0
        if common_item >= "a" and common_item <= "z":
            priority = ord(common_item) - ord("a") + 1
        else:
            priority = ord(common_item) - ord("A") + 27
        print(f"Priority: {priority}")
        total_priorities += priority
print(f"Total priorities: {total_priorities}")
