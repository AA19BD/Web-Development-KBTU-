def lucky_sum(a, b, c):
    return Count(a, b, c)


def Count(a, b, c):
    if a == 13:
        return 0
    elif b == 13 and a != b:
        return a
    elif c == 13 and b != c:
        return a + b
    return a + b + c

