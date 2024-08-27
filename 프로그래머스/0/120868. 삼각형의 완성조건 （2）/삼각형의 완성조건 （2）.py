def solution(sides):
    answer = 0
    maxnum = max(sides)
    minnum = min(sides)
    sumnum = sum(sides)
    for i in range(1, maxnum + 1):
        if i + minnum > maxnum:
            answer += 1
    for i in range(maxnum+1, sumnum):
        answer += 1
    return answer