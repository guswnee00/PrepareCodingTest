def solution(n, control):
    for c in range(len(control)):
        if control[c] == "w":
            n += 1
        elif control[c] == "s":
            n -= 1
        elif control[c] == "d":
            n += 10
        else:
            n -= 10
    return n