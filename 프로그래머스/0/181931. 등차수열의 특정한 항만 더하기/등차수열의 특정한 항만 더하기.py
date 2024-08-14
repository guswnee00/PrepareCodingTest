def solution(a, d, included):
    answer = 0
    cnt = 0
    for idx, val in enumerate(included):
        if val == True:
            answer += idx
            cnt += 1
    return a * cnt + answer * d