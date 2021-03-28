def front_back(str):
    if len(str) <= 1:
        return str

    mid = str[1:len(str) - 1]
    b = str[len(str) - 1]
    f = str[0]
    return b + mid + f

