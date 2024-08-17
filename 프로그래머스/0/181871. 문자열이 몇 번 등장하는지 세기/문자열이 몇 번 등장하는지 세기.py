def solution(myString, pat):
    s, c = 0, 0
    while True:
        idx = myString.find(pat, s)
        if idx == -1:
            break
        c += 1
        s = idx + 1
    return c