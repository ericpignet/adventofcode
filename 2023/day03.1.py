with open("2023/input_files/day03") as f:
    lines = [line.rstrip() for line in f]

def isSymbol(char):
    return not s_char.isdigit() and s_char != '.'

res = 0
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
                    for s_char in lines[i_line-1][start:end]:
                        if isSymbol(s_char):
                            is_near = True
                for s_char in lines[i_line][start:end]:
                    if isSymbol(s_char):
                        is_near = True
                if i_line<len(lines)-1:
                    for s_char in lines[i_line+1][start:end]:
                        if isSymbol(s_char):
                            is_near = True

                if is_near:
                    res += int(part_nb)
                part_nb = ''

        #elif i>0 and line[i-1].isdigit():
            # not a digit but previous character was
print(f"{res=}")

