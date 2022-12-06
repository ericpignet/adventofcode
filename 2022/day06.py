with open("2022/input_files/day06") as f:
    datastream = f.readline().rstrip()

# Part 1: start_packet_size = 4
# Part 2: start_packet_size = 14
start_packet_size = 14

for i in range(start_packet_size - 1, len(datastream)):
    last_packet = datastream[i - start_packet_size + 1 : i + 1]
    found = True
    for j in range(start_packet_size):
        if last_packet.count(last_packet[j]) > 1:
            found = False
            break
    if found:
        break
i += 1
print(f"{i=}")
