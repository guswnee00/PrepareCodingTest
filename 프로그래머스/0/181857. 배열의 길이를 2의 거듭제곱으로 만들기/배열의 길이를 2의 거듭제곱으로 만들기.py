def solution(arr):
    c = 0
    l = len(arr)
    while l > 1:
        l = l/2
        c += 1
    return arr + [0] * (2 ** c - len(arr))
