def solution(n):
    p = 6
    while p % n != 0:
        p += 6
    return p/6