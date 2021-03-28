def lone_sum(a, b, c):
    return Counter(a, b, c)


def Counter(a, b, c):
    if a == b == c:
        return 0
    elif a == b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a
    return a + b + c



