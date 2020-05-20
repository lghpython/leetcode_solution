def reverse(x: int) -> int:
    num = str(x)
    result = 0
    if num[0] == '-':
        result = int(num[1:][::-1]) * -1
    else:
        result = int(num[::-1])
    if result > 2**32 or result < -2**31:
        return 0
    return result




s = -2**32
print(s > -8589934592)
reverse(s)