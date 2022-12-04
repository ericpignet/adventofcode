total_increases = 0
prev_measurement_1 = 99999
prev_measurement_2 = 99999
last_group_measurement = 999999
with open("2021/input_files/day01") as f:
    for data in f:
        data = int(data.strip())
        current_group = prev_measurement_2 + prev_measurement_1 + data
        print(f"Current group: {current_group}")
        if current_group > last_group_measurement:
            print(f"Increase!")
            total_increases += 1
        prev_measurement_2 = prev_measurement_1
        prev_measurement_1 = data
        last_group_measurement = current_group

print(f"Total increases: {total_increases}")
