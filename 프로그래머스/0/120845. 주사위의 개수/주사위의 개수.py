def solution(box, n):
    newbox = [b//n for b in box]
    answer = 1
    for i in newbox:
        answer *= i
    return answer