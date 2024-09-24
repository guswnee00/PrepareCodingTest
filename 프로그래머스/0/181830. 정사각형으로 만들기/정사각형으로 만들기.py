def solution(arr):
    r = len(arr)
    c = len(arr[0])
    if r > c:
        for i in range(r):
            for j in range(r - c):
                arr[i].append(0)
    else:
        for i in range(c - r):
            arr.append([0] * c)
    return arr