def flip_binary(val: str):
    res = ""
    for c in val:
        res += "0" if c == "1" else "1"
    return res


all_data = []
gamma = ""
with open("2021/input_files/day03") as f:
    for data in f:
        data = data.strip()
        print(f"data: {data}")
        all_data.append(data)
for i in range(len(all_data[0])):
    nb_1 = 0
    nb_0 = 0
    # Should have used Counter and most_common
    for data in all_data:
        nb_1 += 1 if data[i] == "1" else 0
        nb_0 += 1 if data[i] == "0" else 0
    gamma += "1" if nb_1 > nb_0 else "0"
    print(f"i={i} nb_1={nb_1} nb_0={nb_0}")

print(f"gamma string: {gamma}")
epsilon = flip_binary(gamma)
gamma_int = int(gamma, 2)
epsilon_int = int(epsilon, 2)
print(f"gamma: {bin(gamma_int)} {gamma_int}")
print(f"epsilon: {bin(epsilon_int)} {epsilon_int}")
print(f"Result: {gamma_int*epsilon_int}")
