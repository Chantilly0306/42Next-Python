def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    if not (2 <= from_base <= 36 and 2 <= to_base <= 36):
        return "ERROR"

    digit = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    base1, base2 = digit[:from_base], digit[:to_base]

    ten_base = 0
    for c in number:
        pos = base1.find(c)
        if pos == -1:
            return "ERROR"
        ten_base = ten_base * from_base + pos

    res = ""
    while ten_base > 0:
        res += base2[ten_base % to_base]
        ten_base //= to_base

    res = res[::-1]

    return res

print(f"{number_base_converter("1010", 2, 10)}")