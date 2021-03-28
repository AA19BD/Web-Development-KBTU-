def caught_speeding(speed, is_birthday):
    if speed <= 60 and not is_birthday:
        return 0
    elif speed >= 61 and speed <= 80 and not is_birthday:
        return 1
    elif speed >= 81 and not is_birthday:
        return 2
    elif speed <= 65 and is_birthday:
        return 0
    elif speed >= 66 and speed <= 85 and is_birthday:
        return 1
    elif speed >= 86 and is_birthday:
        return 2



