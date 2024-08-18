def solution(strArr):
    answer = [len(x) for x in strArr]
    arr = []
    for x in set(answer):
        arr.append(answer.count(x))
    return max(arr)