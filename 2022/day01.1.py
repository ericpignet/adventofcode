most_calories = 0
current_elf_calories = 0
with open("2022/input_files/day01") as f:
    for data in f:
        if data.strip():
            current_elf_calories += int(data.strip())
        else:
            most_calories = max(most_calories, current_elf_calories)
            current_elf_calories = 0

print(f"Most calories: {most_calories}")
