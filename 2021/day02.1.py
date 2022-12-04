total_x = 0
total_depth = 0

with open("2021/input_files/day02") as f:
    for data in f:
        (action, amount) = data.strip().split(" ")
        print(f"action: {action} amount: {amount}")
        match action:
            case "forward":
                total_x += int(amount)
            case "down":
                total_depth += int(amount)
            case "up":
                total_depth -= int(amount)

print(f"Total: {total_x*total_depth}")
