# Recursive function. I could also have used a while(True), deleting from the list at each step
def filter_list(values: list, idx: int, is_oxygen: bool):
    if len(values) == 1:
        return values
    nb_1 = 0
    nb_0 = 0
    for data in values:
        nb_1 += 1 if data[idx] == "1" else 0
        nb_0 += 1 if data[idx] == "0" else 0
    if is_oxygen:  # most common
        to_keep = "1" if nb_1 >= nb_0 else "0"
    else:  # least common
        to_keep = "1" if nb_1 < nb_0 else "0"
    res = [item for item in values if item[idx] == to_keep]
    print(f"nb_1={nb_1} nb_0={nb_0} idx={idx} to_keep={to_keep} res={res}")
    return filter_list(res, idx + 1, is_oxygen)


all_data = []
with open("2021/input_files/day03") as f:
    for data in f:
        data = data.strip()
        print(f"data: {data}")
        all_data.append(data)
oxygen = filter_list(all_data, 0, True)[0]
co2 = filter_list(all_data, 0, False)[0]
print(f"oxygen: {oxygen} {int(oxygen, 2)}")
print(f"co2: {co2} {int(co2, 2)}")

print(f"Result: {int(oxygen, 2)*int(co2, 2)}")
