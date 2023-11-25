with open("2020/input_files/day04") as f:
    data = "".join([line for line in f])
    raw_passports = [group for group in data.split("\n\n")]

nb_valid = 0
for raw_passport in raw_passports:
    fields = raw_passport.replace('\n', ' ').split()
    is_valid = True
    for required_field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
        field_ok = False
        for field in fields:
            if required_field+':' == field[:4]:
                field_ok = True
                break
        if not field_ok:
            is_valid = False
            break
    if is_valid:
        nb_valid += 1
        
print(f"{nb_valid=}")