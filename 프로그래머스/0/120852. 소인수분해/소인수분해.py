def solution(n):
    answer = []
    a = 2
    while a <= n:
        if n % a == 0:
            n /= a
            if a not in answer:
                answer.append(a)
        else:
            a += 1
    return answer