def solution(array, n):
    answer = 0
    a = 101
    for i in sorted(array):
        if abs(i - n) < a:
            a = abs(i-n)
            answer = i
    return answer
            