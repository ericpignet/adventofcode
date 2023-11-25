import re

with open("2020/input_files/day04") as f:
    data = "".join([line for line in f])
    raw_passports = [group for group in data.split("\n\n")]

def validate_field(name: str, value: str):
    # match only available from python 3.10
    if name == 'byr':
        return re.match(r'\d{4}', value) and 1920 <= int(value) <= 2002
    elif name == 'iyr':
        return re.match(r'\d{4}', value) and 2010 <= int(value) <= 2020
    elif name == 'eyr':
        return re.match(r'\d{4}', value) and 2020 <= int(value) <= 2030
    elif name == 'hgt':
        match = re.match(r'(\d+)(cm|in)', value)
        if not match:
            return False
        if match.group(2) == 'cm':
            return 150 <= int(match.group(1)) <= 193
        else:
            return 59 <= int(match.group(1)) <=76
    elif name == 'hcl':
        return re.match(r'#[0-9a-f]{6}', value)
    elif name == 'ecl':
        return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    elif name == 'pid':
        return re.match(r'\d{9}$', value)
    elif name == 'cid':
        return True

nb_valid = 0
for raw_passport in raw_passports:
    fields = raw_passport.replace('\n', ' ').split()
    is_valid = True
    for required_field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
        field_ok = False
        for field in fields:
            if required_field+':' == field[:4]:
                if validate_field(required_field, field[4:]):
                    field_ok = True
                break
        if not field_ok:
            is_valid = False
            break
    if is_valid:
        nb_valid += 1
    #print(f"{raw_passport}\n{is_valid=}\n")
        
print(f"{nb_valid=}")