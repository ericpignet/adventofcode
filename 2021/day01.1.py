total_increases = 0
prev_measurement = 99999
with open("2021/input_files/day01") as f:
    for data in f:
        data = int(data.strip())
        if data > prev_measurement:
            total_increases += 1
        prev_measurement = data

print(f"Total increases: {total_increases}")
