res = 0
with open("2023/input_files/day01") as f:
    for data in f:
        data = data.rstrip()
        current_calib = ''
        for c in data:
            if ord('0') <= ord(c) <= ord('9'):
                current_calib += c
        first_and_last = current_calib[0] + current_calib[-1]
        res += int(first_and_last)

print(f"{res=}")