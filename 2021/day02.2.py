x = 0
depth = 0
aim = 0

with open("2021/input_files/day02") as f:
    for data in f:
        (action, amount) = data.strip().split(" ")
        print(f"action: {action} amount: {amount}")
        match action:
            case "forward":
                x += int(amount)
                depth += aim * int(amount)
            case "down":
                aim += int(amount)
            case "up":
                aim -= int(amount)

print(f"Total: {x*depth}")
