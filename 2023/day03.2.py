with open("2023/input_files/day03") as f:
    lines = [line.rstrip() for line in f]

def isSymbol(char):
    return not s_char.isdigit() and s_char != '.'

part1 = 0
part2 = 0
gear_dict = {}

def addGear(s_char, coords, part_nb):
    if s_char=='*':
        if coords in gear_dict:
            gear_dict[coords].append(int(part_nb))
        else:
            gear_dict[coords] = [ int(part_nb) ]

for i_line, line in enumerate(lines):
    part_nb = ''
    nb_ongoing = False
    for i_char, char in enumerate(line):
        if char.isdigit():
            part_nb += char
            if i_char==len(line)-1 or (i_char<len(line)-1 and not line[i_char+1].isdigit()):
                #Nb is finished
                print(part_nb)
                # Check if if it's near a symbol
                is_near = False
                start = 0
                if i_char-len(part_nb)>0:
                    start = i_char-len(part_nb)
                end = i_char+2 if i_char<len(line) else i_char+1

                if i_line>=1:
                    for i_s_char, s_char in enumerate(lines[i_line-1][start:end]):
                        is_near = is_near or isSymbol(s_char)
                        addGear(s_char, (i_line-1, i_s_char+start), part_nb)
                for i_s_char, s_char in enumerate(lines[i_line][start:end]):
                    is_near = is_near or isSymbol(s_char)
                    addGear(s_char, (i_line, i_s_char+start), part_nb)
                if i_line<len(lines)-1:
                    for i_s_char, s_char in enumerate(lines[i_line+1][start:end]):
                        is_near = is_near or isSymbol(s_char)
                        addGear(s_char, (i_line+1, i_s_char+start), part_nb)

                if is_near:
                    part1 += int(part_nb)
                part_nb = ''

        #elif i>0 and line[i-1].isdigit():
            # not a digit but previous character was
for coord, numbers in gear_dict.items():
    if len(numbers) == 2:
        part2 += numbers[0] * numbers[1]
print(f"{part1=}")
print(f"{part2=}")

