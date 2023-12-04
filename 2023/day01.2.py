def digit_to_int(digit: str):
    if len(digit)>1:
        return str(all_digits.index(digit) +1)
    else:
        return digit

res = 0
all_digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
all_digits += [chr(i) for i in range(ord('0'), ord('9')+1)]
with open("2023/input_files/day01") as f:
    for i, data in enumerate(f):
        data = data.rstrip()

        all_first_indexes = {}
        for digit in all_digits:
            found = data.find(digit)
            if found != -1:
                all_first_indexes[digit] = found

        all_last_indexes = {}
        for digit in all_digits:
            found = data.rfind(digit)
            if found != -1:
                all_last_indexes[digit] = found

        min_val = 100
        first_digit = ''
        for key in all_first_indexes:
            if all_first_indexes[key]<min_val:
                min_val = all_first_indexes[key]
                first_digit = key

        max_val = -1
        last_digit = ''
        for key in all_last_indexes:
            if all_last_indexes[key]>max_val:
                max_val = all_last_indexes[key]
                last_digit = key
        calib = digit_to_int(first_digit) + digit_to_int(last_digit)
        print(f"{i} {calib=}")
        res += int(calib)

print(f"{res=}")
#
# one, two, three, four, five, six, seven, eight, and nine