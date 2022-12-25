from itertools import count

SNAFU_TO_DECIMAL = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
DECIMAL_TO_SNAFU = {v: k for k, v in SNAFU_TO_DECIMAL.items()}

with open("2022/input_files/day25") as f:
    snafu_numbers = [line.rstrip() for line in f]


def snafu_to_decimal(snafu: str) -> int:
    return sum(SNAFU_TO_DECIMAL[snafu[len(snafu) - i - 1]] * 5**i for i in range(len(snafu)))


def decimal_to_snafu(decimal: int) -> str:
    def make_maxima():
        cur = 0
        yield 0
        for power_of_5 in count(0):
            yield cur + 1 * 5**power_of_5
            yield cur + 2 * 5**power_of_5
            cur += 2 * 5**power_of_5

    remaining = decimal
    snafu = {}
    while abs(remaining) > 0:
        sign = 1 if remaining > 0 else -1
        i = next(i for i, x in enumerate(make_maxima()) if x >= abs(remaining))
        number_needed = 2 - i % 2  # do I need 1 or 2 of this power of 5?
        power_of_5 = i // 2 + 1 - number_needed
        snafu[power_of_5 + 1] = number_needed * sign
        new_value = number_needed * sign * 5**power_of_5

        remaining = remaining - new_value

    return "".join(DECIMAL_TO_SNAFU[snafu[i] if i in snafu else 0] for i in range(max(snafu.keys()), 0, -1))


decimal_total = sum(snafu_to_decimal(snafu) for snafu in snafu_numbers)
print(f"Part 1: {decimal_total=}")
print(f"Part 2: {decimal_to_snafu(decimal_total)=}")
