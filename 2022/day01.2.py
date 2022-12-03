current_elf_calories = 0
all_elf_calories = []
with open("2022/input_files/day01") as f:
    for data in f:
        if data.strip():
            current_elf_calories += int(data.strip())
        else:
            all_elf_calories.append(current_elf_calories)
            current_elf_calories = 0
all_elf_calories.sort(reverse=True)

top_3 = 0
for i in range(3):
    print(f"Elf {str(i)}'s calories: {str(all_elf_calories[i])}")
    top_3 += all_elf_calories[i]
print(f"Total calories: {str(top_3)}")
