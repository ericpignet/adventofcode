total_priorities = 0
with open("2022/input_files/day03") as f:
    for data in f:
        data = data.strip()

        comp1 = data[0 : int(len(data) / 2)]
        comp2 = data[int(len(data) / 2) :]
        print(f"comp 1 = {comp1}")
        print(f"comp 2 = {comp2}")
        common_item = " "
        for item1 in comp1:
            for item2 in comp2:
                if item1 == item2:
                    common_item = item1
                    break
        print(f"Common item: {common_item}")
        priority = 0
        if common_item >= "a" and common_item <= "z":
            priority = ord(common_item) - ord("a") + 1
        else:
            priority = ord(common_item) - ord("A") + 27
        print(f"Priority: {priority}")
        total_priorities += priority
print(f"Total priorities: {total_priorities}")
